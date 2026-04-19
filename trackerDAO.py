import mysql.connector
import dbconfig as cfg

class TrackerDAO:
    connection = ""
    cursor = ""
    host = ""
    user = ""
    password = ""
    database = ""

    def __init__(self):
        self.host = cfg.mysql["host"]
        self.user = cfg.mysql["user"]
        self.password = cfg.mysql["password"]
        self.database = cfg.mysql["database"]

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def getAll(self):
        cursor = self.getcursor()
        sql = "select * from shipments"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray
    
    def findByID(self, id):
        cursor = self.getcursor()
        sql = "select * from shipments where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, shipment):
        cursor = self.getcursor()
        sql = "insert into shipments (status, planned_eta, supplier_code, supplier_name, actual_eta, item_code)"
        values = (
            shipment.get("status"),
            shipment.get("planned_eta"),
            shipment.get("supplier_code"),
            shipment.get("supplier_name"),
            shipment.get("actual_eta"),
            shipment.get("item_code")
        )
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        shipment["id"] = newid

        self.closeAll()
        return shipment

def update(self, id, shipment):
    cursor = self.getcursor()
    sql = "update shipments set status=%s, planned_eta=%s, supplier_code=%s, supplier_name=%s, actual_eta=%s, item_code=%s where id =%s"
    print(f"update shipment {shipment}")
    values = (
        shipment.get("status"),
        shipment.get("planned_eta"),
        shipment.get("supplier_code"),
        shipment.get("supplier_name"),
        shipment.get("actual_eta"),
        shipment.get("item_code"),
        id
    )
    cursor.execute(sql, values)
    self.connection.commit()
    self.closeAll()
        
def delete(self, id):
    cursor = self.getcursor()
    sql="delete from shipments where id = %s"
    values = (id,)
    cursor.execute(sql, values)
    self.connection.commit()
    self.closeAll()

def convertToDictionary(self, resultLine):
    attkeys=['id','status','planned_eta','supplier_code','supplier_name','actual_eta','item_code']
    shipment = {}
    currentkey = 0
    for attrib in resultLine:
        shipment[attkeys[currentkey]] = attrib
        currentkey = currentkey + 1 
    return shipment

trackerDAO = TrackerDAO()

#Reference:
#Python anywhere lecture
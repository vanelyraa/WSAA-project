import sqlite3
import dbconfig as cfg
from os import path

class TrackerDAO:
    connection = ""
    cursor = ""
    host = ""    
    database = ""

    def __init__(self):
        self.database = cfg.sqlite["database"]

    def getcursor(self):
        ROOT = path.dirname(path.realpath(__file__))
        self.connection = sqlite3.connect(path.join(ROOT,self.database))
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()        

    def getAll(self):
        cursor = self.getcursor()
        
        sql = """
        select
            shipments.id,
            shipments.status,
            shipments.planned_eta,
            suppliers.supplier_name,
            suppliers.country,
            shipments.actual_eta,
            shipments.item_code
        from shipments
        join suppliers
        on shipments.supplier_id = suppliers.supplier_id
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []        
        
        for result in results:            
            returnArray.append(self.convertToDictionary(result))        
        self.closeAll()
        return returnArray
    
    def findByID(self, id):
        cursor = self.getcursor()
        sql = """
        select
            shipments.id,
            shipments.status,
            shipments.planned_eta,
            suppliers.supplier_name,
            suppliers.country,
            shipments.actual_eta,
            shipments.item_code

        from shipments
        join suppliers
        on shipments.supplier_id = suppliers.supplier_id
        where shipments.id = ?
        """
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, shipment):
        cursor = self.getcursor()
        sql = "insert into shipments (status, planned_eta, supplier_id, actual_eta, item_code) values (?,?,?,?,?)"
        values = (
            shipment.get("status"),
            shipment.get("planned_eta"),
            shipment.get("supplier_id"),            
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
        sql = "update shipments set status=?, planned_eta=?, supplier_id=?, actual_eta=?, item_code=? where id =?"
        print(f"update shipment {shipment}")
        values = (
            shipment.get("status"),
            shipment.get("planned_eta"),
            shipment.get("supplier_id"),            
            shipment.get("actual_eta"),
            shipment.get("item_code"),
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
            
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from shipments where id = ?"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def convertToDictionary(self, resultLine):
        attkeys=["id","status","planned_eta","supplier_name","country","actual_eta","item_code"]
        shipment = {}
        currentkey = 0
        for attrib in resultLine:
            shipment[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return shipment

trackerDAO = TrackerDAO()

#Reference:
#Python anywhere lecture
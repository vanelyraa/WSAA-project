import sqlite3
import dbconfig as cfg
from os import path

# TrackerDAO class and database variables
class TrackerDAO:
    connection = ""
    cursor = ""
    host = ""    
    database = ""

    # Getting database name from configuration file
    def __init__(self):
        self.database = cfg.sqlite["database"]

    # Createing sqlite3 connection and returning cursor
    def getcursor(self):
        ROOT = path.dirname(path.realpath(__file__))
        self.connection = sqlite3.connect(path.join(ROOT,self.database))
        self.cursor = self.connection.cursor()
        return self.cursor

    # Close database connection
    def closeAll(self):
        self.connection.close()        

    # Get all shipment records from database
    def getAll(self):
        cursor = self.getcursor()
        
        sql = """
        select
            shipments.id,
            shipments.status,
            shipments.planned_eta,
            shipments.supplier_id,
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
    
    # Find shipment by ID
    def findByID(self, id):
        cursor = self.getcursor()
        sql = """
        select
            shipments.id,
            shipments.status,
            shipments.planned_eta,
            shipments.supplier_id,
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
        result = cursor.fetchone() # Fetch one db result
        if result is None: # Return none if shipment is not found
            return None
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    # Create new shipment in database
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

    # Updte shipment
    def update(self, id, shipment):
        cursor = self.getcursor()
        sql = "update shipments set status=?, planned_eta=?, supplier_id=?, actual_eta=?, item_code=? where id =?"
        # print(f"update shipment {shipment}")
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

    # Delete shipment        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from shipments where id = ?"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    # Convert database result to dictionary format
    def convertToDictionary(self, resultLine):
        attkeys=["id","status","planned_eta","supplier_id","supplier_name","country","actual_eta","item_code"]
        shipment = {}
        currentkey = 0
        for attrib in resultLine:
            shipment[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return shipment

trackerDAO = TrackerDAO()

#Reference:
## PythonAnywhere lecture material from module
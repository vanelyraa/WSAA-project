import sqlite3
import dbconfig as cfg
from os import path

# Supplier DAO
class SupplierDAO:

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

        sql = "select * from suppliers"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []

        for result in results:
            returnArray.append(
                self.convertToDictionary(result)
            )
        self.closeAll()
        return returnArray

    def create(self, supplier):
        cursor = self.getcursor()
        sql = "insert into suppliers (supplier_name, country) values (?,?)"
        values = (
            supplier.get("supplier_name"),
            supplier.get("country")
        )
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        supplier["supplier_id"] = newid

        self.closeAll()
        return supplier

    def convertToDictionary(self, resultLine):
        attkeys = ["supplier_id","supplier_name","country"]
        supplier = {}
        currentkey = 0
        for attrib in resultLine:
            supplier[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return supplier
    
supplierDAO = SupplierDAO()
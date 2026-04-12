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
        self.cursor = self.connection.cursor(dictionary=True)
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM shipments"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))

        self.closeAll()
        return results


trackerDAO = TrackerDAO()
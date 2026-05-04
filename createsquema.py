import sqlite3
import dbconfig as cfg
from os import path

database = cfg.sqlite["database"]

ROOT = path.dirname(path.realpath(__file__))
db_path = path.join(ROOT, database)
schema_path = path.join(ROOT, "schema.sql")

con = sqlite3.connect(db_path)
cur = con.cursor()
with open(schema_path, "r") as fp:
    sql = fp.read()

cur.executescript(sql)
con.close()


# PythonAnywhere FileNotFoundError:'schema.sql':https://stackoverflow.com/questions/34510196/python-flask-how-to-access-sqlite-database-db-on-pythonanywhere-com-without-sp
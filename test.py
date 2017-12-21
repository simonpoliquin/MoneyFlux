import sys	
import sqlite3
from DBTransaction import *


path= "C:\\Programmation\Python\MoneyFlux\MoneyFlux\MoneyDatabase.db"
db = sqlite3.connect(path)
cursor = db.cursor()


dbtransact = DBTransaction(path)
dbtransact.InsertNewTransaction('2017-12-20',500,'SIMON')

cursor.execute("SELECT * FROM [TRANSACTION]")
rows = cursor.fetchall()
 
for row in rows:
    print(row)	
db.close()





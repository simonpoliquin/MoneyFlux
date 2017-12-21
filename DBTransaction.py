from DBConnect import *

class  DBTransaction:
    def __init__(self,dbPath):
        self.dbPath = dbPath

    
    def InsertNewTransaction(self,transactionDate,amount,name):
        try:
            Connection =  DBConnect()
            db =Connection.create_connection(self.dbPath)
            cur = db.cursor()
            sql = ''' INSERT INTO [TRANSACTION](TRANSACTION_DATE,AMOUNT,NAME) VALUES(?,?,?) '''
            transaction = (transactionDate,amount,name)

            cur.execute(sql, transaction)
            db.commit()
        except Error as e:
            print(e)
            return None
        return cur.lastrowid
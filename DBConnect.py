from PyQt5 import QtSql, QtGui


class DBConnect:
    def __init__(self):
        self.DBconnection = None


    def create_connection(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            self.DBconnection = db.setDatabaseName('MoneyDatabase.db')
            return conn
        except Exception as err:
            print(err)
            return None
 

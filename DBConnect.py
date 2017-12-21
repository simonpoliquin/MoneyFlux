import sqlite3
from sqlite3 import Error


class DBConnect:
    def __init__(self):
        self.DBconnection = None


    def create_connection(self,db_file):
        try:
            conn = sqlite3.connect(db_file)
            self.DBconnection = conn
            return conn
        except Error as e:
            print(e)
            return None
 

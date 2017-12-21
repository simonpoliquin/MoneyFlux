from datetime import *
from DBConnect import *

class  Transaction:
    def __init__(self):
        self.date = None
        self.Amount = 0

    def NewTransaction(self,date,amount):
            self.date = date
            self.Amount = amount

    def DeleteTransaction(self):
        self.date =""
        self.amount = 0

    def EditTransaction(self,date,amount):
        self.date = date
        self.amount = amount

    def PrintTransaction(self):
        print("Date :"+str(self.date) + "  Montant: " + str(self.Amount) + "\n")
        

    

    
    
    

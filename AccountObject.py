import sys
from Transaction import *

class Account:
    def __init__(self):
        self.name = "Simon"
        self.balanceAsToday = 0
        self.listOfTransaction = []
        self.DateOfToday = None

    def AddNewTransactionToAccount(self,year,month,day,amount):
        x = Transaction()
        x.NewTransaction(date(year, month, day).isoformat(),amount)
        self.listOfTransaction.append(x)

    # def DeleteTransactionToAccount():

    def ShowAllTransactionFromAccount(self):
        for z in self.listOfTransaction:
            z.PrintTransaction()
            
    def SetBalance(self,balanceAmount):
        self.balanceAsToday = balanceAmount

    def SortListTransaction(self):
        self.listOfTransaction.sort(key=lambda x:x.date, reverse=False)
    
    

    #def CalculateBalanceInDateOf(self):

    

    
  

import sys
from Transaction import *
from datetime import *


class Account:
    def __init__(self):
        self.name = "Simon"
        self.balanceAsToday = 0
        self.listOfTransaction = []
        self.DateOfToday = None

    def AddNewTransactionToAccount(self,year,month,day,amount):
        x = Transaction()
        x.NewTransaction(date(year, month, day),amount)
        self.listOfTransaction.append(x)

    # def DeleteTransactionToAccount():

    def ShowAllTransactionFromAccount(self):
        for z in self.listOfTransaction:
            z.PrintTransaction()
            
    def SetBalance(self,balanceAmount):
        self.balanceAsToday = balanceAmount

    def SortListTransaction(self):
        self.listOfTransaction.sort(key=lambda x:x.date, reverse=False)
    
    

    def CalculateBalanceInDateOf(self,year,month,day):
        self.DateOfToday = date.today()
        DateToCalculate = date(year, month, day)
        sumOfTransaction = 0
        for z in self.listOfTransaction :
            if z.date > self.DateOfToday and z.date < DateToCalculate:
                sumOfTransaction = sumOfTransaction + z.Amount
        balance = (self.balanceAsToday + sumOfTransaction)
        return balance

    def SaveAccount(self,filename):
        file = open(filename,'w')
        file.write(self.name+"\n") #Name of Account
        file.write(str(self.balanceAsToday)+"\n")
        file.write(str(self.DateOfToday)+"\n")
        file.write("Transactions"+"\n")
        for z in self.listOfTransaction :
            file.write(str(z.date)+";"+str(z.Amount)+"\n")          
        file.close()

    def LoadAccount(self,filename):
       files = open(filename,'r')
       self.name = (files.readline()
       self.name = self.name.strip()
       print(self.name)
       self.balanceAsToday = files.readline()
       
       DateOfToday = files.readline()
       DateOfToday = (DateOfToday.replace("-","")
       
       print(DateOfToday)
       self.DateOfToday = datetime.strptime(DateOfToday,'%Y%m%d').date()
       Header = strip(files.readline())
       for z in files:
           line = strip(z)
           SplitString = line.split(";")
           date = SplitString[0]
           date = date.replace("-","")
           print(date)
           amount = SplitString[1]
           transaction = Transaction()
           transaction.date = datetime.strptime(date,'%Y%m%d').date()
           transaction.Amount = amount
           self.listOfTransaction.append(transaction)


    

    


                

    

    
  

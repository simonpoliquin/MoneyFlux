import sys
from Transaction import *
from AccountObject import *
from datetime import *

x = Account()
calendar = []
x.AddNewTransactionToAccount(2017, 12, 4,100)
x.AddNewTransactionToAccount(2008, 12, 4,100)
x.AddNewTransactionToAccount(2017, 12, 4,100)
x.ShowAllTransactionFromAccount()
x.SortListTransaction()
x.ShowAllTransactionFromAccount()

v = x.CalculateBalanceInDateOf(2017,12,20)
print(v)

x.SaveAccount("Chaton.txt")

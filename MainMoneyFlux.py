import sys
from Transaction import *
from AccountObject import *
from datetime import *

x = Account()
calendar = []
x.AddNewTransactionToAccount(2010, 12, 4,100)
x.AddNewTransactionToAccount(2005, 12, 4,100)
x.AddNewTransactionToAccount(2008, 12, 4,100)
x.ShowAllTransactionFromAccount()
x.SortListTransaction()
x.ShowAllTransactionFromAccount()


from os import write 


def CheckBalance():
    file_Bank = open("BankData.txt", "r")
    Balance = file_Bank.read()
    print("R",Balance)
    file_Bank.close()
    return Balance
def updateBalance(new_amount):
    file = open("BankData.txt","w")
    file.write(str(new_amount))
    new_balance = CheckBalance()
   
def withdraw(amount):
    bank_balance = float(CheckBalance())
    new_balance = bank_balance - float(amount)
    file = open("Trans.txt","a")
    file.write("Withsdrawal : - R",str(amount),"\nBalannce: R",str(new_balance))
    file.close()

CheckBalance()
Option = input("Would like to make Deposit:D or Withdrawal:W or Get Statement:S")
if Option.lower() == "d":
    desposit_amount = float(input("How much: R"))
    balance = float(CheckBalance()) + desposit_amount
    file = open("Trans.txt","a")
    file.write("Diposit: +R "+str(desposit_amount)+"\nBalance: R"+str(balance))
    file.close()
    updateBalance(balance)
    CheckBalance()
       
elif Option.lower() == 'w':
    withdraw = float(input("How much: R"))
    balance = float(CheckBalance()) - withdraw
    file = open("Trans.txt","a")
    file.write("Withdrawal: -R"+str(withdraw)- "\nBalance: R"+str(balance))
    updateBalance(balance)
    
    
    CheckBalance()    
elif Option.lower() == "s":
    file = open("Trans.txt","r")
    statement= file.read()
    print(statement)
    
UserExit = input("Would you Like to Contine with your Transaction! Y/N")
if UserExit.lower()=="n":
    print("Thank You")
#elif UserExit.lower()=="y":


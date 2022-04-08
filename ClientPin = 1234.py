ClientPin = 1234
ClientPin =str(ClientPin)
ClientBalance = [10000]
Deposition = 0
Withdrawal = 0
Balance = 0

print("WELCOME TO MY BANK")
print("Would you like to make a Transaction?")
print("(1) Yes")
print("(2) No")

EnterOption = input("Make a selection")
if EnterOption == "1":
 
    ClientPin = str(input("Please Enter your Pin:"))
    
    print("(1) Make a Deposit")
    print("(2) Make a Withdrawal")
    print("(3) Check Balance")
    print("(4) Print Statement")

    Option = input("Continue with your Transacation:")
    
    if Option == "1":
        print("Make a Deposit:")
        Deposition = float(input())
        ClientBalance = Balance + deposit:
        print("New Balance R"+ str(Balance))
        
    if (Option == '2'):
        Withdrawal()
        
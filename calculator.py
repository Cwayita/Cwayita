
# Online Python - IDE, Editor, Compiler, Interpreter
import math
import typing

print("Choose either 'investment' or 'bond' from the menu below to proceed")
print ("(1) Investment - To calculate the amount of interest you'll earn on interest")
print ("(2) Bond - To calculate the amount you'll have to pay on a home loan")
choice = input()

if choice.lower() == "i" or choice == "investment":
    print("Enter your deposit:")
    p = input()
    print("Enter your interest rate:")
    i= input()
    print("Enter your number of years:")
    n= input()
    print("Would you like to use simple or compound?")
    interestType = input()
    if interestType.lower() == "s" or interestType.lower() == "simple":
        a = float(p) * (1+(float(i)/100)*float(n))
        print("Your return on investment: " + str(a))
    
    elif interestType.lower() == "c" or interestType.lower() == "compound":
        a = (float(p) * math.pow((1 + (float(i/100)), float(n))))
        print("Your return on investment: ", str(a))




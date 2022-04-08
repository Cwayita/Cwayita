
from tkinter import *
from functools import partial
import os
from typing import Any



def register_user():
	register = Tk()
	register.geometry("500x500")
	register.title('Registration form')

	global fullname
	global Email
	global AccountNumber
	global Gender
	global Language
	global Password

	fullname = StringVar
	Email = StringVar
	AccountNumber = IntVar
	Gender = IntVar
	Language = IntVar
	Password = IntVar

	label_0 =Label(register,text="Registration form", width=20,font=("bold",20))
	label_0.place(x=90,y=60)

	label_1 =Label(register,text="Full Name", width=20,font=("bold",10))
	label_1.place(x=80,y=130)

	entry_1=Entry(register)
	entry_1.place(x=240,y=130)

	label_3 =Label(register,text="Email", width=20,font=("bold",10))
	label_3.place(x=68,y=180)

	entry_3=Entry(register)
	entry_3.place(x=240,y=180)

	label_4=Label(register,text="Account number",width=20,font=("bold",10))
	label_4.place(x=70,y=230)

	entry_4=Entry(register)
	entry_4.place(x=240,y=230)

	label_5 =Label(register,text="Gender:", width=20,font=("bold",10))
	label_5.place(x=70,y=280)

	var=IntVar()
#Creating RadioButtom
	Radiobutton(register,text="Male",padx= 5, variable= var, value=1).place(x=210,y=280)
	Radiobutton(register,text="Female",padx= 20, variable= var, value=2).place(x=290,y=280)
	
	##this creates 'Label'  wfor Language 
	label_6=Label(register,text="Language:",width=20,font=('bold',10))
	label_6.place(x=75,y=330)

	#the variable 'var1' mentioned here holds Integer Value, by default 0
	var1=IntVar()
	Checkbutton(register,text="English", variable=var1).place(x=230,y=330)
	var2=IntVar()
	Checkbutton(register,text="Isixhosa", variable=var2).place(x=290,y=330)
  
	label_3 =Label(register,text="Passowrd:", width=20,font=("bold",10))
	label_3.place(x=90,y=380)

	entry_3=Entry(register)
	entry_3.place(x=240,y=380)

	Button(register, text='Submit' , width=20,bg="black",fg='white', command = submit_Button).place(x=140,y=420)
	Button(register, text="Exit", width=20,bg="black", fg="white", command = register.destroy).plac(x=180,y=420)
    
def submit_Button():
	fullname = fullname.get()
    Email = Email.get()
    AccountNumber = AccountNumber.get()
 	Gender = Gender.get()
    Password = Password.get()
    all_accounts = os.listdir()
    
    if fullname == "" or Email == "" or AccountNumber == "" or Gender == "" or Password == "" :
        Any.config(fg="red",text=" *** Complete all field *** ")
        return
    
    for name_check in all_accounts:
        if fullname == name_check:
        Any.config(fg="red",text="Account already exists")
            return
        else:
            new_file = open(fullname,"w")
            new_file.write(fullname+'\n')
            new_file.write(Email+'\n')
            new_file.write(AccountNumber+'\n')
            new_file.write(Gender+'\n')
			new_file.write(Password+'\n')
            new_file.write('0')
            new_file.close()
            Any.config(fg="green", text="Account has been created")

		
Window = Tk()
Window.geometry("300x150")  
Window.title("Banking App")

usernameLabel = Label(Window, text="User Name").place(x=0,y=0)
usernameEntry = Entry(Window)
usernameEntry.place(x=150,y=0)  

passwordLabel = Label(Window,text="Password").place(x=0,y=50)
 
password = Entry(Window)
password.place(x=150,y=50)  

def validateLogin():
	user_name = usernameEntry.get()
	print(user_name)
loginButton = Button(Window, text="Login",command=validateLogin)
loginButton.place(x=150,y=80)


registerButton = Button(Window, text="Register",command=register_user)
registerButton.place(x=200,y=80)


def login_session():
    global login_name
    all_accounts = os.listdir()
    login = login_name.get()
    login_password = login.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            #Account_Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                #Labels
                Label(account_dashboard, text="Account Dashboard", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome", font=('Calibri',12)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Personal Details", font=('Calibri',12),width=30,command=personal_details).grid(row=2,sticky=N,pady=10)
                Button(account_dashboard, text="Deposit", font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,pady=10)
                Button(account_dashboard, text="Withdraw", font=('Calibri',12),width=30,command=withdraw).grid(row=4,sticky=N,pady=10)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red", text="Password incorrect")
                return
    login_notif.config(fg="red", text="No account found !")

	
Window.mainloop()	
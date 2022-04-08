from tkinter import *



window = Tk()
window.geometry("500x500")

def reg_fin():
    label_1 = fullname.get()
    label_3 = email.get()
    
    #label_4 = temp_gender.get()
    for name_check in 
    new_file = open(label_1,"w")
    new_file.write(label_1+'\n')
    new_file.write(label_3+'\n')
    #new_file.write(label_4+'\n')
    new_file.close()





global fullname
global email
fullname = StringVar()
email =StringVar()
#Registration form
window.title('Registration form')

label_0 =Label(window,text="Registration form", width=20,font=("bold",20))
label_0.place(x=90,y=60)


label_1 =Label(window,text="FullName", width=20,font=("bold",10))
label_1.place(x=80,y=130)


entry_1=Entry(window,textvariable = fullname)
entry_1.place(x=240,y=130)

label_3 =Label(window,text="Email", width=20,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(window,textvariable = email)
entry_3.place(x=240,y=180)

label_4 =Label(window,text="Gender", width=20,font=("bold",10))
label_4.place(x=70,y=230)


var=IntVar()

#this creates 'Radio button' widget and uses place() method
Radiobutton(window,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(window,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)


##this creates 'Label' widget for country and uses place() method.
label_5=Label(window,text="Country",width=20,font=("bold",10))
label_5.place(x=70,y=280)

#this creates list of countries available in the dropdownlist.
list_of_country=[ 'South Africa' ,'Botwana' ,'Zambia']

#the variable 'c' mentioned here holds String Value.
c=StringVar()
droplist=OptionMenu(window,c, *list_of_country)
droplist.config(width=15)
c.set('Select your Country')
droplist.place(x=240,y=280)

##this creates 'Label'  wfor Language 
label_6=Label(window,text="Language",width=20,font=('bold',10))
label_6.place(x=75,y=330)

#the variable 'var1' mentioned here holds Integer Value, by default 0
var1=IntVar()
Checkbutton(window,text="English", variable=var1).place(x=230,y=330)
var2=IntVar()
Checkbutton(window,text="Isixhosa", variable=var2).place(x=290,y=330)


Button(window, text='Submit', command=reg_fin, width=20,bg="black",fg='white').place(x=180,y=380)


window.mainloop()
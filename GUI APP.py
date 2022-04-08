from tkinter import *

master = Tk()
master.config(bg='#0B5A81')

f = ('Times', 14)

frame = Frame(master, bd=2, bg='#CCCCCC',   relief=SOLID, padx=10, pady=10)
Label(frame, text="Enter Username:", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(frame, text="Enter Password:", bg='#CCCCCC',font=f).grid(row=1, column=0, pady=10)

username_tf = Entry(frame, font=f)
password_tf = Entry(frame, font=f,show='*')
login_btn = Button(frame, width=15, text='Login', font=f, relief=SOLID,cursor='hand2',command=None)
register_btn = Button(frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2',command=None

username_tf.grid(row=0, column=1, pady=10, padx=20)
password_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
register_btn.grid(row=3, column=1, pady=10, padx=20)
frame.pack()

master.mainloop()
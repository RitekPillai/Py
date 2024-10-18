

from tkinter import * 
root=Tk()
user=Label(root,text="Email:")
user.grid()
passw=Label(root,text="Password:")
passw.grid(row=1)
userv=StringVar()
uservalue=Entry(root,textvariable=userv,)
uservalue.grid(row=0,column=1)
passv=StringVar()
passvalue=Entry(root,textvariable=passv,)
passvalue.grid(row=1,column=1)

def display():
    print("Email:",userv.get())
    print("Password:",passv.get())


button=Button(root,text="Submit",command=display)
button.grid(row=3,column=1)
root.mainloop()

"""
#scale
from tkinter import *
root=Tk()
s1=Scale(root,from_=0,to=100,orient="horizontal")
s1.pack()
s2=Scale(root,from_=0,to=5000)
s2.pack()
root.mainloop()

"""
from tkinter import *

root= Tk()
msg = Message(root,text="hello everyone",width=500)
msg.config(bg="red",font=('times',24,'bold'))
msg.pack()
mainloop()

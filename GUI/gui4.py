"""
pracitcal 9e

from tkinter import *
root=Tk()
msg=Message(root,text="hello everyone",width=1000)
msg.config(bg="red",font=("times",50,"italic"))
msg.pack()
root.mainloop()


practical 9g 
from tkinter import *
root=Tk()
l=Listbox(root)
l.pack()
l.insert(0,"data structue")
l.insert(1,"Python")
l.insert(2,"CN")
l.insert(3,"os")
l.insert(4,"maths")


root.mainloop()


spinbox practical 9h

from tkinter import *
root=Tk()
s1=Spinbox(root,from_=0,to=50)
s1.pack()
s2=Spinbox(root,values=[1,2,3,4,5,67,9,5]).pack()
root.mainloop()

chekcbox

from tkinter import *
root=Tk()
v1=IntVar()
v2=IntVar()
frame=Frame(root,bg="pink",)

def display():
    print("Male:",v1.get()," Female:",v2.get())
check1=Checkbutton(root,text="Male",variable=v1).pack()
check2=Checkbutton(root,text="FeMale",variable=v2).pack()
b=Button(root,text="print",command=display).pack()
root.mainloop
"""
from tkinter import *
root=Tk()
frame=Frame(root,bg="pink")
frame.pack()
b1=Button(frame,text="W").pack(side=TOP)
b1=Button(frame,text="A").pack(side=LEFT)
b1=Button(frame,text="S").pack(side=LEFT)
b1=Button(frame,text="D").pack(side=LEFT)
root.mainloop()
 

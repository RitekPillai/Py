#button
from tkinter import *
from tkinter import messagebox
root=Tk()
def message1():
    messagebox.showinfo("infomessage","Good Night")
def message2():
     messagebox.showerror("Errormessage","Error in your program")
def message3():
     messagebox.showwarning("Warningmessage","Warining message")
def m4():
     messagebox.askretrycancel("message","message")
b=Button(root,text="info message",command=message1,bg="Black",fg="blue")
b1=Button(root,text="errror message",command=message2,bg="Black",fg="blue")
b2=Button(root,text="warning message",command=message3,bg="Black",fg="blue")
b3=Button(root,text="idk",command=m4)
b.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()

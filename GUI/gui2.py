from tkinter import * 
from tkinter import messagebox
root=Tk()
def m1():
     messagebox.showinfo("Information","Good night")
def m2():
     messagebox.showerror("Error Page ","ERROR")
def m3():
     messagebox.showwarning("Warning page ","Warning")
def m4():
     messagebox.askokcancel("okcancelpage","Try again")
def m5():
     messagebox.askyesno("Alert","Are you sure?")
def m6():
     messagebox.askquestion('q',"Are you good man?")
def m7():
     messagebox.askretrycancel('retry',"not working")

Button(root,text="Info",command=m1).pack()
Button(root,text="info",command=m2).pack()
Button(root,text="Info",command=m3).pack()
Button(root,text="Info",command=m4).pack()
Button(root,text="Info",command=m5).pack()
Button(root,text="Info",command=m6).pack()
Button(root,text="Info",command=m7).pack()


root.mainloop()
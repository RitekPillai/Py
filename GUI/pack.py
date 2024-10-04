from tkinter import *
root=Tk()

Button(root,text="Red",background="red").pack(fill=X,ipadx=10,ipady=30)
Button(root,text="Blue",background="blue").pack(padx=10,pady=30,side=LEFT)

root.mainloop()
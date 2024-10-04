from tkinter import *
root=Tk()
Label(root,text="Name:").grid(row=0,column=0)
Entry(root).grid(row=0,column=1)
Label(root,text="Moblie:").grid(row=1,column=0)
Entry(root).grid(row=1,column=1)

Label(root,text="Age:").grid(row=2,column=0)
Entry(root).grid(row=2,column=1)

Button(root,text="Submit").grid(row=3,column=0)
Button(root,text="Exit").grid(row=3,column=1)

root.mainloop()
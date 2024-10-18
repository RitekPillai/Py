#gui1
from tkinter import *
root=Tk()
t=Text(root,height=3,width=50).pack()
t.insert(END,"hello\neveryone\n")
farme = Frame(root)
farme.pack()
b1 = Button(farme,text="one",bg="red")
b1.pack()
root.mainloop()
 

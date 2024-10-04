from tkinter import *
root=Tk()
label = Label(root,text="List of Grades")
l=Listbox(root)

l.pack()
l.insert(1,"Grade A")
l.insert(0,"Grade A+")

l.insert(END,"Grade D")
l.curselection()
print(l.get(1))
l.delete(first=1,)
root.mainloop()
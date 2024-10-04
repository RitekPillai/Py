from tkinter import *
root=Tk()

scroll=Scrollbar()
scroll.pack(side=LEFT,fill=Y)

l=Listbox(root,yscrollcommand=scroll.set)
l.pack()
for i in range(20+1):
  
    l.insert(i,str(i))
scroll.config(command=l.yview)
root.mainloop()


from tkinter import * 
root=Tk()
var1=IntVar()
var2=IntVar()
def var_states():
    
    print("Male:",var1.get(),"\n Female:",var2.get())

Checkbutton(root,text="Male",variable=var1).pack()


Checkbutton(root,text="Female",variable=var2).pack()
Button(root,text="Show Result",command=var_states).pack()

root.mainloop()


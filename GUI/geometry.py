from tkinter import *
root=Tk()

Button(root,text="red",borderwidth=10,cursor="circle",activeforeground="red",activebackground="yellow").place(relx=.5,rely=.5)
Button(root,text="green").place(width=100)

Button(root,text="yello").place(relx=.2,rely=.8)

root.mainloop()
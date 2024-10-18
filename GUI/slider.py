from tkinter import *
root=Tk()
s1=Scale(root,activebackground="grey",from_=10,to=100,background="light blue").pack()
s2=Scale(root,from_=100,to=1000,activebackground="blue",orient=HORIZONTAL).pack()
root.mainloop()
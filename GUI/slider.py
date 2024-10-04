from tkinter import *
root=Tk()
s1=Scale(root,orient=HORIZONTAL ,to=50.3,from_=1.1,)
s1.pack()

def getscale():
    print(s1.get())

button = Button(root,command=getscale,text="Get Value")
button.pack()
root.mainloop()
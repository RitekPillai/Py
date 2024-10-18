from tkinter import *
root=Tk()

values=["python","c++","c","Dart"]

Label(root,text="Select your language").pack()
v=StringVar()
v.set(values[0])
def display():
    print("you language is:",v.get())

for i in range(len(values)):
    Radiobutton(root,command=display,text=values[i],value=values[i],variable=v).pack(anchor=W)


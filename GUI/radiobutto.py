from tkinter import *
root=Tk()

values=["o","A+","A","B"]
v = StringVar()   
v.set(values[1])  # Set the default value

def showvalue():
    print("you have got ", v.get(),"grade")
Label(root,text="Enter The Student Grade:").pack()
for i, value in enumerate(values):#value is used to get default value and variable that store the selected data
    Radiobutton(root, command=showvalue, variable=v, value=value, text=value).pack(anchor=W)

root.mainloop()
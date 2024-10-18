import mysql.connector
from tkinter import * 
mydb=mysql.connector.connect(host='localhost',password='1234',user='root')
cur=mydb.cursor()

root=Tk()
def delete():
    pass

Label(root,text="Enter the Id you want to delete").grid(row=0,column=1)
Label(root,text="EmpId:").grid(row=1,column=0)
eid=Entry(root)
eid.grid(row=1,column=1)
Button(root,command=delete,text=delete).grid(row=3,column=1)

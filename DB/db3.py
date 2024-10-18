import mysql.connector
from tkinter import *
mydb=mysql.connector.connect(host='localhost',password='1234',user='root')
cur=mydb.cursor()

def insert():
    emp_id = ide.get()
    emp_name = name.get()
    salary = sal.get()
    cur.execute("USE ABHISHEK")
    cur.execute('INSERT INTO EMP(EMPID,ENAME,SAL) VALUES(%s,%s,%s)',(emp_id,emp_name,salary))
    print("Values Inserted Successfully")
    mydb.commit()#save the changes
    mydb.close()

def display():
    cur.execute("USE ABHISHEK")
    cur.execute("SELECT * FROM EMP")
    
    print(cur.fetchall())

root=Tk()
Label(root,text="Enter values in Tabels").grid(row=0,column=1)
Label(root,text="EmpID:").grid(row=1,column=0)
ide=Entry(root)
ide.grid(row=1,column=1)
Label(root,text="Ename:").grid(row=2,column=0)
name=Entry(root)
name.grid(row=2,column=1)
Label(root,text="SALARY:").grid(row=3,column=0)
sal=Entry(root)
sal.grid(row=3,column=1)
b=Button(root,text="Insert",command=insert).grid(row=4,column=1)
b1=Button(root,text="show Values",command=display).grid(row= 4, column=3)
root.mainloop()

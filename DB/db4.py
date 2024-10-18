import mysql.connector
mydb=mysql.connector.connect(host='localhost',password='1234',user='root')
from tkinter import *
cur=mydb.cursor()

def update():
    cur.execute("USE ABHISHEK")
    s="UPDATE EMP SET SAL=%s WHERE EMPID=%s"
    sal=sal_entry.get()
    eid=ide.get()
    cur.execute(s,(sal,eid))
    print("Update Seccessfully")
    cur.execute("SELECT * FROM EMP")
    print(cur.fetchall())
    mydb.commit() 




root=Tk()
Label(root,text="EmpID:").grid(row=0,column=0)
ide=Entry(root)
ide.grid(row=0,column=1)
Label(root,text="ENTER THE UPDATED SALARY:").grid(row=1,column=0)
sal_entry=Entry(root)
sal_entry.grid(row=1,column=1)
b=Button(root,text="UPDATE",command=update).grid(row=2,column=1)

root.mainloop()

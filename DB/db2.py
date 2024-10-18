import mysql.connector
mydb=mysql.connector.connect(host='localhost',password='1234',user='root')
cur=mydb.cursor()

cur.execute('USE ABHISHEK')
cur.execute('DROP TABLE EMP')
cur.execute('CREATE TABLE EMP(EMPID INT NOT NULL,ENAME VARCHAR(20) NOT NULL,SAL INT NOT NULL,PRIMARY KEY(EMPID))ENGINE=INNODB')
print("Table Create successfully")
cur.execute('SHOW TABLES')
result=cur.fetchall()
print(result)
mydb.close()

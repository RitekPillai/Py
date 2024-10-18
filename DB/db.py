import mysql.connector 
mydb = mysql.connector.connect(host='localhost',password='1234',user='root')
cur=mydb.cursor()

try:
    cur.execute("SHOW DATABASES")
    print(cur.fetchall())
except OSError as err:
  print("failed to create db:{}",format(err))
mydb.close()

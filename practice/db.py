import mysql.connector 
conn = mysql.connector.connect(host='Abhi',password='1234',user='root')
if conn.is_connected():
    print("done")


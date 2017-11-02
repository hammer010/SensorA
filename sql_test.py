import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="XXX", database="test1")
cursor = conn.cursor()
conn.close()
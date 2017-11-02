import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="pi",password="raspberry", database="test")
cursor = conn.cursor()








conn.close()

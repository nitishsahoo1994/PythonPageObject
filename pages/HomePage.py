import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='tiger')
print(mydb.connection_id)

import mysql.connector as sql
db = sql.connect(host="sanchitlogger-vm1.centralindia.cloudapp.azure.com", password="Password@1234", user="sanchitlogger", database="msms")
if db.is_connected()==True:
    print("Connection Success")
else:
    print("connection failes")
cur= db.cursor()
db.close()
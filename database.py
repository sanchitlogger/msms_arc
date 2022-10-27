
import mysql.connector as sql
with sql.connect(host="sanchitlogger-vm1.centralindia.cloudapp.azure.com", user="sanchitlogger", passwd="Password@1234", database="msms") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table")
    for row in cursor:
        print(row)

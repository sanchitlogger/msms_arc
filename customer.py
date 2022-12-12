import mysql.connector as con
import datetime as dt
import zoneinfo as zi


file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()


db = con.connect(host=f"{host}",user=f"{user}",password=f"{passwd}",database=f"{dbs}")
cur = db.cursor()

def add_cust():
    
    ex1 = cur.execute("insert into customers(f_name,l_name,main_phone,alt_phone,last_purchased,total_purchased,currency,email) values()")


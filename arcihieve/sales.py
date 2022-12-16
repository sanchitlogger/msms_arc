import mysql.connector as con
db = con.connect(host=f"{host}",user=f"{user}",password=f"{passwd}",database=f"{dbs}")
cur = db.cursor()




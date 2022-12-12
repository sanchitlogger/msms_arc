from cryptography import fernet as fer
import mysql.connector as con
import datetime as dt
import zoneinfo as zi
import getpass as pas

file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()
# db = con.connect(host=f"{host}", user=f"{user}", password=f"{passwd}", database=f"{dbs}")
# cur = db.cursor()

from tkinter import *
root = Tk()



root.mainloop()
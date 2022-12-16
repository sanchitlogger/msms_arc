from cryptography import fernet as fer
import mysql.connector as con
import datetime as dt
import zoneinfo as zi
import getpass as pas
import tkinter.ttk as ttk
from tkinter import *

root = Tk()

frame1=Frame(root)
frame1.grid()
var1=StringVar()
l1=["monday","Tuesday","Wendnesday","Thursday","Friday","Saturday","Sunday"]
var1.set(l1[0])
cb=ttk.Combobox(frame1,values=l1,textvariable=var1)
cb.grid()
root.mainloop()


file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()
# db = con.connect(host=f"{host}", user=f"{user}", password=f"{passwd}", database=f"{dbs}")
# cur = db.cursor()


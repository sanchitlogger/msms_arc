from cryptography import fernet as fer
import mysql.connector as con
import getpass as pas
from tkinter import *
import PIL
from time import strftime
import sys
"""
variable is named as first-alphabet_frame-number_var-number.
"""
"""
file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()
db = con.connect(host=f"{host}", user=f"{user}",password=f"{passwd}", database=f"{dbs}")
cur = db.cursor


db.close()
"""

root = Tk()
root.title("Medical shop management system")
# start of row 1
frame=Frame(root)
frame.grid(row=0)
def time():
    now = strftime('%H:%M:%S')
    l1_.config(text=now)
    l1_.after(1000, time)
l1_ = Label(frame)
l1_.grid() 

# start of row 2
frame2=Frame(root)
frame2.grid(row=1)

# start of row 3
frame3=Frame(root)
frame3.grid(row=3)

# start of row 4
frame4=Frame(root)
frame4.grid(row=4)

root.mainloop()


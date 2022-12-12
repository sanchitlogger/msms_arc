from cryptography import fernet as fer
import mysql.connector as con
import getpass as pas
from tkinter import *
from tkinter import ttk
import PIL
from time import strftime
import sys


file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()

root = Tk()
root.title("Medical shop management system")
root.geometry('1000x700+200+100')
root.resizable(False, False)

head=Frame(root,height=150,width=1000,background="#f0f3f9")
head.place(x=0,y=0)

border=Frame(root,height=3,width=1000,background="grey")
border.place(x=0,y=145)
border2=Frame(root,height=2,width=1000,background="grey")
border2.place(x=0,y=147)

body = Frame(root,height=550,width=1000,background="#f0f3f9")
body.place(x=0,y=150)


body1= Frame(body,height=200,width=1000,highlightbackground="yellow",highlightthickness=2,background="#f0f3f9")
body1.place(x=0,y=50)
button1=Button(body1,cursor="hand2",relief="solid",text="Medicines")
button1.place(x=250,y=100)


button2=Button(body1,cursor="hand2",relief="solid",text="Sales")
button2.place(x=450,y=100)

button3=Button(body1,cursor="hand2",relief="solid",text="Trades")
button3.place(x=650,y=100)


body2=Frame(body,height=200,width=1000,highlightbackground="orange",highlightthickness=2,background="#f0f3f9")
body2.place(x=0,y=250)
button4=Button(body2,cursor="hand2",relief="solid",text="customers")
button4.place(x=250,y=100)

button5=Button(body2,cursor="hand2",relief="solid",text="employees")
button5.place(x=450,y=100)

button6=Button(body2,cursor="hand2",relief="solid",text="users")
button6.place(x=650,y=100)

root.mainloop()

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


db = con.connect(host=f"{host}", user=f"{user}", password=f"{passwd}", database=f"{dbs}")
cur = db.cursor()


def create_user():
    # This function is used to create new user
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()

        f_name = input("Enter first name: ").title()
        l_name = input("Enter last name: ").title()
        gender = input("Enter gender(M/F): ").lower()
        gender.strip()
        username = input("Enter username: ").lower()
        a = 1
        while a == 1:
            password1 = pas.getpass(prompt="Enter password: ")
            password2 = pas.getpass(prompt="Renter password: ")
            if password1 == password2:
                key = fer.Fernet.generate_key()
                fernet = fer.Fernet(key)
                encrypted = fernet.encrypt(password1.encode())
                cur.execute(
                    "INSERT INTO users (f_name , l_name, username, gender, pass, secret) VALUES (%s, %s, %s, %s, %s, %s)",
                    (f_name, l_name, username, gender, encrypted, key))
                b = db.commit()
                print("User created successfully")
                a = 0
            else:
                print("Wrong Password. Try again!")
                a = 1
        return a


def user_login():
    # This function is used to log user in the system.
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        const = 0
        login = 0
        while const <2:
            username = input("Enter username:").lower()

            exe1 = cur.execute(f"select f_name,l_name,gender from users where username = '{username}'")
            b = cur.fetchone()
            if b == None:
                const +=1
                print("re check username")
            if b != None:
                const +=3    
        if const ==2:
            print("User not found, Contact admin to create user.")    
         # login prompt should be closed after this..s   
        else:
            while login <2:
                if b[2]=="m":
                    print(f"Hello Mr {b[0].title()} {b[1].title()}.")
                if b[2]=="f":
                    print(f"Hello Mrs {b[0].title()} {b[1].title()}.")
                passin = pas.getpass(prompt="Enter password: ")

                exe2=cur.execute(f"select secret,pass from users where username = '{username}'")
                c =cur.fetchone()
                fernet2 = fer.Fernet(c[0])
                decrypted = fernet2.decrypt(c[1].encode())
                if decrypted.decode()==passin:
                    print("Login successful .")
                    return "Welcome "+username
                else:
                    login += 1
                    print("Login unsuccessful")    


def data_in(b, c, d, e, f, g, h, i):
    lt1 = []
    while True:
        tup = ()

        def gen_trade_id():
            a = dt.datetime.now().strftime("%H%M%S%d%m%y" + d)
            return a

        def medi_code():
            exe1 = cur.execute("select medi_code from trades")
            fe1 = cur.fetchall()
            const1 = 0
            list1 = ["A", "B", "C", "D", "E"]
            for i in fe1:
                if i[0] == d:
                    const1 += 1
                    return b

        tup = (gen_trade_id(),)
    a = cur.execute(
        "insert into table trades(trade_id,brand,medi_code,medi_name,medi_mfg,medi_exp,quantity,price,deal_init,partner_id) values(%s,%s,%s,v%s,%s,%s,%s,%s,%s)",
        lt1)

    db.commit()


"""
# this algo will be used to enter item after every recurring entry.
a = 1
b = []
while a ==1:
    x = 10
    tup = ()
    c = input("ENtry1")
    d = input("ENtry2")
    e = input("ENtry3")
    f = input("ENtry4")
    g = input("ENtry5")
    tup = (c,d,e,f,g)
    b.append(tup)
    while x == 10:
        a = int(input("What to enter more? (0/1)"))
        if a==1 and a !=0:
            x = 11
        if a !=1 and a ==0:
            x = 11
        else:
            x = 11
            print("Please enter either 0 or 1")
    print(b)
"""


def sync(lst):
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        ex1 = cur.execute("select medi_code from medicines")
        fe1 = cur.fetchall()
        for i in fe1:
            for j in lst:
                if i[0] == j[2[:-1]]:
                    ex1 = cur.execute("update medicines set quantity += j[6] where medi_code = i[0] ")
                if i[0] != j[2[:-1]]:
                    ex2 = cur.execute("insert into medicines ")


def data_view():
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        b = cur.execute("insert into t")
        print(b)


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

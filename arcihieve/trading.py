import mysql.connector as con
import datetime as dt
import zoneinfo as zi
from tkinter import *
from tkinter import ttk
file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()
"""
with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
"""
#db = con.connect(host=f"{host}", user=f"{user}", password=f"{passwd}", database=f"{dbs}")
#cur = db.cursor()


root=Tk()

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

def trades():
    root.geometry('800x600+300+90')
    root.title("MSMS - Trades")
    head=Frame(root,width=800,height=170,highlightbackground="black",highlightthickness=3)
    usr=Frame(head,width=200,height=170,highlightbackground="blue",highlightthickness=2)
    today_info = Frame(head,width=200,height=170,highlightbackground="red",highlightthickness=2)
    head.place(x=0,y=0)
    usr.place(x=0,y=0)
    today_info.place(x=600,y=0)
    body3=Frame(root,width=800,height=430)
    body3.place(y=170,x=0)

    def enter():
        form1=Frame(body3,height=430,width=677)
        form1.place(y=0,x=0)
        cb_tup=["hello","World"]
        cb = ttk.Combobox(form1,values=cb_tup,state="readonly",width=10)
        cb.set(cb_tup[0])
        cb.place(x=10,y=10)
    def view():
        view1=Frame(body3,height=430,width=677,highlightbackground="orange",highlightthickness=2)
        ttk.Treeview()

    rig_butt=Frame(body3,height=430,width=122,highlightbackground="blue",highlightthickness=3)
    rig_butt.place(y=0,x=678)
    b1=Button(rig_butt,text="View",width=6)
    b1.place(y=80,x=15)
    b2=Button(rig_butt,text="Enter",width=6,command=enter)
    b2.place(y=150,x=15)
    b3=Button(rig_butt,text="Update",width=6)
    b3.place(y=220,x=15)
    b4=Button(rig_butt,text="Export",width=6)
    b4.place(y=290,x=15)

    

trades()

root.mainloop()
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
    for i in b:        
        print(i)



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
"""
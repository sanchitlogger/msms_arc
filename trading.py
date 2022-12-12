import mysql.connector as con
import datetime as dt
import zoneinfo as zi

file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()
"""
with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
"""
db = con.connect(host=f"{host}", user=f"{user}", password=f"{passwd}", database=f"{dbs}")
cur = db.cursor()


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

from cryptography import fernet as fer
import mysql.connector as con
import datetime as dt
file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()
"""
with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
"""





def data_in(b,c,d,e,f,g,h,i):
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        def gen_trade_id():
            print("hello")
        a = cur.execute(f"""insert into table trades(trade_id,company,brand,medi_code,medi_name,medi_mfg,medi_exp,quantity,price,deal_init) values({gen_trade_id()},{b},{c},{d},{e},{f},{g},{h},{i})""")
        print(a)


def data_update():
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        b = cur.execute("insert into t")
        print(b)

def data_del():
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        b = cur.execute("insert into t")
        print(b)

def data_out():
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        b = cur.execute("insert into t")
        print(b)

def data_export():
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        b = cur.execute("insert into t")
        print(b)
        
"""
def data_update():
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        b = cur.execute("insert into t")
        print(b)
"""        
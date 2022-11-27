from cryptography import fernet as fer
import mysql.connector as con

file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()
"""
with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
"""
def gen_trade_id():




def data_in():
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        a = input(" Enter company name: ")
        b = input("Enter Brand: ")
        c = input("Enter medicine name: ")
        d = input("Enter medicine code: ")
        e = input("enter mfg data(yyyy-mm-dd): ")
        f = input("enter exp data(yyyy-mm-dd): ")
        g = int(input("Enter quantity: "))
        i = float(input("Enter price: "))
        j = input("enter deal initiated data(yyyy-mm-dd): ")
        k = input("enter deal finalized data(yyyy-mm-dd): ")
        l = input("enter delivered data(yyyy-mm-dd): ")




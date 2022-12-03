from cryptography import fernet as fer
import mysql.connector as con
import getpass as pas

file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()



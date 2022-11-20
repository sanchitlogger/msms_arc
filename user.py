# This program will be used to create new users and add them to the database
from cryptography import fernet as fer
import pickle
import mysql.connector as con

with con.connect(host="sanchitlogger-vm1.centralindia.cloudapp.azure.com",user="sanchitlogger",password="Password@1234",database="msms") as db:
    cur = db.cursor()
    def create_user():
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        gender = input("Enter gender(M/F): ").lower()
        key = fer.Fernet.generate_key()
        fernet = fer.Fernet(key)
        encrypted = fernet.encrypt(password.encode())
        cur.execute("INSERT INTO users (f_name , l_name, username, gender, pass, secret) VALUES (%s, %s, %s, %s, %s, %s)", (f_name, l_name,username, gender, encrypted, key))
        db.commit()
        print("User created successfully")
    
    def user_login():


# This program will be used to create new users and add them to the database
from cryptography import fernet as fer
import mysql.connector as con
import getpass as pas

with con.connect(host="sanchitlogger-vm1.centralindia.cloudapp.azure.com",user="sanchitlogger",password="Password@1234",database="msms") as db:
    cur = db.cursor()
    def create_user():
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        gender = input("Enter gender(M/F): ").lower()
        username = input("Enter username: ")
        a = 1
        while a ==1:
            global password1
            global password2
            password1 = pas.getpass(prompt="Enter password: ")
            password2 = pas.getpass(prompt="Renter password: ")
            if password1 == password2:
                key = fer.Fernet.generate_key()
                fernet = fer.Fernet(key)
                encrypted = fernet.encrypt(password1.encode())
                cur.execute("INSERT INTO users (f_name , l_name, username, gender, pass, secret) VALUES (%s, %s, %s, %s, %s, %s)", (f_name, l_name,username, gender, encrypted, key))
                b = db.commit()
                print("User created successfully")
                a = 0
            else:
                print("Wrong Password. Try again!")
                a = 1
            #if a ==5:
            
    create_user()            
        
        
"""
    def user_login():
        username = input("Enter username:")
        cur.execute("")
"""
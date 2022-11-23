# This program will be used to create new users and add them to the database
from cryptography import fernet as fer
import mysql.connector as con
import getpass as pas

def create_user():
    with con.connect(host="sanchitlogger-vm1.centralindia.cloudapp.azure.com",user="sanchitlogger",password="Password@1234",database="msms") as db:
        cur = db.cursor()
    
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
                      
        
def user_login():
     with con.connect(host="sanchitlogger-vm1.centralindia.cloudapp.azure.com",user="sanchitlogger",password="Password@1234",database="msms") as db:
        cur = db.cursor()
        username = input("Enter username:")
        a =cur.execute(f"select f_name from users where username = '{username}'")
        b = cur.fetchone()
        print(b)
user_login()
        

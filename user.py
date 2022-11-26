# This program will be used to create new users and add them to the database
from cryptography import fernet as fer
import mysql.connector as con
import getpass as pas

file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()


def create_user():
    # This function is used to create new user
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()

        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        gender = input("Enter gender(M/F): ").lower()
        username = input("Enter username: ")
        a = 1
        while a == 1:
            global password1
            global password2
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
            # if a ==5:


def user_login():
    # This function is used to log user in the system.
    with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        username = input("Enter username:")

        exe1 = cur.execute(f"select f_name,l_name,gender from users where username = '{username}'")
        b = cur.fetchone()
        
        if b == None:
            print("User not found")
        else:
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
            else:
                print("Login unsuccessful")    
user_login()


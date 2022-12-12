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
def list_users(a):
     with con.connect(host=f"{host}", user=f"{user}",
                     password=f"{passwd}", database=f"{dbs}") as db:
        cur = db.cursor()
        exe1 = cur.execute(f"select username,f_name,l_name,gender from users")
        b = cur.fetchmany(a)
        return b 
user_login()   
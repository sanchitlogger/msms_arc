import sys
from tkinter import *
from tkinter import ttk
import re
import mysql.connector as con
import PIL
from cryptography import fernet as fer

file = open("db.txt", "r")
host = file.readline().strip()
user = file.readline().strip()
passwd = file.readline().strip()
dbs = file.readline().strip()

db = con.connect(host=f"{host}", user=f"{user}", password=f"{passwd}", database=f"{dbs}")
cur = db.cursor()

root = Tk()
root.title("Medical shop management system")
root.geometry('500x350+350+200')
root.resizable(False, False)

def user_login(username, passin):

    username.lower()
    exe1 = cur.execute(f"select f_name,l_name,gender from users where username = '{username}'")
    b = cur.fetchone()
    if b == None:
        usr_alt1.set("User not found")

    else:
        # if b[2]=="m":
        #    print(f"Hello Mr {b[0].title()} {b[1].title()}.")
        # if b[2]=="f":
        #    print(f"Hello Mrs {b[0].title()} {b[1].title()}.")

        exe2 = cur.execute(f"select secret,pass from users where username = '{username}'")
        c = cur.fetchone()
        fernet2 = fer.Fernet(c[0])
        decrypted = fernet2.decrypt(c[1].encode())
        if decrypted.decode() != passin:
            ps_alt.set("* Wrong Password")
        if decrypted.decode() == passin:
            ui()

main1 = Frame(root, background="orange", width=500, height=350)
main1.place(x=0, y=0)
head = Label(main1, text="Medical Shop Magement System", font=("FreeSans", 18))
head.place(x=75, y=10)



login_frame = Frame(main1, bg="White", width=485, height=270)
login_frame.place(y=75, x=7)
#
usr_name = Label(login_frame, text="username:", )
usr_name.place(x=250, y=85)
usr_alt1 = StringVar()
usr_alt1_1 = Label(login_frame, textvariable=usr_alt1, font=("Bell MT", 8), background="white", fg="red")
usr_alt1_1.place(x=255, y=130)
#
usr_pass = Label(login_frame, text="password:", )
usr_pass.place(x=250, y=160)
ps_alt = StringVar()
ps_alt1_1=Label(login_frame, textvariable=ps_alt, font=("Bell MT", 8), background="white", fg="red")
ps_alt1_1.place(x=255, y=205)
#
us=StringVar()
usr = Entry(login_frame, width=25,textvariable=us, highlightbackground="black", highlightthickness=1, relief="flat")
usr.place(x=250, y=105)
pas = StringVar
ps = Entry(login_frame, show="*", textvariable=pas, width=25, highlightbackground="black", highlightthickness=1,
           relief="flat")
ps.place(x=250, y=180)
login_butt = Button(login_frame, text="Login", relief="flat", bg="#0dbd55", highlightbackground="black", cursor="hand2",
                    command=lambda: user_login(usr.get(), ps.get()))
login_butt.place(x=250, y=225)
def ui():
    main1.destroy()
    head.destroy()
    login_frame.destroy()
    usr_name.destroy()
    usr_pass.destroy()
    ps_alt1_1.destroy()
    usr_alt1_1.destroy()
    ps.destroy()
    usr.destroy()
    login_butt.destroy()

    
root.mainloop()


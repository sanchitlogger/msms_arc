from tkinter import *
from PIL import Image
from PIL.ImageTk import *

root=Tk()
root.resizable(False,False)
def home():
    root.geometry('800x600+300+90')
    root.title("MSMS - Home")
    
    head=Frame(root,width=800,height=215,highlightbackground="black",highlightthickness=3)
    usr=Frame(head,width=200,height=215,highlightbackground="blue",highlightthickness=2)
    today_info = Frame(head,width=200,height=215,highlightbackground="red",highlightthickness=2)
    body=Frame(root,width=800,height=500,highlightbackground="orange",highlightthickness=3)
    butt=Frame(body,width=550,height=400,highlightbackground="purple",highlightthickness=2)
    alert_box=Frame(body,width=290,height=400,bg="#f0a049")

    head.place(x=0,y=0)
    usr.place(x=0,y=0)
    today_info.place(x=600,y=0)
    body.place(x=0,y=215)
    butt.place(x=0,y=50)
    alert_box.place(x=550,y=50)
    l1 = Label(head,text="Medical Shop Management System")
    l2 = Label(alert_box,text="Alerts",foreground="green")
    admin_pic=Image.open("images/admin_img.png")
    l3=Label(usr,image=admin_pic)
    l3.place(x=0,y=0)


    b1 = Button(butt,text="Medicines",width=10,bg="#2fd07d")
    b1.place(x=60,y=100)
    b2= Button(butt,text="Sales",width=10,bg="#2fd07d")
    b2.place(x=250,y=100)
    b3 = Button(butt,text="Trades",width=10,bg="#2fd07d")
    b3.place(x=420,y=100)
    b4= Button(butt,text="Partners",width=10,bg="#2fd07d")
    b4.place(x=60,y=200)
    b5 = Button(butt,text="Customers",width=10,bg="#2fd07d")
    b5.place(x=250,y=200)
    b6 = Button(butt,text="Users",width=10,bg="#2fd07d")
    b6.place(x=420,y=200)


   
home()

root.mainloop()

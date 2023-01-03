import tkinter
from tkinter import messagebox
from tkinter import *
from admin_login import *
from userloginscr import *
import pymysql
t=tkinter.Tk()
t.geometry('500x500')
t.title('front page')
t.config(bg='red')
c=Canvas(t,height=450,width=450,bg='yellow')
c.place(x=25,y=25)
c1=Canvas(t,height=400,width=400,bg='green')
c1.place(x=50,y=50)
c2=Canvas(t,height=350,width=350,bg='hotpink')
c2.place(x=75,y=75)
a=Label(t,text='WELCOME ALL',font=40,bg='white',fg='blue')
a.place(x=185,y=85)
b=Label(t,text='TO',font=40,bg='white',fg='blue')
b.place(x=225,y=125)
c_label=Label(t,text='TEACHER FEEDBACK SYSTEM',font=40,bg='white',fg='blue')
c_label.place(x=130,y=165)
bt_admin=Button(t,text="admin login",font=20,bg="black",fg="white",command=adminlogin)
bt_admin.place(x=140,y=275)
bt_user=Button(t,text="user login",font=20,bg="black",fg="white",command=userlogin)
bt_user.place(x=280,y=275)
t.mainloop()
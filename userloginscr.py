import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from user_mainscr import *
from userinsert import *
from user_forgot import *
def userlogin():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('login to main screen')
    t.config(bg='grey')
    def logincheck():
        x=e1.get()
        y=f1.get()
        db=pymysql.connect(host="localhost",user="root",password="youtube",database="testdb")
        cur=db.cursor()
        sql="select count(*) from users where uname='%s' and upass='%s'"%(x,y)
        cur.execute(sql)
        data=cur.fetchone()
        w=int(data[0])
        if w==0:
            messagebox.showinfo('Status','Not found')
        else:
            usermainscr()
    def cleardata():
        e1.delete(0,100)
        f1.delete(0,100)
    c=Canvas(t,height=600,width=600,bg='black')
    c.place(x=50,y=50)
    a=Label(t,text='TEACHER FEEDBACK SYSTEM',font=40,bg='black',fg='white')
    a.place(x=70,y=70)
    c.create_oval(250,150,320,220,fill='sky blue')
    b=Label(c,text='WELCOME',font=40,bg='black',fg='white')
    b.place(x=243,y=230)
    d=Label(c,text='Sign In',font=30,bg='black',fg='white')
    d.place(x=258,y=250)
    e=Label(c,text='Name',font=20,bg='black',fg='grey')
    e.place(x=160,y=290)
    e1=Entry(c,width=20)
    e1.place(x=270,y=290)
    f=Label(t,text='Password',font=20,bg='black',fg='grey')
    f.place(x=210,y=370)
    f1=Entry(c,width=20,show='*')
    f1.place(x=270,y=320)
    g=Button(c,text='Login',fg='white',bg='blue',command=logincheck)
    g.place(x=150,y=360,height=20,width=70)
    h=Label(c,text='No account yet ?',font=20,bg='black',fg='grey')
    h.place(x=160,y=400)
    bt=Button(c,text='Create account',font=5,bg='green',fg='white',command=userinsert)
    bt.place(x=310,y=400,height=20,width=150)
    bt1=Button(c,text='forgot id & pass',fg='black',bg='yellow',command=userforgot)
    bt1.place(x=230,y=360,height=20)
    bt2=Button(c,text='Clear',fg='white',bg='blue')
    bt2.place(x=335,y=360,height=20,width=70)
    t.mainloop()  
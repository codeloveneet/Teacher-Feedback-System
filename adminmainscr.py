import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
from collegeinsert import *
from collegefind import *
from collegedelete import *
from collegeupdate import *
from departmentinsert import *
from departmentfind import *
from departmentdelete import *
from departmentupdate import *
from teacherinsert import *
from teacherfind import *
from teacherdelete import *
from teacherupdate import *
from studentreginsert import *
from studentregfind import *
from studentregdelete import *
from studentregupdate import *
from feedbackinsert import *
from feedbackfind import *
from feedbackdelete import *
from feedbackupdate import *
from escinsert import *
from escfind import *
from escdelete import *
from escupdate import *
from userinsert import *
from userdelete import *
from userfind import *
from userupdate import *
def adminmainscr():
    t=tkinter.Tk()
    t.geometry('900x900')
    t.title('main screen')
    t.config(bg='light yellow')
    def coins():
        collegeinsert()
    def cofind():
        collegefind()
    def codelete():
        collegedelete()
    def coupdate():
        collegeupdate()
    def depinsert():
        departmentinsert()
    def depfind():
        departmentfind()
    def depupdate():
        departmentupdate()
    def depdelete():
        departmentdelete()
    def teainsert():
        teacherinsert()
    def teafind():
        teacherfind()
    def teadelete():
        teacherdelete()
    def teaupdate():
        teacherupdate()
    def streginsert():
        studreginsert()
    def stregfind():
        stregfind()
    def stregdelete():
        studregdelete()
    def stregupdate():
        studregupdate()
    def feedinsert():
        feedbackinsert()
    def feedfind():
        feedbackfind()
    def feeddelete():
        feedbackdelete()
    def feedupdate():
        feedbackupdate()
    def esinsert():
        escalationinsert()
    def esfind():
        escalationfind()
    def esdelete():
        escalationdelete()
    def esupdate():
        escalationupdate()
    def usrinsert():
        userinsert()
    def usrdelete():
        userdelete()
    def usrfind():
        userfind()
    def usrupdate():
        userupdate()
        
    def collegecall():
        c1=Canvas(t,height=270,width=180,bg='light pink')
        c1.place(x=100,y=280)
        c1a=Button(c1,text='College Insert',font=30,command=coins)
        c1a.place(x=20,y=25)
        c1b=Button(c1,text='College Find',font=30,command=cofind)
        c1b.place(x=20,y=75)
        c1c=Button(c1,text='College Update',font=30,command=coupdate)
        c1c.place(x=20,y=125)
        c1d=Button(c1,text='College Delete',font=30,command=codelete)
        c1d.place(x=20,y=175)
        def exit():
               c1.destroy()
        c1e=Button(c1,text='Exit',font=30,command=exit)
        c1e.place(x=20,y=225)
    def depcall():
        c1=Canvas(t,height=270,width=180,bg='light pink')
        c1.place(x=300,y=280)
        c1a=Button(c1,text='Dep Insert',font=30,command=depinsert)
        c1a.place(x=20,y=25)
        c1b=Button(c1,text='Dep Find',font=30,command=depfind)
        c1b.place(x=20,y=75)
        c1c=Button(c1,text='Dep Update',font=30,command=depupdate)
        c1c.place(x=20,y=125)
        c1d=Button(c1,text='Dep Delete',font=30,command=depdelete)
        c1d.place(x=20,y=175)
        def exit():
               c1.destroy()
        c1e=Button(c1,text='Exit',font=30,command=exit)
        c1e.place(x=20,y=225)
    def teacall():
        c1=Canvas(t,height=270,width=180,bg='light pink')
        c1.place(x=500,y=280)
        c1a=Button(c1,text='Teacher Insert',font=30,command=teainsert)
        c1a.place(x=20,y=25)
        c1b=Button(c1,text='Teacher Find',font=30,command=teafind)
        c1b.place(x=20,y=75)
        c1c=Button(c1,text='Teacher Update',font=30,command=teaupdate)
        c1c.place(x=20,y=125)
        c1d=Button(c1,text='Teacher Delete',font=30,command=teadelete)
        c1d.place(x=20,y=175)
        def exit():
               c1.destroy()
        c1e=Button(c1,text='Exit',font=30,command=exit)
        c1e.place(x=20,y=225)
    def studregcall():
        c1=Canvas(t,height=270,width=200,bg='light pink')
        c1.place(x=75,y=480)
        c1a=Button(c1,text='Stud Reg Insert',font=30,command=streginsert)
        c1a.place(x=20,y=25)
        c1b=Button(c1,text='Stud Reg Find',font=30,command=stregfind)
        c1b.place(x=20,y=75)
        c1c=Button(c1,text='Stud Reg Update',font=30,command=stregupdate)
        c1c.place(x=20,y=125)
        c1d=Button(c1,text='Stud Reg Delete',font=30,command=stregdelete)
        c1d.place(x=20,y=175)
        def exit():
               c1.destroy()
        c1e=Button(c1,text='Exit',font=30,command=exit)
        c1e.place(x=20,y=225)
    def feedcall():
        c1=Canvas(t,height=270,width=200,bg='light pink')
        c1.place(x=290,y=470)
        c1a=Button(c1,text='Feedback Insert',font=30,command=feedinsert)
        c1a.place(x=20,y=25)
        c1b=Button(c1,text='Feedback Find',font=30,command=feedfind)
        c1b.place(x=20,y=75)
        c1c=Button(c1,text='Feedback Update',font=30,command=feedupdate)
        c1c.place(x=20,y=125)
        c1d=Button(c1,text='Feedback Delete',font=30,command=feeddelete)
        c1d.place(x=20,y=175)
        def exit():
               c1.destroy()
        c1e=Button(c1,text='Exit',font=30,command=exit)
        c1e.place(x=20,y=225)
    def esccall():
        c1=Canvas(t,height=270,width=200,bg='light pink')
        c1.place(x=480,y=470)
        c1a=Button(c1,text='Escalation Insert',font=30,command=esinsert)
        c1a.place(x=20,y=25)
        c1b=Button(c1,text='Escalation Find',font=30,command=esfind)
        c1b.place(x=20,y=75)
        c1c=Button(c1,text='Escalation Update',font=30,command=esupdate)
        c1c.place(x=20,y=125)
        c1d=Button(c1,text='Escalation Delete',font=30,command=esdelete)
        c1d.place(x=20,y=175)
        def exit():
               c1.destroy()
        c1e=Button(c1,text='Exit',font=30,command=exit)
        c1e.place(x=20,y=220)
    def usrcall():
         c1=Canvas(t,height=270,width=200,bg='light pink')
         c1.place(x=240,y=470)
         c1a=Button(c1,text='User Insert',font=30,command=usrinsert)
         c1a.place(x=20,y=25)
         c1b=Button(c1,text='User Find',font=30,command=usrfind)
         c1b.place(x=20,y=75)
         c1c=Button(c1,text='User Update',font=30,command=usrupdate)
         c1c.place(x=20,y=125)
         c1d=Button(c1,text='User Delete',font=30,command=usrdelete)
         c1d.place(x=20,y=175)
         def exit():
                c1.destroy()
         c1e=Button(c1,text='Exit',font=30,command=exit)
         c1e.place(x=20,y=225)
    c=Canvas(t,height=700,width=1400,bg='light green')
    c.place(x=0,y=100)
    a=Label(t,text='TEACHER    FEEDBACK   SYSTEM',font=40,bg='black',fg='white')
    a.place(x=350,y=50)
    co=Button(t,text='COLLEGE',font=40,bg='light blue',fg='black',command=collegecall)
    co.place(x=105,y=200)
    c.create_oval(60,50,240,170,fill='orange')
    dep=Button(t,text='DEPARTMENT',font=40,bg='light blue',fg='black',command=depcall)
    dep.place(x=305,y=200)
    c.create_oval(270,50,470,170,fill='skyblue')
    tea=Button(t,text='TEACHER',font=40,bg='light blue',fg='black',command=teacall)
    tea.place(x=550,y=200)
    c.create_oval(500,50,700,170,fill='pink')
    st=Button(t,text='STUDENT REG',font=40,bg='light blue',fg='black',command=studregcall)
    st.place(x=85,y=400)
    c.create_oval(60,250,240,370,fill='green')
    fed=Button(t,text='FEEDBACK',font=40,bg='light blue',fg='black',command=feedcall)
    fed.place(x=315,y=400)
    c.create_oval(270,250,470,370,fill='grey')
    esc=Button(t,text='ESCALATION',font=40,bg='light blue',fg='black',command=esccall)
    esc.place(x=540,y=400)
    c.create_oval(500,250,700,370,fill='red')
    usr=Button(t,text='USER',font=40,bg='light blue',fg='black',command=usrcall)
    usr.place(x=125,y=595)
    c.create_oval(70,450,240,570,fill='yellow')
    t.mainloop()
    
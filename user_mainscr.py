import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
from userupdate import *
from studentreginsert import *
from studentregfind import *
from studentregdelete import *
from studentregupdate import *
from feedbackinsert import *
from feedbackfind import *
from feedbackdelete import *
from feedbackupdate import *
def usermainscr():
    t=tkinter.Tk()
    t.geometry('800x700')
    t.title('main screen')
    t.config(bg='light yellow')
    
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
    def usupdate():
        userupdate()
    
    def studregcall():
        c1=Canvas(t,height=270,width=200,bg='light pink')
        c1.place(x=480,y=200)
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
        c1.place(x=470,y=400)
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
    def userupdatecall():
        c1=Canvas(t,height=90,width=175,bg='light pink')
        c1.place(x=480,y=560)
        c1a=Button(c1,text='User Update',font=30,command=usupdate)
        c1a.place(x=20,y=15)
        def exit():
               c1.destroy()
        c1b=Button(c1,text='Exit',font=30,command=exit)
        c1b.place(x=20,y=50)
        
    a=Label(t,text='TEACHER    FEEDBACK   SYSTEM',font=40,bg='black',fg='white')
    a.place(x=275,y=50)
    c=Canvas(t,height=700,width=1400,bg='light green')
    c.place(x=0,y=100)
    st=Button(t,text='STUDENT REG',font=40,bg='light blue',fg='black',command=studregcall)
    st.place(x=305,y=200)
    c.create_oval(270,50,470,170,fill='purple')
    fed=Button(t,text='FEEDBACK',font=40,bg='light blue',fg='black',command=feedcall)
    fed.place(x=315,y=400)
    c.create_oval(270,250,470,370,fill='hotpink')
    us=Button(t,text='USER',font=40,bg='light blue',fg='black',command=userupdatecall)
    us.place(x=340,y=600)
    c.create_oval(270,450,470,570,fill='green')
    
    t.mainloop()

  

    
    
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def adminforgot():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title('admin forgot')
    t.config(bg='light green')
    
    def searchdata():
        x=a1.get()
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select adminid,aname,apass from admin where aemail='%s'"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        if data==None:
            messagebox.showerror("Error",'Data Not Found')
        else:
            b1.delete(0,100)
            c1.delete(0,100)
            d1.delete(0,100)
       
            b1.insert(0,data[0])
            c1.insert(0,data[1])
            d1.insert(0,data[2])
       
    def clear():
        a1.delete(0,100)
        b1.delete(0,100)
        c1.delete(0,100)
        d1.delete(0,100)
        
    s=Label(t,text='FORGOT PASSWORD',font=40,fg='black',bg='red')
    s.place(x=210,y=50)
    a=Label(t,text='EMAIL',font=20,bg='green')
    a.place(x=75,y=125)
    a1=Entry(t,width=30)
    a1.place(x=300,y=125)
    b=Label(t,text='ID',font=20,bg='green')
    b.place(x=75,y=175)
    b1=Entry(t,width=30)
    b1.place(x=300,y=175)
    c=Label(t,text='NAME',font=20,bg='green')
    c.place(x=75,y=225)
    c1=Entry(t,width=30)
    c1.place(x=300,y=225)
    d=Label(t,text='PASS',font=20,bg='green')
    d.place(x=75,y=275)
    d1=Entry(t,width=30)
    d1.place(x=300,y=275)
    
    bt1=Button(t,text='SEARCH',bg='orange',command=searchdata)
    bt1.place(x=200,y=350,height=40,width=80)
    bt2=Button(t,text='CLEAR',bg='orange',command=clear)
    bt2.place(x=300,y=350,height=40,width=80)
    t.mainloop()



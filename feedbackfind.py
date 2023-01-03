import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def feedbackfind():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('FEEDBACK FIND')
    t.config(bg='light green')
    def fillids():
        x=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select studid from feedback"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def finddata():
        x=a1.get()
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select Teacherid,Majorsub,Rating,Dateoffeedback,Remark from feedback where studid='%s'"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        if data==None:
            messagebox.showerror("Error",'Data Not Found')
        else:
            b1.delete(0,100)
            c1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            f1.delete(0,100)
            b1.insert(0,data[0])
            c1.insert(0,data[1])
            d1.insert(0,data[2])
            e1.insert(0,data[3])
            f1.insert(0,data[4])
    def clear():
        a1.delete(0,100)
        b1.delete(0,100)
        c1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
    s=Label(t,text='FEEDBACK FIND',font=40,fg='black',bg='red')
    s.place(x=275,y=50)
    a=Label(t,text='Student Id',font=20,bg='green')
    a.place(x=75,y=125)
    a1=ttk.Combobox(t,width=37)
    a1.place(x=250,y=125)
    idlist=fillids()
    a1['values']=idlist
    b=Label(t,text='Teacher Id',font=20,bg='green')
    b.place(x=75,y=175)
    b1=Entry(t,width=40)
    b1.place(x=250,y=175)
    c=Label(t,text='Major Subject',font=20,bg='green')
    c.place(x=75,y=225)
    c1=Entry(t,width=40)
    c1.place(x=250,y=225)
    d=Label(t,text='Rating',font=20,bg='green')
    d.place(x=75,y=275)
    d1=Entry(t,width=40)
    d1.place(x=250,y=275)
    e=Label(t,text='Date of feedback',font=20,bg='green')
    e.place(x=75,y=325)
    e1=Entry(t,width=40)
    e1.place(x=250,y=325)
    f=Label(t,text='Remarks',font=20,bg='green')
    f.place(x=75,y=375)
    f1=Entry(t,width=40)
    f1.place(x=250,y=375)
    bt1=Button(t,text='FIND',bg='orange',command=finddata)
    bt1.place(x=250,y=450,width=80,height=40)
    bt2=Button(t,text='CLEAR',bg='orange',command=clear)
    bt2.place(x=350,y=450,width=80,height=40)
    t.mainloop()
    
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def departmentinsert():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('DEPARTMENT INSERT')
    t.config(bg='light green')
    
    def savedata():
        x=a1.get() #depid
        y=b1.get() #name
        z=c1.get() #description
        p=d1.get()
        if(len(x)==0 or len(y)==0 or len(z)==0 or len(p)==0):
            messagebox.showerror('Error','Error:Empty fields')
        elif(x.isdigit() or y.isdigit() or z.isdigit() or p.isdigit()):
            messagebox.showerror("Error","Error:Invalid entry")
        
        else:
            db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
            cur=db.cursor()
            sql="insert into department values('%s','%s','%s','%s')"%(x,y,z,p)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo("Saved","Data Saved")
            a1.delete(0,100)
            b1.delete(0,100)
            c1.delete(0,100)
            d1.delete(0,100)
    def clear():
        a1.delete(0,100)
        b1.delete(0,100)
        c1.delete(0,100)
        d1.delete(0,100)
    def checkdata():
        x=a1.get() 
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select count(*) from department where depid='%s'"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        if int(data[0])==0:
            lblstatus.config(text='Record Not Present',fg='green')
        else:
            lblstatus.config(text='Record ALREADY Present',fg='red')
    s=Label(t,text='DEPARTMENT INSERT',bg='red',fg='black',font=50)
    s.place(x=230,y=50)
    a=Label(t,text="Department ID",bg='green',font=30)
    a.place(x=100,y=150)
    a1=Entry(t,width=30)
    a1.place(x=300,y=150)
    btfind=Button(t,text='Check Data',command=checkdata,bg='orange')
    btfind.place(x=500,y=145)
    lblstatus=Label(t,text='Status',fg='red')
    lblstatus.place(x=600,y=145)
    b=Label(t,text="Department name",bg='green',font=30)
    b.place(x=100,y=210)
    b1=Entry(t,width=30)
    b1.place(x=300,y=210)
    c=Label(t,text="Description",bg='green',font=30)
    c.place(x=100,y=280)
    c1=Entry(t,width=30)
    c1.place(x=300,y=280)
    d=Label(t,text="HOD",bg='green',font=30)
    d.place(x=100,y=340)
    d1=Entry(t,width=30)
    d1.place(x=300,y=340)
    bt1=Button(t,text='SAVE',bg='orange',command=savedata)
    bt1.place(x=200,y=470,height=40,width=80)
    bt2=Button(t,text='CLEAR',bg='orange',command=clear)
    bt2.place(x=350,y=470,height=40,width=80)
    t.mainloop()
    
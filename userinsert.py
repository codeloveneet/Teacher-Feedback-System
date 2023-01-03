import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import pymysql
def userinsert():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('USER INSERT')
    t.config(bg='light green')
    def check(p):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(pat,p):
            pass
            x=a1.get() 
            y=b1.get() 
            z=c1.get() 
            p=d1.get() 
            q=e1.get()
            r=f1.get()
            s=g1.get()
            db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
            cur=db.cursor()
            sql="insert into users values('%s','%s','%s','%s','%s','%s','%s')"%(x,y,z,p,q,r,s)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo("Saved","Data Saved")
            a1.delete(0,100)
            b1.delete(0,100)
            c1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            f1.delete(0,100)
            g1.delete(0,100)
        else:
            messagebox.showerror("error","Invalid Email")
            
    def savedata():
        x=a1.get() 
        y=b1.get() 
        z=c1.get() 
        p=d1.get() 
        q=e1.get()
        r=f1.get()
        s=g1.get()
        if(len(x)==0 or len(y)==0 or len(z)==0 or len(p)==0 or len(q)==0 or len(r)==0 or len(s)==0):
            messagebox.showerror('Error','Error: First Fill Empty fields!')
        elif(x.isdigit() or x.isalpha() or y.isdigit() or z.isdigit() or p.isdigit() or q.isdigit()):
            messagebox.showerror("Error","Error:Invalid entry")
        elif x.startswith('-') or y.startswith('-') or p.startswith('-') or q.startswith('-'):
            messagebox.showerror("Error",'Error: Entered negatives values')
        elif len(s)!=10:
            messagebox.showerror('Error','Error:Invalid phoneno')
        elif s.isdigit():
            check(p)
            
        else:
             messagebox.showerror('Error','Error:Invalid phoneno')
    def clear():
        a1.delete(0,100)
        b1.delete(0,100)
        c1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
    def checkdata():
        x=a1.get() 
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select count(*) from users where userid='%s'"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        if int(data[0])==0:
            lblstatus.config(text='Available',bg='green')
        else:
            lblstatus.config(text='Not available',bg='red')
    
    def checkemaildata():
            x=d1.get() 
            db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
            cur=db.cursor()
            sql="select count(*) from users where userid='%s'"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            if int(data[0])==0:
                lblstatus1.config(text='Available',bg='green')
            else:
                lblstatus1.config(text='Not available',bg='red')
            
    s=Label(t,text='USER INSERT',font=40,fg='black',bg='red')
    s.place(x=250,y=50)
    a=Label(t,text='User id',font=20,bg='light blue')
    a.place(x=75,y=125)
    a1=Entry(t,width=40)
    a1.place(x=250,y=125)
    btfind=Button(t,text='Check Data',command=checkdata,bg='orange')
    btfind.place(x=500,y=125)
    lblstatus=Label(t,text='Status',fg='black')
    lblstatus.place(x=590,y=125)
    b=Label(t,text='User name',font=20,bg='light blue')
    b.place(x=75,y=175)
    b1=Entry(t,width=40)
    b1.place(x=250,y=175)
    c=Label(t,text='User password',font=20,bg='light blue')
    c.place(x=75,y=225)
    c1=Entry(t,width=40,show='*')
    c1.place(x=250,y=225)
    d=Label(t,text='User E-mail',font=20,bg='light blue')
    d.place(x=75,y=275)
    d1=Entry(t,width=40)
    d1.place(x=250,y=275)
    btfind1=Button(t,text='Check',bg='orange',command=checkemaildata)
    btfind1.place(x=500,y=275)
    lblstatus1=Label(t,text='Status',fg='black')
    lblstatus1.place(x=590,y=275)
    e=Label(t,text='Address',font=20,bg='light blue')
    e.place(x=75,y=325)
    e1=Entry(t,width=40)
    e1.place(x=250,y=325)
    f=Label(t,text='City',font=20,bg='light blue')
    f.place(x=75,y=375)
    f1=Entry(t,width=40)
    f1.place(x=250,y=375)
    g=Label(t,text='Phone',font=20,bg='light blue')
    g.place(x=75,y=425)
    g1=Entry(t,width=40)
    g1.place(x=250,y=425)
    bt1=Button(t,text='SAVE',bg='orange',command=savedata)
    bt1.place(x=250,y=500,height=40,width=80)
    bt2=Button(t,text='CLEAR',bg='orange',command=clear)
    bt2.place(x=350,y=500,height=40,width=80)
    t.mainloop()   


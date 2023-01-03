import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import pymysql
def admininsert():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('ADMIN INSERT')
    t.config(bg='light green')
    
    def savedata():
        x=a1.get() 
        y=b1.get() 
        z=c1.get() 
        p=d1.get() 
       
        if(len(x)==0 or len(y)==0 or len(z)==0 or len(p)==0):
            messagebox.showerror('Error','Error: First Fill Empty fields!')
        elif(x.isdigit() or x.isalpha() or y.isdigit() or z.isdigit() or p.isdigit()):
            messagebox.showerror("Error","Error:Invalid entry")
        elif x.startswith('-') or y.startswith('-') or p.startswith('-'):
            messagebox.showerror("Error",'Error: Entered negatives values')
        else:
            email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.match(email,p):
                pass
                x=a1.get() 
                y=b1.get() 
                z=c1.get() 
                p=d1.get() 
                db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
                cur=db.cursor()
                sql="insert into admin values('%s','%s','%s','%s')"%(x,y,z,p)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo("Saved","Data Saved")
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
             
            else:
                messagebox.showerror("error","Invalid Email")
            
    def clear():
        a1.delete(0,100)
        b1.delete(0,100)
        c1.delete(0,100)
        d1.delete(0,100)
    
    def checkdata():
        x=a1.get() 
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select count(*) from admin where adminid='%s'"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        if int(data[0])==0:
            lblstatus.config(text='Available',fg='green')
        else:
            lblstatus.config(text='Not Available',fg='red')
    s=Label(t,text='ADMIN INSERT',font=40,fg='black',bg='red')
    s.place(x=280,y=50)
    a=Label(t,text='Admin id',font=20,bg='light blue')
    a.place(x=75,y=125)
    a1=Entry(t,width=40)
    a1.place(x=250,y=125)
    btfind=Button(t,text='Check Data',command=checkdata,bg='orange')
    btfind.place(x=500,y=125)
    lblstatus=Label(t,text='Status',fg='red')
    lblstatus.place(x=590,y=125)
    b=Label(t,text='Admin name',font=20,bg='light blue')
    b.place(x=75,y=175)
    b1=Entry(t,width=40)
    b1.place(x=250,y=175)
    c=Label(t,text='Admin password',font=20,bg='light blue')
    c.place(x=75,y=225)
    c1=Entry(t,width=40,show='*')
    c1.place(x=250,y=225)
    d=Label(t,text='E-mail',font=20,bg='light blue')
    d.place(x=75,y=275)
    d1=Entry(t,width=40)
    d1.place(x=250,y=275)
    bt1=Button(t,text='SAVE',bg='orange',command=savedata)
    bt1.place(x=250,y=400,height=40,width=80)
    bt2=Button(t,text='CLEAR',bg='orange',command=clear)
    bt2.place(x=350,y=400,height=40,width=80)
    t.mainloop() 

          

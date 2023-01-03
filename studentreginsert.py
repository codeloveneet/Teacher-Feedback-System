import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def studentregisterinsert():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('STUDENT REGISTER INSERT')
    t.config(bg='light green')
    def fillids():
        x=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select depid from studentregister"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def savedata():
        x=a1.get() 
        y=b1.get() 
        z=c1.get() 
        p=d1.get() 
        q=e1.get()
        r=f1.get()
        if(len(x)==0 or len(y)==0 or len(z)==0 or len(p)==0 or len(q)==0 or len(r)==0):
               messagebox.showerror('Error','Empty fields')
        elif(r.count('@')==0 or r.count('.')==0 and r[0]!='@' and r[0]!='.'):
             messagebox.showerror("Error","Enter Valid Email")
        elif(x.isalpha() or y.isdigit() or z.isdigit() or p.isdigit() or q.isdigit()):
            messagebox.showerror("Error","Error:Invalid entry")
        
        else:
            db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
            cur=db.cursor()
            sql="insert into studentregister values('%s','%s','%s','%s','%s','%s')"%(x,y,z,p,q,r)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo("Saved","Data Saved")
            a1.delete(0,100)
            b1.delete(0,100)
            c1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            f1.delete(0,100)
    def clear():
        a1.delete(0,100)
        b1.delete(0,100)
        c1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
    def checkdata():
        x=a1.get() 
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select count(*) from studentregister where studid='%s'"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        if int(data[0])==0:
            lblstatus.config(text='Record Not Present',fg='red')
        else:
            lblstatus.config(text='Record ALREADY Present',fg='green')
    s=Label(t,text='STUDENT REGISTER INSERT ',font=40,fg='black',bg='red')
    s.place(x=150,y=50)
    a=Label(t,text='Student id',font=20,bg='green')
    a.place(x=75,y=125)
    a1=Entry(t,width=30)
    a1.place(x=250,y=125)
    btfind=Button(t,text='Check Data',command=checkdata,bg='orange')
    btfind.place(x=500,y=125)
    lblstatus=Label(t,text='Status',fg='red')
    lblstatus.place(x=600,y=125)
    b=Label(t,text='Student name',font=20,bg='green')
    b.place(x=75,y=175)
    b1=Entry(t,width=30)
    b1.place(x=250,y=175)
    c=Label(t,text='Depid',font=20,bg='green')
    c.place(x=75,y=225)
    c1=ttk.Combobox(t,width=27)
    c1.place(x=250,y=225)
    idlist=fillids()
    c1['values']=idlist
    d=Label(t,text='Address',font=20,bg='green')
    d.place(x=75,y=275)
    d1=Entry(t,width=30)
    d1.place(x=250,y=275)
    e=Label(t,text='City',font=20,bg='green')
    e.place(x=75,y=325)
    e1=Entry(t,width=30)
    e1.place(x=250,y=325)
    f=Label(t,text='Email',font=20,bg='green')
    f.place(x=75,y=375)
    f1=Entry(t,width=30)
    f1.place(x=250,y=375)
    bt1=Button(t,text='SAVE',bg='orange',command=savedata)
    bt1.place(x=250,y=450,height=40,width=80)
    bt2=Button(t,text='CLEAR',bg='orange2',command=clear)
    bt2.place(x=350,y=450,height=40,width=80)
    t.mainloop()
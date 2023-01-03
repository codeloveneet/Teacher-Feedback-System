import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def teacherupdate():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('TEACHER UPDATE')
    t.config(bg='light green')
    def check(q):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(pat,q):
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
            sql="update teacher set teachername='%s',address='%s',city='%s',email='%s',depid='%s',majorsub='%s' where teacherid='%s'"%(y,z,p,q,r,s,x)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo("Saved","Data Updated")
            a1.delete(0,100)
            b1.delete(0,100)
            c1.delete(0,100)
            d1.delete(0,100) 
            e1.delete(0,100)
            f1.delete(0,100)
            g1.delete(0,100)
        else:
            messagebox.showerror("error","Invalid Email")
    def filldep():
        x=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select depid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def fillmaj():
        x=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select majorsub from teacher"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def fillids():
        x=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select teacherid from teacher"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def finddata():
        x=a1.get()
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select teachername,address,city,email,depid,majorsub from teacher where teacherid='%s'"%(x)
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
            g1.delete(0,100)
            b1.insert(0,data[0])
            c1.insert(0,data[1])
            d1.insert(0,data[2])
            e1.insert(0,data[3])
            f1.insert(0,data[4])
            g1.insert(0,data[5])
    def updatedata():
        x=a1.get()
        y=b1.get() 
        z=c1.get() 
        p=d1.get() 
        q=e1.get()
        r=f1.get()
        s=g1.get()
        if(len(x)==0 or len(y)==0 or len(z)==0 or len(p)==0 or len(q)==0 or len(r)==0 or len(s)==0):
           messagebox.showerror('Error','Error:Empty fields')
        elif(q.count('@')==0 or q.count('.')==0 and q[0]!='@' and q[0]!='.'):
           messagebox.showerror("Error","Error:Enter Valid Email")
        elif(x.isdigit() or y.isdigit() or z.isdigit() or p.isdigit() or r.isdigit()):
           messagebox.showerror("Error","Error:Invalid entry")
        else:
            check(q)
        
    def clear():
        a1.delete(0,100)
        b1.delete(0,100)
        c1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
        
    def checkemaildata():
            x=d1.get() 
            db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
            cur=db.cursor()
            sql="select count(*) from teacher where teacherid='%s'"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            if int(data[0])==0:
                lblstatus.config(text='Available',bg='green')
            else:
                lblstatus.config(text='Not available',bg='red')
    s=Label(t,text='TEACHERS UPDATE',font=40,fg='black',bg='red')
    s.place(x=200,y=50)
    a=Label(t,text='Teacher id',font=20,bg='green')
    a.place(x=75,y=125)
    a1=ttk.Combobox(t,width=27)
    a1.place(x=250,y=125)
    idlist=fillids()
    a1['values']=idlist
    b=Label(t,text='Teacher name',font=20,bg='green')
    b.place(x=75,y=175)
    b1=Entry(t,width=30)
    b1.place(x=250,y=175)
    c=Label(t,text='Address',font=20,bg='green')
    c.place(x=75,y=225)
    c1=Entry(t,width=30)
    c1.place(x=250,y=225)
    d=Label(t,text='City',font=20,bg='green')
    d.place(x=75,y=275)
    d1=Entry(t,width=30)
    d1.place(x=250,y=275)
    e=Label(t,text='Email',font=20,bg='green')
    e.place(x=75,y=325)
    e1=Entry(t,width=30)
    e1.place(x=250,y=325)
    btfind=Button(t,text='Check Data',command=checkemaildata,bg='orange')
    btfind.place(x=450,y=325)
    lblstatus=Label(t,text='Status',fg='black')
    lblstatus.place(x=550,y=325)
    f=Label(t,text='Depid',font=20,bg='green')
    f.place(x=75,y=375)
    f1=ttk.Combobox(t,width=27)
    f1.place(x=250,y=375)
    idlist1=filldep()
    f1['values']=idlist1
    g=Label(t,text='Major sub',font=20,bg='green')
    g.place(x=75,y=425)
    g1=ttk.Combobox(t,width=27)
    g1.place(x=250,y=425)
    idlist2=fillmaj()
    g1['values']=idlist2
    bt1=Button(t,text='FIND',bg='orange',command=finddata)
    bt1.place(x=150,y=500,height=40,width=80)
    bt2=Button(t,text='UPDATE',bg='orange',command=updatedata)
    bt2.place(x=250,y=500,height=40,width=80)
    bt3=Button(t,text='CLEAR',bg='orange',command=clear)
    bt3.place(x=350,y=500,height=40,width=80)
    t.mainloop()
import tkinter
from tkinter import *
from tkinter import messagebox
import time
import pymysql
from tkinter import ttk
def feedbackinsert():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('FEEDBACK INSERT')
    t.config(bg='light green')
    def dof():
        at=time.asctime()
        e1.insert(0,str(at))
    def fillids():
        x=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select studid from studentregister"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def fillids1():
        y=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select teacherid from teacher"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            y.append(res[0])
        return y
    def fillids2():
        z=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select majorsub from teacher"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            z.append(res[0])
        return z
    def matchdata():
        x1=b1.get()
        y1=c1.get()
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select count(*) from teacher where teacherid='%s' and majorsub ='%s'"%(x1,y1)
        cur.execute(sql)
        data=cur.fetchone()
        w=int(data[0])
        if w==0:
            messagebox.showerror("error","teacher id and major sub not matched")
        else: 
            x=a1.get() 
            y=b1.get() 
            z=c1.get() 
            p=d1.get() 
            q=e1.get()
            r=f1.get()
            db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
            cur=db.cursor()
            sql="insert into feedback values('%s','%s','%s','%s','%s','%s')"%(x,y,z,p,q,r)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo("Saved","Data Saved")
            a1.delete(0,100)
            b1.delete(0,100)
            c1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            f1.delete(0,100)
    def savedata():
        x=a1.get() 
        y=b1.get() 
        z=c1.get() 
        p=d1.get() 
        q=e1.get()
        r=f1.get()
        x1=b1.get()
        y1=c1.get()
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select count(*) from studentregister where studid='%s'"%x
        cur.execute(sql)
        data=cur.fetchone()
        w=int(data[0])
        if w!=0:
            if len(x)==0 or len(y)==0 or len(z)==0 or len(p)==0 or len(q)==0 or len(r)==0:
                messagebox.showerror("error","incomplete data")
            elif(x.isdigit() or y.isdigit() or z.isdigit() or p.isalpha() or q.isdigit() or r.isdigit()):
                 messagebox.showerror("Error","Error:Invalid entry")
            elif int(p)<=0 and int(p)>=5:
                     messagebox.showerror("Error","invalid rating")
            else:
                 matchdata()
        else:
            messagebox.showerror("error",'student not registered with this id') 
     
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
          sql="select count(*) from feedback where studid='%s'"%(x)
          cur.execute(sql)
          data=cur.fetchone()
          if int(data[0])==0:
              lblstatus.config(text='Record Not Present',fg='red')
          else:
              lblstatus.config(text='Record ALREADY Present',fg='green')
  
    
    s=Label(t,text='FEEDBACK INSERT',font=40,fg='black',bg='red')
    s.place(x=275,y=50)
    a=Label(t,text='Student Id',font=20,bg='green')
    a.place(x=75,y=125)
    a1=ttk.Combobox(t,width=37)
    a1.place(x=250,y=125)
    idlist=fillids()
    a1['values']=idlist
    b=Label(t,text='Teacher Id',font=20,bg='green')
    b.place(x=75,y=175)
    b1=ttk.Combobox(t,width=37)
    b1.place(x=250,y=175)
    idlist=fillids1()
    b1['values']=idlist
    c=Label(t,text='Major Subject',font=20,bg='green')
    c.place(x=75,y=225)
    c1=ttk.Combobox(t,width=37)
    c1.place(x=250,y=225)
    idlist=fillids2()
    c1['values']=idlist
    d=Label(t,text='Rating',font=20,bg='green')
    d.place(x=75,y=275)
    d1=ttk.Combobox(t,width=37)
    d1.place(x=250,y=275)
    d1['values'] = (1,2,3,4,5) 
    e=Label(t,text='Date of feedback',font=20,bg='green')
    e.place(x=75,y=325)
    e1=Entry(t,width=40)
    e1.place(x=250,y=325)
    bt=Button(t,text='Calendar',bg='orange',command=dof)
    bt.place(x=525,y=325,height=30,width=80)
    f=Label(t,text='Remarks',font=20,bg='green')
    f.place(x=75,y=375)
    f1=Entry(t,width=40)
    f1.place(x=250,y=375)
    bt1=Button(t,text='SAVE',bg='orange',command=savedata)
    bt1.place(x=250,y=450,width=80,height=40)
    bt2=Button(t,text='CLEAR',bg='orange',command=clear)
    bt2.place(x=350,y=450,width=80,height=40)
    t.mainloop()


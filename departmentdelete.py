import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def departmentdelete():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('DEPARTMENT DELETE')
    t.config(bg='light green')
    def fillids():
        x=[]
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select depid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
        return x
    def finddata():
        x=a1.get()
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select depname,description,hod from department where depid='%s'"%(x)
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
    def deletedata():
        x=a1.get()
        db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
        cur=db.cursor()
        sql="select teacherid from teacher where depid='%s'"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        w=data[0]
        if w==0:
             db=pymysql.connect(host='localhost',user='root',password='youtube',database='testdb')
             cur=db.cursor()
             sql="delete from department where depid='%s'"%(x)
             cur.execute(sql)
             a1.delete(0,100)
             db.commit()
             db.close()
             messagebox.showinfo("Deleted","Record Deleted..")   
        else:
            messagebox.showerror("error",'Teacher exist in this department')
    def clear():
        a1.delete(0,100)
        b1.delete(0,100)
        c1.delete(0,100)
        d1.delete(0,100)
    
    s=Label(t,text='DEPARTMENT DELETE',bg='red',fg='black',font=50)
    s.place(x=230,y=50)
    a=Label(t,text="Department ID",bg='green',font=30)
    a.place(x=100,y=150)
    a1=ttk.Combobox(t,width=27)
    a1.place(x=300,y=150)
    idlist=fillids()
    a1['values']=idlist
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
    bt=Button(t,text='FIND',bg='orange',command=finddata)
    bt.place(x=200,y=470,height=40,width=80)
    bt1=Button(t,text='DELETE',bg='orange',command=deletedata)
    bt1.place(x=300,y=470,height=40,width=80)
    bt2=Button(t,text='CLEAR',bg='orange',command=clear)
    bt2.place(x=400,y=470,height=40,width=80)
    t.mainloop()
   
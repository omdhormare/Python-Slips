from tkinter import *
import datetime
window=Tk()
window.geometry("500x500")

def cal():
    today=datetime.date.today()
    d=int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    
    dd=today.day-d
    mm=today.month-m
    yy=today.year-y
    
    a1.insert(0,dd)
    b1.insert(0,mm)
    c1.insert(0,yy)
    
    

l1=Label(window,text="Enter Your Birthdate Day : ")
l1.pack()

e1=Entry(window,width=20)
e1.pack()

l2=Label(window,text="Enter Your Birthdate Month : ")
l2.pack()

e2=Entry(window,width=20)
e2.pack()

l3=Label(window,text="Enter Your Birthdate Year : ")
l3.pack()

e3=Entry(window,width=20)
e3.pack()

b=Button(window,text="Calculate Your Age ",command=cal)
b.pack()

l4=Label(window,text="Calculate Year ",font=("bold",10))
l4.pack()

a=Label(window,text="calculate Day : ",font=("bold",10))
a.pack()
a1=Entry(window,width=20,font=("bold",10))
a1.pack()

b=Label(window,text="calculate Month : ",font=("bold",10))
b.pack()
b1=Entry(window,width=20,font=("bold",10))
b1.pack()

c=Label(window,text="calculate Year : ",font=("bold",10))
c.pack()
c1=Entry(window,width=20,font=("bold",10))
c1.pack()
window.mainloop()
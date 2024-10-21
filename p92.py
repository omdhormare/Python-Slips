'''B) Write Python GUI program to accept a number n and check whether it is Prime, 
Perfect or Armstrong number or not. Specify three radio buttons.'''
from tkinter import *
window=Tk()
window.geometry("500x500")

def armstrong():
    n=int(t1.get())
    n1=n
    sum=0
    while n>0:
        d=n%10
        sum=sum+d*d*d
        n=n//10
        t3.delete(0,END)
    if sum==n1:
        t3.insert(0,"Armstrong Number..")
    else:
        t3.insert(0,"Not Armstrong No...")

def perfect():
    n=int(t1.get())
    sum=0
    t3.delete(0,END)
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        t3.insert(0,"Prime Number ...")
    else:
        t3.insert(0,"Not prime No ...")

def prime():
    n=int(t1.get())
    sum=0
    t3.delete(0,END)
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+1
    if sum==2:
        t3.insert(0,"Prime Number..")
    else:
        t3.insert(0,"Not Prime Number...")

l1=Label(window,text="Enter Number : ",font=("arial",20))
l1.pack()
t1=Entry(window,width=20,font=("arial",20))
t1.pack()
r1=Radiobutton(window,text="Armstron No ",value=1,font=("arial",10),command=armstrong)
r1.pack()
r2=Radiobutton(window,text="perfect No ",value=2,font=("arial",10),command=perfect)
r2.pack()
r3=Radiobutton(window,text="prime No ",value=3,font=("arial",10),command=prime)
r3.pack()
l2=Label(window,text="Result : ",font=("arial",20))
l2.pack()

t3=Entry(window,width=20)
t3.pack()
window.mainloop()
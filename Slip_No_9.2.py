'''B) Write Python GUI program to accept a number n and check whether it is Prime, 
Perfect or Armstrong number or not. Specify three radio buttons. 
'''
from tkinter import *
window=Tk()
window.geometry("500x500")

def prime():
    n=int(e1.get())
    sum=0
    e2.delete(0,END)
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+1
    if sum==2:
        e2.insert(0,"prime No..")
    else:
        e2.insert(0,"Not Prime No..")

def arm():
    n=int(e1.get())
    n1=n
    sum=0
    e2.delete(0,END)
    while n>0:
        d=n%10
        sum=sum+d*d*d
        n=n//10
    if sum==n1:
        e2.insert(0,"Armstrong No ..")
    else:
        e2.insert(0,"Not Armstrong No ..")
        
def perfect_no():
    n=int(e1.get())
    sum=0
    e2.delete(0,END)
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        e2.insert(0,"Perfect Number ..")
    else:
        e2.insert(0,"Not Perfect Number ..")
        
        
l1=Label(window,text="Enter Number : ",font=("arial",15))
l1.pack()
e1=Entry(window,width="20")
e1.pack()

r1=Radiobutton(window,text="Prime Number ",value=1,command=prime)
r1.pack()

r2=Radiobutton(window,text="Armstrong Number ",value=2,command=arm)
r2.pack()

r3=Radiobutton(window,text="Perfect Number ",value=3,command=perfect_no)
r3.pack()

l1=Label(window,text="Result : ")
l1.pack()
e2=Entry(window,width="40")
e2.pack()

window.mainloop()
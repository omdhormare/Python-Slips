from tkinter import *
window=Tk()
window.geometry("500x500")

def armstrong():
    n=int(e1.get())
    sum=0
    n1=n
    e2.delete(0,END)
    while(n>0):
        d=n%10
        sum=sum+d*d*d
        n=n//10
    if n1==sum:
        e2.insert(0,"Armstrong Number...")
    else:
        e2.insert(0,"Not Armstrong Number..")
    
def prime():
    cnt=0
    n=int(e1.get())
    e2.delete(0,END)
    for i in range(1,n+1):
        if n%i==0:
            cnt=cnt+1
    if cnt==2:
        e2.insert(0,"Prime Number..")
    else:
        e2.insert(0,"Not Prime Number")

def perfect():
    e2.delete(0,END)
    sum=0
    n=int(e1.get())
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
       e2.insert(0,"perfect No..")
    else:
        e2.insert(0,"Not perfect No..")
    
l1=Label(window,text="Enter Number : ")
l1.pack()
e1=Entry(window,width=20)
e1.pack()

r1=Radiobutton(window,text="Armstrong Number ",value=1,command=armstrong)
r1.pack()

r2=Radiobutton(window,text="prime Number ",value=2,command=prime)
r2.pack()

r3=Radiobutton(window,text="Perfect Number ",value=3,command=perfect)
r3.pack()

e2=Entry(window,width=40)
e2.pack()
window.mainloop()

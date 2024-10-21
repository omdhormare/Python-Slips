'''A) Write a Python GUI program to accept dimensions of a cylinder and display the 
surface area and volume of cylinder. '''
from tkinter import *
window=Tk()
window.geometry("500x500")

def add():
    a=int(e1.get())
    b=int(e2.get())
    e3.delete(0,END)
    e3.insert(0,a+b)
    
l1=Label(window,text="Enter 1 Number : ")
l1.pack()

e1=Entry(window,width=20)
e1.pack()

l2=Label(window,text="Enter 2 Number : ")
l2.pack()

e2=Entry(window,width=20)
e2.pack()

l3=Label(window,text="Addtion : ")
l3.pack()

e3=Entry(window,width=20)
e3.pack()

b=Button(window,text="Addtion",width=10,command=add)
b.pack()
window.mainloop()


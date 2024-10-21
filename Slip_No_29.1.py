'''A) Write a Python GUI program to calculate volume of Sphere by accepting radius as input'''
from tkinter import *
window=Tk()

def volume():
    r=float(e1.get())
    #r=float(r)
    v=(4/3)*3.14*(r**3)
    e2.delete(0,END)
    e2.insert(0,v)
    
window.geometry("500x500")
l1=Label(window,text="Enter Radius : ")
l1.pack()
e1=Entry(window,width="30")
e1.pack()
l2=Label(window,text="Volume of Sphere : ")
l2.pack()
e2=Entry(window,width="30")
e2.pack()
b=Button(window,text="Calculate",width="10",command=volume)
b.pack()
window.mainloop()
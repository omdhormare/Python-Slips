'''A) Write a Python GUI program to accept dimensions of a cylinder and display the 
surface area and volume of cylinder. '''
from tkinter import *
window=Tk()
window.geometry("1000x1000")

def calculate():
    r = float(e1.get())
    h = float(e2.get())
    surface_area = 2 * 3.14 * r * (r + h)
    volume = 3.14 * r**2 * h
    e3.delete(0, END)
    e3.insert(0, surface_area)
    e4.delete(0, END)
    e4.insert(0, volume)


l1=Label(window,text="Enter Radius : ")
l1.pack()
e1=Entry(window,width="20")
e1.pack()

l2=Label(window,text="Enter Height : ")
l2.pack()
e2=Entry(window,width="20")
e2.pack()

l3=Label(window,text="Surface Area of : ")
l3.pack()
e3=Entry(window,width="20")
e3.pack()

l4=Label(window,text="Volume of Cylinder: ")
l4.pack()
e4=Entry(window,width="20")
e4.pack(pady="20")

b1=Button(window,text="Calculate",width="20",command=calculate)
b1.pack()
window.mainloop()
'''A) Write a Python GUI program to accept a string and a character from user and count 
the occurrences of a character in a string'''
from tkinter import *
window=Tk()

def check_char():
    s1=e1.get()
    s2=e2.get()
    s3=s1.count(s2)
    e3.delete(0,END)
    e3.insert(0,s3)

window.geometry("500x500")
l1=Label(window,text="Enter String : ")
e1=Entry(window,width="30")
l1.pack()
e1.pack()

l2=Label(window,text="Enter char To count: ")
e2=Entry(window,width="30")
l2.pack()
e2.pack()

l3=Label(window,text="Count Character : ")
e3=Entry(window,width="30")
l3.pack()
e3.pack()

b=Button(window,text="Check",width="10",command=check_char)
b.pack()
window.mainloop()
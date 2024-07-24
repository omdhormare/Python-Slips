#B) Write python GUI program to generate a random password with upper and lower case letters. 
from tkinter import *
import random
window=Tk()
window.geometry("1000x1000")

def password():
    p="ZXCVBNMASDFGHJKLQWERTYUIOPzxcvbnmasdfghjklqwertyuiop"
    l=8
    pas=''.join(random.sample(p,l))
    E.delete(0,END)
    E.insert(0,pas)

l=Label(window,text="Generate password : ")
l.pack()
E=Entry(window,width=30)
E.pack()
b=Button(window,text="Generate Password",command=password)
b.pack()
window.mainloop()
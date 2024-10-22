from tkinter import *
import random
window=Tk()
window.geometry("500x500")

def password():
    p='zxcvbnmasdfghjklqwertyuiopQWERTYUIOPASDFGHJKLXCVBNM'
    l=8
    a=''.join(random.sample(p,l))
    e1.delete(0,END)
    e1.insert(0,a)

l1=Label(window,text="Generate Password")
l1.pack()
e1=Entry(window,width=20)
e1.pack()

b=Button(window,text="Generate Password",width=20,command=password)
b.pack()
window.mainloop()

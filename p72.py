from tkinter import *
import random
window=Tk()
window.geometry("500x500")

def password():
    p="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12304567890"
    l=8
    pas=''.join(random.sample(p,l))
    e1.delete(0,END)
    e1.insert(0,pas)
    
    
l1=Label(window,text="Generate Password : ",font=("arial",10))
l1.pack()

e1=Entry(window,width=20,font=("arial",10))
e1.pack()

b1=Button(window,text="Generate Password : ",font=("arial",10),command=password)
b1.pack()
window.mainloop()
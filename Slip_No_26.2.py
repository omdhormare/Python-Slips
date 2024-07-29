'''B) Write Python GUI program which accepts a sentence from the user and alters it 
when a button is pressed. Every space should be replaced by *, case of all alphabets 
should be reversed, digits are replaced by?'''
from tkinter import *
window=Tk()

def convert():
    s=e1.get()
    s1=""
    for ch in s:
        if ch==" ":
            s1=s1+"*"
        elif ch>='a' and ch<='z':
            s1=s1+ch.upper()    
        elif ch>='A' and ch<='Z':
            s1=s1+ch.lower()
        elif ch>='0' and ch<'9':
            s1=s1+"?"
        else:
            s1 += ch
    e2.delete(0,END)        
    e2.insert(0,s1)

window.geometry("1000x1000")
l1=Label(window,text="Enter A Sentence : ")
l1.pack()

e1=Entry(window,width="30")
e1.pack(pady=(0,10))

l2=Label(window,text="Result : ")
l2.pack()

e2=Entry(window,width="30")
e2.pack(pady=(0,10))

b=Button(window,text="Replaced",width="10",command=convert)
b.pack()
window.mainloop()
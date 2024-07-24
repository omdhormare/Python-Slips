# Write Python GUI program that takes input string and change letter to upper case when a 
# button is pressed.

from tkinter import *

def upper_string():
    s=t.get()
    s1=s.upper()
    t1.delete(0,END)
    t1.insert(0,s1)

window=Tk()
window.geometry("1000x1000")

l=Label(window,text="Enter String : ",font=("arial",20))
l.pack()
t=Entry(window,width="20",font=("arial",20))
t.pack()

l1=Label(window,text="Result",width="20",font=("arial",20))
l1.pack()
t1=Entry(window,width="20",font=("arial",20))
t1.pack()

b=Button(window,text="Submit",font=("arial",20),pady=10,padx=100,command=upper_string).pack()
window.mainloop()
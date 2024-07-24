#A) Write a Python GUI program to accept a number form user and display its multiplication 
# table on button click. 

from tkinter import *
window=Tk()
def mul():
    n=e.get()
    n=int(n)
    t.delete(0,END)
    for i in range(1,11):
        t.insert(END,n*i)
        
window.geometry("1000x1000")
l=Label(window,text="Enter No : ",font=("arial",20))
l.pack()

e=Entry(window,width="10",font=("arial",20))
e.pack()

l1=Label(window,text="Multiplication Table : ",font=("arial",20))
l1.pack()
t=Listbox(window,font=("arial",20))
t.pack()

b=Button(window,text="Multiplication",font=("arial",20),command=mul)
b.pack()
window.mainloop()
'''A) Write a Python GUI program to create a list of Computer Science Courses using 
Tkinter module (use Listbox). '''
from tkinter import *
window=Tk()
window.geometry("500x500")
t=Label(window,text="List Box",font=("Arial",20))
t.pack()
l=Listbox(window,width="20",height="5")
l.pack()
l.insert(1,"C")
l.insert(2,"C++")
l.insert(3,"Java")
l.insert(4,"Python")
l.insert(5,"PHP")
l.insert(6,"DBMS")
l.insert(7,"RDBMS")
l.insert(8,"Web Technology")

window.mainloop()
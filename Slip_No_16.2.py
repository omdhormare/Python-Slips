'''
B) Write Python GUI program to add items in listbox widget and to print and delete the 
selected items from listbox on button click. Provide three separate buttons to add, print 
and delete.
'''

from tkinter import *
window=Tk()
window.geometry("1000x1000")
  
def add():
    s1=e1.get()
    l.insert(0,s1)
    
def del1():
    l.delete(ANCHOR)

 
l1=Label(window,text="Enter Item Name : ",font=("arial",20))
l1.pack(pady="10")
e1=Entry(window,width="30",font=("arial",20))
e1.pack(pady="10")

l=Listbox(window)
l.pack()

b1=Button(window,text="Add",width="20",font=("arial",10),command=add)
b1.pack(pady="10")
b2=Button(window,text="Delete",width="20",font=("arial",10),command=del1)
b2.pack(pady="10")
b3=Button(window,text="Print",width="20",font=("arial",10))
b3.pack()
window.mainloop()
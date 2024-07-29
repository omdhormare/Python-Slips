'''B) Write Python GUI program to accept a decimal number and convert and display it to 
binary, octal and hexadecimal number.'''

from tkinter import *
window=Tk()
window.geometry("1000x1000")
def bch():
    n=e1.get()
    n=int(n)
    b=bin(n)[2:]
    o=oct(n)[2:]
    h=hex(n)[2:]
    
    
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    
    e2.insert(0,b)
    e3.insert(0,o)
    e4.insert(0,h)
    
  
l1=Label(window,text="Enter Number : ")
l1.pack()

e1=Entry(window,width="20")
e1.pack()

l2=Label(window,text="Binary  : ")
l2.pack()

e2=Entry(window,width="20")
e2.pack()

l3=Label(window,text="Octal : ")
l3.pack()

e3=Entry(window,width="20")
e3.pack()

l4=Label(window,text="Hexadecimal : ")
l4.pack()

e4=Entry(window,width="20")
e4.pack(pady=(0, 10))

b=Button(window,text="Convert",width="10",height="1",bg="green",fg="orange",command=bch)
b.pack()
window.mainloop()
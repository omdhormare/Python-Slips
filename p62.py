'''B) Write a Python GUI program to create a label and change the label font style (font 
name, bold, size). Specify separate check button for each style.'''
from tkinter import *
window=Tk()
window.geometry("500x500")

def font():
    l1.config(font=("Castellar"))
    
def bold():
    l1.config(font=("Castellar",12,"bold"))
    
def size():
    l1.config(font=("arial",50))    
    
l1=Label(window,text="Hii I Am Om")
l1.pack()

b1=Checkbutton(window,text="Gigi",command=font)
b1.pack()

b2=Checkbutton(window,text="Bold" ,command=bold)
b2.pack()

b3=Checkbutton(window,text="Font Size " ,command=size)
b3.pack()
window.mainloop()
'''B) Write a Python GUI program to create a label and change the label font style (font 
name, bold, size). Specify separate check button for each style. '''
from tkinter import *
window=Tk()
window.geometry("500x500")

def name():
    l1.config(font=("Arial", 12))
def bold():
    l1.config(font=("Arial", 12, "bold"))
def size():
    l1.config(font=("Arial", 20))
    
l1=Label(window, text="Om Dada...")
l1.pack()

c1=Checkbutton(window, text="Gigi", command=name)
c1.pack()
c2=Checkbutton(window, text="Bold Name", command=bold)
c2.pack()
c3=Checkbutton(window, text="Font Size", command=size)
c3.pack()

window.mainloop()

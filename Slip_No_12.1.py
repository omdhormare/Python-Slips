'''A) Write a Python GUI program to create a label and change the label font style (font 
name, bold, size) using tkinter module. '''
from tkinter import *
window=Tk()
window.geometry("500x500")
l1=Label(window,text="Om Dada",font=("arial",20,"bold"))
l1.pack()
window.mainloop()
'''A) Write a Python GUI program to create a label and change the label font style (font 
name, bold, size) using tkinter modul'''
from tkinter import *
window=Tk()
window.geometry("500x500")
l1=Label(text="I am Om Dhormare", font=("arial",20,"bold"))
l1.pack()
window.mainloop()

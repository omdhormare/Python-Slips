from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("500x500")

def show():
    messagebox.showinfo("Alert","Hii I am Om dhormare")

b1=Button(window,text="Press Button",width=20,command=show)
b1.pack()
window.mainloop()

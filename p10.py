from tkinter import *
from tkinter import messagebox
window=Tk()
def add():
    messagebox.showinfo("Alert","Hii,Hello")
window.geometry("500x500")
b=Button(window,text="Pressed Button", command=add)
b.pack()
window.mainloop()
#A) Write Python GUI program to display an alert message when a button is pressed.
from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("1000x1000")
def button():
    messagebox.showinfo("Alert","Hii How Are You....!")

b=Button(window,text="Pressed Button",command=button)
b.pack()
window.mainloop()
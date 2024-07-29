'''A) Write a Python GUI program to create a label and change the label font style (font 
name, bold, size) using tkinter module. '''

from tkinter import *

window = Tk()
window.geometry("10000x1000")

l1 = Label(window, text="Om Dada", font=("gigi",60,"bold"))
l1.pack()

window.mainloop()


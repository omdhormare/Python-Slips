#A) Write Python GUI program to create background with changing colors
import random
from tkinter import *

window = Tk()
window.geometry("1000x1000")

def change_color():
    c=['red','pink','yellow','orange','white','blue','gold','purple','black','green']
    color=random.choice(c)
    window.config(bg=color)
    window.after(1000,change_color)

change_color()
window.mainloop()
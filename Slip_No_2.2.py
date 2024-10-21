#B)Write Python GUI program to create a digital clock with Tkinter to display the time.
import time
from tkinter import *
window=Tk()

def digital_clock():
    t=time.strftime("%H : %M : %S : %D")
    l.config(text=t)
    l.after(100,digital_clock)
    
window.geometry("1000x1000")
l=Label(window,font=("arial","60"),fg="orange",bg="black")
l.pack()
digital_clock()
window.mainloop()
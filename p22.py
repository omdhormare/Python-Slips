from tkinter import *
import time
window=Tk()
window.geometry("500x500")

def show_time():
    t=time.strftime("%I : %H : %M : %S")
    l.config(text=t)
    l.after(100,show_time)

l=Label(window,font=("arial",20,"bold"),fg="red",bg="orange")
l.pack()
show_time()
window.mainloop()
from tkinter import *

window=Tk()
window.geometry("500x500")

def font():
    l1.config(font=("arial"))
def  bold():
    l1.config(font=("bold",10))
def size():
    l1.config(font=(30))
l1=Label(window,text="I am Om Dhormare")
l1.pack()
c1=Checkbutton(window,text="Font",command=font)
c1.pack()
c2=Checkbutton(window,text="Bold",command=bold)
c2.pack()
c3=Checkbutton(window,text="Size",command=size)
c3.pack()
window.mainloop()

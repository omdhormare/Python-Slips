from tkinter import *
window=Tk()
window.geometry("500x500")

def red():
    window.config(bg="red")
def black():
    window.config(bg="black")
menu=Menu(window)
color_menu=Menu(menu)
color_menu.add_command(label="Red",command=red)
color_menu.add_command(label="Black",command=black)
menu.add_cascade(label="Color", menu=color_menu)

window.config(menu=menu)
window.mainloop()


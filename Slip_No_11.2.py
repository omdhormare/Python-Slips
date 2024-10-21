'''B) Write Python GUI program to add menu bar with name of colors as options to 
change the background color as per selection from menu option'''

from tkinter import *
def change1():
    window.config(bg="pink")
def change2():
    window.config(bg="yellow")
def change3():
    window.config(bg="orange")

window = Tk() 
menubar = Menu(window) 
color = Menu(menubar) 
color.add_command(label="pink",command=change1) 
color.add_command(label="yellow",command=change2) 
color.add_command(label="orange",command=change3) 
menubar.add_cascade(label="Color", menu=color)

window.config(menu=menubar) 
window.mainloop()
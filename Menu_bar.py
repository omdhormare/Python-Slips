from tkinter import *

window = Tk()
window.geometry("1000x1000")

menu = Menu(window)
window.config(menu=menu)  # Configure the window to use the menu

m1 = Menu(menu)
m1.add_command(label="Add New File")  # Use lowercase 'label'
menu.add_cascade(label="File", menu=m1)  # Add the menu to the menubar

window.mainloop()

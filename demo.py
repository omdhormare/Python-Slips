import tkinter as tk
import random

def change_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]
    new_color = random.choice(colors)
    root.config(bg=new_color)
    root.after(1000, change_color)  # Change color every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Color Changing Background")
root.geometry("400x300")

# Start the color changing loop
change_color()

# Run the application
root.mainloop()

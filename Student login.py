from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
from dashboard import open_dashboard 


def login():
    u = e1.get()
    p = e2.get()
    con = mc.connect(host="localhost", username="root", password="root", database="student")
    db = con.cursor()
    db.execute("select * from login where username=%s and password=%s", (u, p))
    res = db.fetchall()
    if res:
        messagebox.showinfo("Login", "Successfully Logged In")
        window.withdraw() 
        open_dashboard()  
    else:
        messagebox.showerror("Invalid login", "Incorrect Username or Password")
    con.commit()

window = Tk()
window.title("Employee Management System")
window.geometry("1300x1300")

frame = Frame(window, bg="lightblue", bd=10)
frame.place(relx=0.5, rely=0.3, anchor=CENTER)

l1 = Label(frame, text="Employee Login", font=("Arial", 30, "bold"), bg="lightblue")
l1.grid(row=0, column=0, columnspan=2, pady=20)

l2 = Label(frame, text="Enter User Name: ", font=("Arial", 16), bg="lightblue")
l2.grid(row=1, column=0, pady=10, padx=10, sticky=E)

e1 = Entry(frame, width=25, font=("Arial", 14))
e1.grid(row=1, column=1, pady=10, padx=10)

l3 = Label(frame, text="Enter Password: ", font=("Arial", 16), bg="lightblue")
l3.grid(row=2, column=0, pady=10, padx=10, sticky=E)

e2 = Entry(frame, width=25, font=("Arial", 14), show="*")
e2.grid(row=2, column=1, pady=10, padx=10)

b = Button(frame, text="Login", width=20, font=("Arial", 16, "bold"), command=login, bg="blue", fg="white")
b.grid(row=3, column=0, columnspan=2, pady=20)


footer = Label(window, text="Developed by : Om Dhormare © Employee Management System 2024. All rights reserved.", font=("Arial", 16, "bold"), bg="lightblue")
footer.place(relx=0.5, rely=0.95, anchor=S)


window.mainloop()
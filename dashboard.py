from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mc  # Import for MySQL connector

def add():
    con = mc.connect(host="localhost", user="root", password="root", database="emp")
    db = con.cursor()

    if not (e1.get() and e2.get() and e3.get() and e4.get() and e5.get() and e6.get()):
        messagebox.showerror("Error", "All Fields Are Required.")
    else:
        query = "INSERT INTO emp (emp_id, name, phone, role, gender, salary) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get())
        db.execute(query, values)
        con.commit()

        messagebox.showinfo("Success", "Employee Added Successfully!")
        show_data()

    db.close()
    con.close()

def update():
    con = mc.connect(host="localhost", user="root", password="root", database="emp")
    db = con.cursor()

    if not (e1.get() and e2.get() and e3.get() and e4.get() and e5.get() and e6.get()):
        messagebox.showerror("Error", "All Fields Are Required.")
    else:
        query = "UPDATE emp SET name=%s, phone=%s, role=%s, gender=%s, salary=%s WHERE emp_id=%s"
        values = (e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e1.get())
        db.execute(query, values)
        con.commit()

        messagebox.showinfo("Success", "Employee Updated Successfully!")
        show_data()

    db.close()
    con.close()

def delete():
    con = mc.connect(host="localhost", user="root", password="root", database="emp")
    db = con.cursor()

    if not e1.get():
        messagebox.showerror("Error", "Employee ID is required for deletion.")
    else:
        query = "DELETE FROM emp WHERE emp_id=%s"
        db.execute(query, (e1.get(),))
        con.commit()

        messagebox.showinfo("Success", "Employee Deleted Successfully!")
        show_data()

    db.close()
    con.close()

def show_data():
    con = mc.connect(host="localhost", user="root", password="root", database="emp")
    db = con.cursor()
    query = "SELECT * FROM emp"
    db.execute(query)
    rows = db.fetchall()

    for i in employee_table.get_children():
        employee_table.delete(i)

    for row in rows:
        employee_table.insert("", "end", values=row)

    db.close()

def open_dashboard():
    dashboard = Tk()
    dashboard.title("Employee Management System")
    dashboard.geometry("800x600")
    dashboard.config(bg="lightblue")

    title_label = Label(dashboard, text="Employee Management System", font=("Arial", 24, "bold"), bg="lightblue")
    title_label.pack(pady=20)

    form_frame = Frame(dashboard, bg="lightblue")
    form_frame.pack(pady=20)

    Label(form_frame, text="ID", font=("Arial", 12), bg="lightblue").grid(row=0, column=0, padx=10, pady=5)
    global e1
    e1 = Entry(form_frame, font=("Arial", 12))
    e1.grid(row=0, column=1, padx=10, pady=5)

    Label(form_frame, text="Name", font=("Arial", 12), bg="lightblue").grid(row=1, column=0, padx=10, pady=5)
    global e2
    e2 = Entry(form_frame, font=("Arial", 12))
    e2.grid(row=1, column=1, padx=10, pady=5)

    Label(form_frame, text="Phone", font=("Arial", 12), bg="lightblue").grid(row=2, column=0, padx=10, pady=5)
    global e3
    e3 = Entry(form_frame, font=("Arial", 12))
    e3.grid(row=2, column=1, padx=10, pady=5)

    Label(form_frame, text="Role", font=("Arial", 12), bg="lightblue").grid(row=3, column=0, padx=10, pady=5)
    global e4
    e4 = ttk.Combobox(form_frame, values=["Web Developer", "Manager", "Tester"], font=("Arial", 12))
    e4.grid(row=3, column=1, padx=10, pady=5)

    Label(form_frame, text="Gender", font=("Arial", 12), bg="lightblue").grid(row=4, column=0, padx=10, pady=5)
    global e5
    e5 = ttk.Combobox(form_frame, values=["Male", "Female"], font=("Arial", 12))
    e5.grid(row=4, column=1, padx=10, pady=5)

    Label(form_frame, text="Salary", font=("Arial", 12), bg="lightblue").grid(row=5, column=0, padx=10, pady=5)
    global e6
    e6 = Entry(form_frame, font=("Arial", 12))
    e6.grid(row=5, column=1, padx=10, pady=5)

    Button(form_frame, text="Add Employee", font=("Arial", 12), bg="green", fg="white", command=add).grid(row=6, column=0, padx=10, pady=10)
    Button(form_frame, text="Update Employee", font=("Arial", 12), bg="orange", fg="white", command=update).grid(row=6, column=1, padx=10, pady=10)
    Button(form_frame, text="Delete Employee", font=("Arial", 12), bg="red", fg="white", command=delete).grid(row=6, column=2, padx=10, pady=10)

    columns = ("ID", "Name", "Phone", "Role", "Gender", "Salary")
    global employee_table
    employee_table = ttk.Treeview(dashboard, columns=columns, show='headings', height=10)
    employee_table.pack(pady=20)

    for col in columns:
        employee_table.heading(col, text=col)
        employee_table.column(col, width=150)

    Button(dashboard, text="Show All", font=("Arial", 20), bg="blue", fg="white", command=show_data).pack(pady=10)

    dashboard.mainloop()

# Open the dashboard window
open_dashboard()

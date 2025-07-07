# ------------------------- #
#  Employee Management GUI  #
# ------------------------- #

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Dictionary to store employee data
employees = {}

# --------------------- #
#   Backend Operations  #
# --------------------- #

# Add a new employee
def add_employee():
    emp_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    salary = entry_salary.get()
    department = entry_department.get()

    if emp_id and name:
        employees[emp_id] = {
            "name": name,
            "age": age,
            "salary": salary,
            "department": department
        }
        messagebox.showinfo("Success", f"Employee {name} added.")
        clear_fields()
    else:
        messagebox.showerror("Error", "ID and Name are required.")

# View all employee details
def view_employees():
    if employees:
        result = ""
        for emp_id, details in employees.items():
            result += (
                f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, "
                f"Salary: {details['salary']}, Dept: {details['department']}\n"
            )
        messagebox.showinfo("Employee List", result)
    else:
        messagebox.showinfo("Empty", "No employees found.")

# Update an existing employee's data
def update_employee():
    emp_id = simpledialog.askstring("Update", "Enter employee ID to update:")
    if emp_id in employees:
        name = simpledialog.askstring("Update", "Enter new name:")
        age = simpledialog.askstring("Update", "Enter new age:")
        salary = simpledialog.askstring("Update", "Enter new salary:")
        department = simpledialog.askstring("Update", "Enter new department:")

        if name:
            employees[emp_id]["name"] = name
        if age:
            employees[emp_id]["age"] = age
        if salary:
            employees[emp_id]["salary"] = salary
        if department:
            employees[emp_id]["department"] = department

        messagebox.showinfo("Updated", f"Employee {emp_id} updated.")
    else:
        messagebox.showerror("Error", "Employee ID not found.")

# Delete an employee from the system
def delete_employee():
    emp_id = simpledialog.askstring("Delete", "Enter employee ID to delete:")
    if emp_id in employees:
        del employees[emp_id]
        messagebox.showinfo("Deleted", f"Employee {emp_id} deleted.")
    else:
        messagebox.showerror("Error", "Employee ID not found.")

# Save employee data to a file
def save_to_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        try:
            with open(filename, "w") as file:
                for emp_id, emp_details in employees.items():
                    line = f"{emp_id} :--> {emp_details['name']},{emp_details['age']},{emp_details['salary']},{emp_details['department']}\n"
                    file.write(line)
            messagebox.showinfo("Saved", f"Data saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {e}")

# Load employee data from a file
def load_from_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        try:
            with open(filename, "r") as file:
                global employees
                employees = {}
                for line in file:
                    if ":-->" in line:
                        emp_id_part, details_part = line.strip().split(":-->")
                        emp_id = emp_id_part.strip()
                        details = details_part.strip().split(",")

                        if len(details) == 4:
                            employees[emp_id] = {
                                "name": details[0].strip(),
                                "age": details[1].strip(),
                                "salary": details[2].strip(),
                                "department": details[3].strip()
                            }
            messagebox.showinfo("Loaded", f"Data loaded from {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load: {e}")

# Clear input fields
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_salary.delete(0, tk.END)
    entry_department.delete(0, tk.END)

# --------------------- #
#     GUI Interface     #
# --------------------- #

# Window setup
window = tk.Tk()
window.title("Employee Management System")

# Employee ID
tk.Label(window, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(window)
entry_id.grid(row=0, column=1, padx=10, pady=5)

# Name
tk.Label(window, text="Name").grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1, padx=10, pady=5)

# Age
tk.Label(window, text="Age").grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(window)
entry_age.grid(row=2, column=1, padx=10, pady=5)

# Salary
tk.Label(window, text="Salary").grid(row=3, column=0, padx=10, pady=5)
entry_salary = tk.Entry(window)
entry_salary.grid(row=3, column=1, padx=10, pady=5)

# Department
tk.Label(window, text="Department").grid(row=4, column=0, padx=10, pady=5)
entry_department = tk.Entry(window)
entry_department.grid(row=4, column=1, padx=10, pady=5)

# Action Buttons
tk.Button(window, text="Add Employee", command=add_employee).grid(row=5, column=0, pady=10)
tk.Button(window, text="View Employees", command=view_employees).grid(row=5, column=1, pady=10)
tk.Button(window, text="Update Employee", command=update_employee).grid(row=6, column=0, pady=10)
tk.Button(window, text="Delete Employee", command=delete_employee).grid(row=6, column=1, pady=10)
tk.Button(window, text="Save to File", command=save_to_file).grid(row=7, column=0, pady=10)
tk.Button(window, text="Load from File", command=load_from_file).grid(row=7, column=1, pady=10)
tk.Button(window, text="Exit", command=window.quit).grid(row=8, column=0, columnspan=2, pady=20)

# Start the main loop
window.mainloop()

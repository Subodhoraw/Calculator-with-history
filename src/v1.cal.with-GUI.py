import tkinter as tk
from tkinter import messagebox

# Basic operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error"
    return a / b
def average(a, b): return (a + b) / 2

# Function to perform selected operation
def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if operation == "add":
            res = add(a, b)
            op_symbol = "+"
        elif operation == "subtract":
            res = subtract(a, b)
            op_symbol = "-"
        elif operation == "multiply":
            res = multiply(a, b)
            op_symbol = "*"
        elif operation == "divide":
            res = divide(a, b)
            op_symbol = "/"
        elif operation == "average":
            res = average(a, b)
            op_symbol = "avg"

        result_label.config(text=f"{a} {op_symbol} {b} = {res}")
        history_list.insert(tk.END, f"{a} {op_symbol} {b} = {res}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Function to clear entries
def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result will appear here")

# GUI setup
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x450")
root.resizable(False, False)

# Title label
tk.Label(root, text="Simple Python Calculator", font=("Arial", 14, "bold")).pack(pady=10)

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root, width=20)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root, width=20)
entry2.pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="+", width=5, command=lambda: calculate("add")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="-", width=5, command=lambda: calculate("subtract")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="*", width=5, command=lambda: calculate("multiply")).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="/", width=5, command=lambda: calculate("divide")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="avg", width=5, command=lambda: calculate("average")).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Clear", width=8, command=clear_fields).grid(row=1, column=2, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="Result will appear here", font=("Arial", 12))
result_label.pack(pady=10)

# History box
tk.Label(root, text="History:").pack()
history_list = tk.Listbox(root, width=40, height=10)
history_list.pack(pady=5)

# Run the GUI
root.mainloop()

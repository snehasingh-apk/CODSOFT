import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    num1_str = entry1.get()
    num2_str = entry2.get()
    operation = operation_var.get()

    # Validate numeric input
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return

    # Perform the selected operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            return
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            messagebox.showerror("Error", "Modulus by zero is not allowed.")
            return
        result = num1 % num2
    elif operation == '//':
        if num2 == 0:
            messagebox.showerror("Error", "Floor division by zero is not allowed.")
            return
        result = num1 // num2
    elif operation == '**':
        result = num1 ** num2
    else:
        messagebox.showerror("Error", "Please select a valid operation.")
        return

    result_label.config(text=f"Result: {result}")

# Main window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("350x320")
root.resizable(False, False)

# Title
tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Input 1
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

# Input 2
tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)

# Operation selection
tk.Label(root, text="Select Operation:").pack()
operation_var = tk.StringVar()
operation_var.set('+')  # default
operations = ['+', '-', '*', '/', '%', '//', '**']
tk.OptionMenu(root, operation_var, *operations).pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate, bg="lightblue", font=("Arial", 12)).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()


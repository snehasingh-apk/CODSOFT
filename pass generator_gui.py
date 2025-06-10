import tkinter as tk
from tkinter import messagebox
import random
import string

# Core logic for password creation
def create_password():
    try:
        length = int(input_box.get())
        if length < 4:
            messagebox.showwarning("Length Error", "Please choose at least 4 characters.")
            return
    except:
        messagebox.showerror("Input Error", "Length must be a number.")
        return

    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(all_chars)

    password_box.delete(0, tk.END)
    password_box.insert(0, password)

# GUI window setup
app = tk.Tk()
app.title("SecurePass Generator")
app.geometry("380x220")
app.config(bg="#e1eaff")
app.resizable(False, False)

# Title label
title = tk.Label(app, text="Password Generator", font=("Arial", 16, "bold"), bg="#e1eaff")
title.pack(pady=12)

# Length input
frame = tk.Frame(app, bg="#e1eaff")
frame.pack()
tk.Label(frame, text="Length:", bg="#e1eaff", font=("Arial", 10)).pack(side="left")
input_box = tk.Entry(frame, width=5, font=("Arial", 10))
input_box.pack(side="left", padx=8)

# Generate button
gen_btn = tk.Button(app, text="Create Password", command=create_password, bg="#0066cc", fg="white", width=18)
gen_btn.pack(pady=15)

# Output field
tk.Label(app, text="Generated Password:", bg="#e1eaff", font=("Arial", 10)).pack()
password_box = tk.Entry(app, width=35, font=("Consolas", 12), justify="center")
password_box.pack(pady=6)

# Start the application
app.mainloop()


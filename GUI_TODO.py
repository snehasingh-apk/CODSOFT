import tkinter as tk
from tkinter import messagebox

# Main app window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(False, False)

tasks = []

# --- Functions ---
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to delete!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = tasks[selected]
        tasks[selected] = f"✓ {task}" if not task.startswith("✓ ") else task[2:]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to mark as done!")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# --- Widgets ---

# Entry box
entry = tk.Entry(root, font=("Arial", 14), width=28)
entry.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack()

add_btn = tk.Button(frame, text="Add Task", width=10, command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)

done_btn = tk.Button(frame, text="Mark Done", width=10, command=mark_done)
done_btn.pack(side=tk.LEFT, padx=5)

del_btn = tk.Button(frame, text="Delete Task", width=10, command=delete_task)
del_btn.pack(side=tk.LEFT, padx=5)

# Listbox
listbox = tk.Listbox(root, font=("Arial", 14), width=38, height=15, selectbackground="#a6a6a6")
listbox.pack(pady=10)

# Run the GUI loop
root.mainloop()

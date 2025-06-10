import tkinter as tk
from tkinter import messagebox, simpledialog

# List to store contact data
contact_data = []

def create_contact():
    cname = simpledialog.askstring("New Contact", "Full Name:")
    cphone = simpledialog.askstring("New Contact", "Phone:")
    cemail = simpledialog.askstring("New Contact", "Email:")
    caddress = simpledialog.askstring("New Contact", "Address:")

    if cname and cphone:
        contact_data.append({
            "name": cname,
            "phone": cphone,
            "email": cemail,
            "address": caddress
        })
        messagebox.showinfo("Saved", f"'{cname}' has been added.")
        show_all()
    else:
        messagebox.showerror("Missing Info", "Name and phone number are mandatory.")

def show_all():
    contact_box.delete(0, tk.END)
    for entry in contact_data:
        contact_box.insert(tk.END, f"{entry['name']} | {entry['phone']}")

def find_contact():
    key = simpledialog.askstring("Search", "Enter name or phone:")
    contact_box.delete(0, tk.END)
    for person in contact_data:
        if key.lower() in person['name'].lower() or key in person['phone']:
            contact_box.insert(tk.END, f"{person['name']} | {person['phone']}")

def edit_contact():
    selected = contact_box.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Pick a contact to edit.")
        return
    idx = selected[0]
    entry = contact_data[idx]

    new_name = simpledialog.askstring("Edit Contact", "Name:", initialvalue=entry['name'])
    new_phone = simpledialog.askstring("Edit Contact", "Phone:", initialvalue=entry['phone'])
    new_email = simpledialog.askstring("Edit Contact", "Email:", initialvalue=entry['email'])
    new_addr = simpledialog.askstring("Edit Contact", "Address:", initialvalue=entry['address'])

    if new_name and new_phone:
        contact_data[idx] = {
            "name": new_name,
            "phone": new_phone,
            "email": new_email,
            "address": new_addr
        }
        messagebox.showinfo("Updated", "Contact details updated.")
        show_all()
    else:
        messagebox.showerror("Missing Info", "Name and phone cannot be empty.")

def remove_contact():
    selected = contact_box.curselection()
    if not selected:
        messagebox.showerror("Error", "Choose a contact to delete.")
        return
    idx = selected[0]
    removed_name = contact_data[idx]['name']
    del contact_data[idx]
    messagebox.showinfo("Deleted", f"Removed contact: {removed_name}")
    show_all()

# Main App Window
app = tk.Tk()
app.title("My Contact Book")
app.geometry("420x430")
app.configure(bg="#f0f0f0")

# Buttons
tk.Button(app, text="➕ Add", width=15, command=create_contact).pack(pady=5)
tk.Button(app, text="📋 View All", width=15, command=show_all).pack(pady=5)
tk.Button(app, text="🔍 Search", width=15, command=find_contact).pack(pady=5)
tk.Button(app, text="✏️ Edit", width=15, command=edit_contact).pack(pady=5)
tk.Button(app, text="❌ Delete", width=15, command=remove_contact).pack(pady=5)

# Contact Display
contact_box = tk.Listbox(app, width=55, height=15)
contact_box.pack(pady=15)

# Run the GUI
app.mainloop()


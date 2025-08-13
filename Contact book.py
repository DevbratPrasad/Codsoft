import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact storage
contacts = []

# Add Contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    phone = simpledialog.askstring("Add Contact", "Enter phone number:")
    email = simpledialog.askstring("Add Contact", "Enter email:")
    address = simpledialog.askstring("Add Contact", "Enter address:")
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", f"Contact '{name}' added.")
        view_contacts()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")

# View Contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")

# Search Contact
def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    contact_list.delete(0, tk.END)
    for c in contacts:
        if query.lower() in c['name'].lower() or query in c['phone']:
            contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")

# Update Contact
def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to update.")
        return
    index = selected[0]
    contact = contacts[index]
    name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact['name'])
    phone = simpledialog.askstring("Update Contact", "Enter new phone:", initialvalue=contact['phone'])
    email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact['email'])
    address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact['address'])
    if name and phone:
        contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", f"Contact '{name}' updated.")
        view_contacts()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")

# Delete Contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to delete.")
        return
    index = selected[0]
    contact = contacts.pop(index)
    messagebox.showinfo("Deleted", f"Contact '{contact['name']}' deleted.")
    view_contacts()

# GUI 
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(frame, text="View", width=10, command=view_contacts).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Search", width=10, command=search_contact).grid(row=0, column=2, padx=5)
tk.Button(frame, text="Update", width=10, command=update_contact).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Delete", width=10, command=delete_contact).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Exit", width=10, command=root.quit).grid(row=1, column=2, padx=5, pady=5)

# List to show contacts
contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=10)

# Start
root.mainloop()

import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

class ToDoListGUI:
    def __init__(self, root, filename="todo_data.json"):
        self.root = root
        self.root.title("To-Do List Application")
        self.filename = filename
        self.tasks = []
        self.load_tasks()

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)

        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="Add Task", width=15, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Mark Completed", width=15, command=self.mark_task).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Delete Task", width=15, command=self.delete_task).grid(row=0, column=2, padx=5)

        self.refresh_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "✔" if task["completed"] else "✘"
            self.listbox.insert(tk.END, f"{idx+1}. [{status}] {task['task']}")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.save_tasks()
            self.refresh_tasks()

    def mark_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Select Task", "Please select a task to mark as completed.")
            return
        index = selection[0]
        self.tasks[index]["completed"] = True
        self.save_tasks()
        self.refresh_tasks()

    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Select Task", "Please select a task to delete.")
            return
        index = selection[0]
        self.tasks.pop(index)
        self.save_tasks()
        self.refresh_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()

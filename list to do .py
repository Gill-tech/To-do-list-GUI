import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task = listbox.get(selected_task_index)
        listbox.itemconfig(selected_task_index, {'bg': 'light green'})
        messagebox.showinfo("Task completed", f"Task '{task}' marked as completed.")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# create the main window
root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Button to add task
add_button = tk.Button(root, text="Add Task", command=add_task, width=15, height=2)
add_button.grid(row=0, column=2, padx=10, pady=10)

# Button to display tasks
listbox = tk.Listbox(root, selectbackground='light blue', selectmode=tk.SINGLE, font=('Arial', 12), width=30, height=10)
listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

# Buttons to remove and mark tasks as completed
remove_button = tk.Button(root, text="Remove Task", command=remove_task, width=15, height=2)
remove_button.grid(row=2, column=0, padx=10, pady=10)

completed_button = tk.Button(root, text="Mark Completed", command=mark_completed, width=15, height=2)
completed_button.grid(row=2, column=1, padx=10, pady=10)

# run the tkinter event loop
root.mainloop()

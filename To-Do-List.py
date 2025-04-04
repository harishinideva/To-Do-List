import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(
            root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(
            root, width=50, height=10, selectmode=tk.SINGLE)
        self.tasks_listbox.pack()

        self.delete_button = tk.Button(
            root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.mark_done_button = tk.Button(
            root, text="Mark as Done", command=self.mark_as_done)
        self.mark_done_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.update_listbox()
        else:
            messagebox.showwarning(
                "Warning", "Please select a task to delete.")

    def mark_as_done(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            self.tasks[index] = f"✔️ {task}"
            self.update_listbox()
        else:
            messagebox.showwarning(
                "Warning", "Please select a task to mark as done.")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)


root = tk.Tk()
app = ToDoApp(root)
root.mainloop()

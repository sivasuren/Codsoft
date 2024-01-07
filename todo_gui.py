import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful To-Do List App")
        self.root.geometry("500x400")

        self.tasks = []

        self.load_tasks()

        self.task_treeview = ttk.Treeview(root, columns=("Title", "Due Date", "Priority", "Status"), show="headings")
        self.task_treeview.heading("Title", text="Title")
        self.task_treeview.heading("Due Date", text="Due Date")
        self.task_treeview.heading("Priority", text="Priority")
        self.task_treeview.heading("Status", text="Status")
        self.task_treeview.pack(pady=10)

        self.update_task_treeview()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg='#51c4d3', fg='white')
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg='#51c4d3', fg='white')
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg='#51c4d3', fg='white')
        self.delete_button.pack(pady=5)

        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed, bg='#51c4d3', fg='white')
        self.mark_completed_button.pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def update_task_treeview(self):
        self.task_treeview.delete(*self.task_treeview.get_children())
        for task in self.tasks:
            status = "Incomplete"
            if task['completed']:
                status = "Completed"
            self.task_treeview.insert("", tk.END, values=(task['title'], task.get('due_date', ''), task.get('priority', ''), status))

    def get_selected_index(self):
        selected_item = self.task_treeview.selection()
        if selected_item:
            index = int(selected_item[0][1:])
            if 0 <= index < len(self.tasks):
                return index
        return None

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            due_date = simpledialog.askstring("Add Task", "Enter due date (optional):")
            priority = simpledialog.askstring("Add Task", "Enter priority (optional):")

            new_task = {'title': title, 'completed': False, 'date': datetime.now().isoformat()}
            
            if due_date:
                new_task['due_date'] = due_date
            if priority:
                new_task['priority'] = priority
            
            self.tasks.append(new_task)
            self.save_tasks()
            self.update_task_treeview()

    def update_task(self):
        index = self.get_selected_index()
        if index is not None:
            title = simpledialog.askstring("Update Task", "Enter updated task title:", initialvalue=self.tasks[index]['title'])
            if title:
                self.tasks[index]['title'] = title
                self.save_tasks()
                self.update_task_treeview()
        else:
            messagebox.showwarning("Invalid Selection", "Please select a task to update.")

    def delete_task(self):
        index = self.get_selected_index()
        if index is not None:
            confirmation = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirmation:
                del self.tasks[index]
                self.save_tasks()
                self.update_task_treeview()
        else:
            messagebox.showwarning("Invalid Selection", "Please select a task to delete.")

    def mark_completed(self):
        index = self.get_selected_index()
        if index is not None:
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.save_tasks()
            self.update_task_treeview()
        else:
            messagebox.showwarning("Invalid Selection", "Please select a task to mark as completed.")

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

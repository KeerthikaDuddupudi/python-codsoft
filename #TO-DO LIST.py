#TO-DO LIST
import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO LIST")
        self.root.geometry("400x400")
        self.tasks = []

        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=1, padx=5, pady=10, columnspan=3)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg='#80c5ec')
        self.add_button.grid(row=0, column=3, padx=5, pady=10)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=12)
        self.task_listbox.grid(row=1, column=1, columnspan=3, padx=10, pady=50, sticky="nsew")

        self.display_button = tk.Button(root, text="Display Tasks", command=self.display_tasks, width=15, height=2, bg='#c0c9e8')
        self.display_button.grid(row=10, column=1, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, width=15, height=2, bg='#c0c9e8')
        self.remove_button.grid(row=10, column=2, padx=5, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, width=15, height=2, bg='#c0c9e8')
        self.exit_button.grid(row=10, column=3, padx=5, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-do list", "No tasks found")
        else:
            display_window = tk.Toplevel(self.root)
            display_window.title("Tasks")
            display_window.geometry("300x200")

            task_text = tk.Text(display_window, wrap=tk.WORD)
            task_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            task_list = "\n".join(self.tasks)
            task_text.insert(tk.END, f"Tasks:\n{task_list}")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.tasks.pop(index)
            self.task_listbox.delete(index)
            messagebox.showinfo("To-do list", f"Task '{removed_task}' removed successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

def main():
    root = tk.Tk()
    todo_list = TodoList(root)
    root.configure(bg="#fcc358")
    root.mainloop()

if __name__ == "__main__":
    main()
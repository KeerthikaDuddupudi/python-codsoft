#PASSWORD GENERATOR
import tkinter as tk
from tkinter import ttk, messagebox
from random import sample
from string import digits, ascii_letters, punctuation

class PasswordGeneratorApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("700x450")
        self.root.config(bg='#f9bded')

        self.setup_ui()

    def setup_ui(self):
    
        tk.Label(self.root, text="PASSWORD GENERATOR", font=('Arial Bold', 14), padx=20, pady=20).grid(row=0, column=0, columnspan=4, padx=50, pady=20)

        tk.Label(self.root, text="Enter password length:", font=('Arial Bold', 12),bg='#c9f88c').grid(row=1, column=0, padx=20, pady=10)
        self.cb = ttk.Combobox(self.root, width=10, values=[i for i in range(1, 21)])
        self.cb.grid(row=1, column=1, padx=20, pady=10)
        self.cb.current(0)

        tk.Label(self.root, text="Select password complexity:", font=('Arial Bold', 12),bg='#c9f88c').grid(row=2, column=0, padx=20, pady=10)
        self.complexity = tk.IntVar()
        tk.Radiobutton(self.root, text="Easy", value=0, variable=self.complexity, padx=15, pady=10,bg='#f9da6d').grid(row=2, column=1, padx=20, pady=10)
        tk.Radiobutton(self.root, text="Moderate", value=1, variable=self.complexity, padx=10, pady=10,bg='#f9da6d').grid(row=2, column=2, padx=20, pady=10)
        tk.Radiobutton(self.root, text="Hard", value=2, variable=self.complexity, padx=13, pady=10,bg='#f9da6d').grid(row=2, column=3, padx=20, pady=10)

        tk.Button(self.root, text="Generate Password", font=('Arial Bold', 12), padx=15, pady=15, command=self.generate,bg='#fed776').grid(row=3, column=0, columnspan=4, padx=20, pady=20)

        tk.Label(self.root, text=" new password", font=('Arial Bold', 12),bg='#c9f88c').grid(row=4, column=0, padx=20, pady=10)
        self.password_entry = tk.Entry(self.root, width=30, font=('Arial', 12), state='readonly')
        self.password_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

        tk.Button(self.root, text="Clear", font=('Arial Bold', 12), padx=15, pady=15, command=self.clear,bg='#f9da6d').grid(row=5, column=0, columnspan=4, padx=20, pady=20)

    def generate(self):
        try:
            length = int(self.cb.get())
            complexity = self.complexity.get()

            if length < 1:
                messagebox.showerror("Error", "Password length must be a positive integer.")
                return

            if complexity == 0:
                password = self.generate_password_easy(length)
            elif complexity == 1:
                password = self.generate_password_moderate(length)
            elif complexity == 2:
                password = self.generate_password_hard(length)

            self.password_entry.config(state='normal')
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            self.password_entry.config(state='readonly')

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length.")

    def generate_password_easy(self, length):
        characters = digits
        return ''.join(sample(characters, length))

    def generate_password_moderate(self, length):
        characters = ascii_letters+digits
        return ''.join(sample(characters, length))

    def generate_password_hard(self, length):
        characters = punctuation+ascii_letters+digits
        return ''.join(sample(characters, length))

    def clear(self):
        self.password_entry.config(state='normal')
        self.password_entry.delete(0, tk.END)
        self.cb.current(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
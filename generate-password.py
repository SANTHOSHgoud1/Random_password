import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()

        characters = string.ascii_letters
        if complexity == "Medium":
            characters += string.digits
        elif complexity == "Strong":
            characters += string.digits + string.punctuation

        password = "".join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
    except ValueError:
        # Handle invalid input (non-numeric length)
        pass

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Widgets
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)
complexity_label = tk.Label(root, text="Complexity:")
complexity_var = tk.StringVar(value="Medium")
complexity_menu = tk.OptionMenu(root, complexity_var, "Weak", "Medium", "Strong")
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
password_entry = tk.Entry(root, show="*")

# Grid layout
length_label.grid(row=0, column=0)
length_entry.grid(row=0, column=1)
complexity_label.grid(row=1, column=0)
complexity_menu.grid(row=1, column=1)
generate_button.grid(row=2, columnspan=2)
password_entry.grid(row=3, columnspan=2)

root.mainloop()

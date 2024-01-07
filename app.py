import tkinter as tk
from tkinter import StringVar
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            result_label.config(text="Invalid length. Please enter a positive integer.")
            return

        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer for the length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Label and entry widget for password length
length_label = tk.Label(window, text="Enter the desired length:")
length_var = StringVar()
length_entry = tk.Entry(window, textvariable=length_var)

# Button to generate and display the password
generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password)

# Label for displaying the generated password
result_label = tk.Label(window, text="Generated Password: ")

# Arrange widgets in the grid
length_label.grid(row=0, column=0, pady=10)
length_entry.grid(row=0, column=1, pady=10)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()

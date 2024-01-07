import tkinter as tk

def click_button(value):
    current_text = entry_var.get()
    
    if value == 'C':
        entry_var.set('')
    elif value == '=':
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set('Error')
    else:
        entry_var.set(current_text + str(value))

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget for displaying input and result
entry_var = tk.StringVar()
entry_var.set('')
entry = tk.Entry(window, textvariable=entry_var, justify='right', font=('Arial', 14))

# Buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2,
            command=lambda b=button: click_button(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Arrange the entry widget
entry.grid(row=0, column=0, columnspan=4)

# Start the main loop
window.mainloop()

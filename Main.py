import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def handle_keypress(event):
    if event.keysym.isdigit() or event.keysym in ['+', '-', '*', '/']:
        button_click(event.keysym)
    elif event.keysym == 'Return':
        calculate_result()
    elif event.keysym == 'BackSpace':
        button_backspace()

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#000000")

# Create an entry widget to display the numbers and results
entry = tk.Entry(window, width=16, borderwidth=5, font=("Helvetica", 28), justify="right", bg="#000000", fg="#ffffff")
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10, sticky="ew")

# Define the buttons
buttons = [
    ("C", 0, 0, "#9e9e9e"),
    ("7", 1, 0, "#000000"),
    ("8", 1, 1, "#000000"),
    ("9", 1, 2, "#000000"),
    ("4", 2, 0, "#000000"),
    ("5", 2, 1, "#000000"),
    ("6", 2, 2, "#000000"),
    ("1", 3, 0, "#000000"),
    ("2", 3, 1, "#000000"),
    ("3", 3, 2, "#000000"),
    ("0", 4, 0, "#000000"),
    (".", 4, 1, "#000000"),
    ("+", 1, 3, "#ff9500"),
    ("-", 2, 3, "#ff9500"),
    ("*", 3, 3, "#ff9500"),
    ("/", 4, 3, "#ff9500"),
    ("=", 4, 2, "#ff9500"),
    ("⌫", 0, 1, "#000000"),
]

# Create the buttons and assign their respective functions
for button_text, row, column, color in buttons:
    if button_text == "=":
        button = tk.Button(window, text=button_text, padx=35, pady=20, font=("Helvetica", 20),
                           command=calculate_result, bg=color, fg="#ffffff")
    elif button_text == "C":
        button = tk.Button(window, text=button_text, padx=35, pady=20, font=("Helvetica", 20),
                           command=button_clear, bg=color, fg="#ffffff")
    elif button_text == "⌫":
        button = tk.Button(window, text=button_text, padx=35, pady=20, font=("Helvetica", 20),
                           command=button_backspace, bg=color, fg="#ffffff")
    else:
        button = tk.Button(window, text=button_text, padx=35, pady=20, font=("Helvetica", 20),
                           command=lambda text=button_text: button_click(text), bg=color, fg="#ffffff")
    button.grid(row=row+1, column=column, padx=5, pady=5, sticky="nsew")

# Configure grid weights to make buttons and entry expandable
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
window.grid_rowconfigure(5, weight=1)

# Bind keypress event to handle_keypress function
window.bind("<Key>", handle_keypress)

# Start the main loop
window.mainloop()
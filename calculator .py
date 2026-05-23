import tkinter as tk


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END) 
    entry.insert(0, current + str(value)) 


def calculate():
    try:
        result = eval(entry.get())  
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def clear():
    entry.delete(0, tk.END)


def backspace():
    current = entry.get()
    entry.delete(len(current)-1, tk.END)


root = tk.Tk()
root.title("Dark Mode Calculator")
root.geometry("400x600")


root.config(bg="#1A1A1A")

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#333333", fg="#F1C40F")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), bg="#27AE60", fg="white", command=calculate)
    elif text in ['+', '-', '*', '/']:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), bg="#E74C3C", fg="white", command=lambda value=text: button_click(value))
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), bg="#34495E", fg="white", command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)


clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), bg="#C0392B", fg="white", command=clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

backspace_button = tk.Button(root, text="⌫", width=5, height=2, font=("Arial", 18), bg="#9B59B6", fg="white", command=backspace)
backspace_button.grid(row=5, column=1, padx=5, pady=5)


root.mainloop()

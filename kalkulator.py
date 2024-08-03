# wcale nie z tutoriala HIHI ^_^ :3

import tkinter as tk

def append_to_expression(value):
    current_text = expression.get()
    expression.set(current_text + value)

def clear_expression():
    expression.set("")

def calculate_result():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("Chuj")

root = tk.Tk()
root.title("Kalkulator przyszłośći")

expression = tk.StringVar()

entry = tk.Entry(root, textvariable=expression, font=("Arial", 16), relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == 'C':
        btn = tk.Button(root, text=button, font=("Arial", 16), command=clear_expression)
    elif button == '=':
        btn = tk.Button(root, text=button, font=("Arial", 16), command=calculate_result)
    else:
        btn = tk.Button(root, text=button, font=("Arial", 16), command=lambda b=button: append_to_expression(b))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()


# nwm co dalej robić
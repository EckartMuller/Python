import tkinter as tk

def on_button_click(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Hata")

root = tk.Tk()
root.title("Basit Hesap Makinesi")

# input kısmı
entry = tk.Entry(root, width=16, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# buyon

buttons = [

    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]



row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12),
              command=lambda b=button: on_button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# temizleme
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 12), command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

root.mainloop()
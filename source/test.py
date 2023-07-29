import tkinter as tk

def update_entry(key):
    entry_field.insert(tk.END, key)

def create_keyboard():
    keyboard_window = tk.Toplevel(root)
    keyboard_window.title("Keyboard")

    keys = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ]

    for row, key_row in enumerate(keys):
        for col, key in enumerate(key_row):
            btn = tk.Button(keyboard_window, text=key, width=5,
                            command=lambda k=key: update_entry(k))
            btn.grid(row=row, column=col, padx=5, pady=5)

# Main window
root = tk.Tk()
root.title("Keyboard Entry Example")

# Entry field
entry_field = tk.Entry(root)
entry_field.pack(padx=10, pady=10)

# Create multiple keyboards
keyboard_btn1 = tk.Button(root, text="Keyboard 1", command=create_keyboard)
keyboard_btn1.pack(pady=5)

keyboard_btn2 = tk.Button(root, text="Keyboard 2", command=create_keyboard)
keyboard_btn2.pack(pady=5)

root.mainloop()

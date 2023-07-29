
import tkinter as tk

class Fields(tk.Frame):
    def __init__(self, text, dim, master=None,password=None):
        super().__init__(master=master)
        self.text  = text
        self.dim = dim
        self.init_components(password)
        self.disp_components()

    def init_components(self, password):
        self.lb = tk.Label(master=self, text = self.text, font = ("Arial", 12))
        self.en = tk.Entry(master=self, width=self.dim,font = ("Arial", 12),justify='center')
    def disp_components(self):
        self.lb.grid(row=0, column=0, padx=3)
        self.en.grid(row=0, column=1, padx=3)

    def get_value(self):
        return str(self.en.get())
    
    def set_value(self, c):
        self.en.insert('end', c)
    
    def set_values(self, c):
        self.en.delete(0, tk.END)
        self.en.insert('end', c)

    def del_value(self):
        current_text = self.en.get()
        new_text = current_text[:-1]  # Remove the last character
        self.en.delete(tk.END, 0)       # Clear the entry
        self.en.insert(0, new_text)
        print(self.en.get())
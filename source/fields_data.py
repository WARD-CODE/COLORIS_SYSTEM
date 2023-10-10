
import tkinter as tk

class Fields(tk.Frame):
    def __init__(self, text, dim, master=None,password=None, contain=None):
        super().__init__(master=master)
        self.text  = text
        self.dim = dim
        self.contain = contain
        self.password = password
        self.init_components(password)
        self.disp_components()

    def init_components(self, password):
        self.lb = tk.Label(master=self, text = self.text, font = ("Arial", 14))
        if self.contain == "configuration":
           self.en = tk.Entry(master=self, width=self.dim,font = ("Arial", 40),justify='center')
        elif self.contain == "login":
           self.en = tk.Entry(master=self, width=self.dim,font = ("Arial", 40),justify='center')
        else:
           self.en = tk.Entry(master=self, width=self.dim,font = ("Arial", 23),justify='center')
        if self.password:
           self.en.configure(show="*")
 

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
        current_text = current_text[:-1]  # Remove the l
        self.set_values(current_text)
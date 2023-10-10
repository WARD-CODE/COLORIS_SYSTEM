import tkinter as tk
import string
from PIL import Image, ImageTk

class VkeyBoard(tk.Toplevel):
    
    def __init__(self, main_wind):
        super().__init__(
                        width = 500,
                        height = 300,
                        )
        
        self.resizable(False,False)        
        self.title("CLAVIER VIRTUEL")
        self.keys = []
        self.overrideredirect(True)
        self.attributes('-topmost',1)
        self.list_caracters = []
        self.list_letters = []
        self.main_wind = main_wind
        self.init_components()
        

        #display components
        self.disp_components()
    
    def init_components(self):
        self.letters_frame = tk.Frame(master=self)
        self.caracters_frame =tk.Frame(master=self)
        self.list_letters = ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n',':',' ','<--','hide']
        
        self.list_caracters = ['1','2','3','4','5','6','7','8','9','0','.','/']

        self.keys= []
        frames = self.letters_frame
        for lists in [self.list_letters,self.list_caracters]:
            length = len(lists)
            
            for k in range(length):
                
                if lists[k] == "<--":
                    
                    self.keys.append(tk.Button(master=self.letters_frame,
                                text=lists[k],
                                font=('Arial',20,"bold"),
                                background="white",
                                relief="groove",
                                command=self.delete_caract,
                                width=50,
                                height=60)
                                )
                    
                    image = Image.open("images/left.png")
                    self.keys[k].image = ImageTk.PhotoImage(image)
                    self.keys[k].configure(image=self.keys[k].image)
                    self.keys[k].configure(text="")

                elif lists[k] == "hide":
                    
                    self.keys.append(tk.Button(master=self.letters_frame,
                                text=lists[k],
                                font=('Arial',20,"bold"),
                                background="white",
                                relief="groove",
                                command=self.hide_keyboard,
                                width=50,
                                height=60)
                                )
                    
                    image = Image.open("images/manual.png")
                    self.keys[k].image = ImageTk.PhotoImage(image)
                    self.keys[k].configure(image=self.keys[k].image)
                    self.keys[k].configure(text="")

        
                    continue
                else:
                    self.keys.append(tk.Button(master=frames,
                                                text=lists[k],
                                                font=('Arial',20,"bold"),
                                                background="white",
                                                relief="groove",
                                                command=lambda c=lists[k]:self.insert_caract(c),
                                                width=2,
                                                height=2)
                                                )
            frames = self.caracters_frame


    def disp_components(self):

        self.letters_frame.pack(side='left')
        self.caracters_frame.pack(side='right', padx=15)

        length = len(self.list_letters)
        i=0
        for x in range(0,3):
            for y in range(0,10):
                if i < length:
                    self.keys[i].grid(row = x, column = y, padx = 2, pady=2)
                    i+=1

        length = len(self.list_caracters)

        for x in range(0,3):
            for y in range(0,4):
                if i < 32 + length:
                    self.keys[i].grid(row = x, column = y, padx = 2, pady=2)
                    i+=1

    def insert_caract(self,c):
        self.main_wind.focused_entry.set_value(str(c))
    
    def delete_caract(self):
        self.main_wind.focused_entry.del_value()

    def hide_keyboard(self):
        self.destroy()
        
    def show_keyboard(self):
        self.geometry("+{a}+{b}".format(a =10,b = 400))

      
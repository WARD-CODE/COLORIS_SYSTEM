
import tkinter as tk
from fields_data import Fields
from PIL import Image, ImageTk
from vkeyboard import VkeyBoard
from tkinter import messagebox
from about import AboutWindow
import re

class LoginWindow(tk.Toplevel):

    
    def __init__(self):
        super().__init__()
        self.geometry("800x580+502+352")
        self.resizable(False, False)
        self.title("LOGIN")
        self.minsize(120, 1)
        self.maxsize(785, 580)
        self.attributes('-fullscreen', True)
        self.overrideredirect(True)
        self.geometry(f"+{10}+{10}")
        self.components = {}
        self.keyboard = None
        
        self.focused_entry=None
        self.focused_entry_old = None
        
        self.init_components()
        self.disp_components()

    def init_components(self):
        self.components["header"] = tk.Label(master=self,text = "")
        image = Image.open("images/COLORISLOGO.png").resize((400, 220))
        self.components["header"].image = ImageTk.PhotoImage(image)
        self.components["header"].configure(image=self.components["header"].image)
       
        self.components["authentif"] = tk.Label(master=self,text = "etat d'Authentification",wraplength=200,font=("Arial", 12,"bold"))

        self.components["frame_1"]= tk.LabelFrame(master=self,text = "AUTHENTIFICATION", width=240,height=330)

        #Frame 1


        self.components["user"] = Fields(master=self.components["frame_1"],text = "     Utilisateur ",dim=12, contain="login")
        self.components["password"] = Fields(master=self.components["frame_1"],text = "Mot de passe ",dim=12, contain="login", password=True)
        self.components["user"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["user"]))
        self.components["password"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["password"]))   

        self.components["connecter"] = tk.Button(master=self, text="Connecter",font=("Arial",18,"bold"), width=8, height=3,foreground = "white",background="#51B8F9",command=self.on_connect) 

        self.components["login"] = tk.Label(master=self,text = "")
        image = Image.open("images/login.png").resize((80, 80))
        self.components["login"].image = ImageTk.PhotoImage(image)
        self.components["login"].configure(image=self.components["login"].image)  

        self.logo = tk.Button(self)
        image = Image.open("images/radisoft_logo.jpg").resize((80, 100))
        self.logo.image = ImageTk.PhotoImage(image)
        self.logo.configure(image=self.logo.image)
        self.logo.configure(command=self.on_about)
        self.logo.place(relx=0.88, rely=0.78, height=100, width=80)         
        self.logo.configure(background="#F7F7F7",borderwidth="0",relief="flat")

        self.components["user"].set_values("radisoft")
        self.components["password"].set_values("laboratoire")


    def disp_components(self):

        self.components["header"].place(relx=0.26,rely=0.09) 
        self.components["frame_1"].place(relx=0.28, rely=0.45)
               
        self.components["user"].grid(row=0,column=0, pady=5)
        self.components["password"].grid(row=1,column=0, pady=5)
        self.components["authentif"].place(relx=0.3, rely=0.73)
        self.components["connecter"].place(relx=0.7, rely=0.73)
        self.components["login"].place(relx=0.16,rely=0.48)
        self.logo.place(relx=0.87,rely=0.04)

    def on_about(self):
        info_string = '''
            Entreprise RADISOFT
           All rights reserved (C)

                     Contact:
         ___________________________

                      Email:
                     -------
        elmokhtaritoufik@gmail.com
        ___________________________

                      Phone:
                     --------
     (+213)552953456 / 770598641
       ___________________________
                                          '''
        return AboutWindow(info_string)
    
    def zone_clicked(self,entry_widget):

        self.focused_entry = entry_widget
        if str(self.focused_entry) != str(self.focused_entry_old):
            self.focused_entry_old = self.focused_entry
            if self.keyboard is None:
               self.keyboard= VkeyBoard(self)
            self.keyboard.destroy()
            self.keyboard= VkeyBoard(self)
            self.keyboard.show_keyboard()
            
            
        

    def on_connect(self):                                    
        if self.components["user"].get_value() =="radisoft" and self.components["password"].get_value() == "laboratoire":
           self.components["authentif"].configure(text = "Bienvenu!",foreground = "green" )
           if self.keyboard is not None:
              self.keyboard.hide_keyboard()

           self.destroy()
        else:
           self.components["authentif"].configure(text = "Utilisateur ou mot de passe incorrect")
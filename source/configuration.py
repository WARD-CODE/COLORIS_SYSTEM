
import tkinter as tk
from fields_data import Fields
from PIL import Image, ImageTk
from vkeyboard import VkeyBoard
from tkinter import messagebox
from database import save_config, load_config
import re

class ConfigWindow(tk.Toplevel):

    
    def __init__(self, main_wind):
        super().__init__()
        self.geometry("800x580+502+352")
        self.resizable(False, False)
        self.title("CONFIGURATION")
        self.minsize(120, 1)
        self.maxsize(782, 580)
        self.attributes('-fullscreen', True)
        self.overrideredirect(True)
        self.geometry(f"+{10}+{10}")
        self.keyboard = None
        self.components = {}
        self.main_wind = main_wind
        self.focused_entry=None
        self.focused_entry_old = None
        
        
        self.init_components()
        self.disp_components()

    def init_components(self):
        
        self.components["top"] = tk.Label(master=self,text = "BLOC DE CONFIGURATION", font=("Arial", 20,"bold"))
        self.components["frame_1"]= tk.LabelFrame(master=self,text = "MOUVEMENT HORIZONTAL", width=200,height=330,font=("Arial", 15,"bold"))
        self.components["frame_2"]= tk.LabelFrame(master=self,text = "MOUVEMENT VERTICAL", width=200,height=330,font=("Arial", 15,"bold"))
        self.components["frame_manuel1"]= tk.LabelFrame(master=self,text = "CONTROL MANUEL", width=220,height=200,font=("Arial", 13,"bold"))
        self.components["frame_manuel2"]= tk.LabelFrame(master=self,text = "CONTROL MANUEL", width=220,height=200,font=("Arial", 13,"bold"))

        #Frame 1
        self.components["unite1"] = Fields(master=self.components["frame_1"],text = "Unite(mm)      ",dim=8, contain="configuration")
        self.components["distance1"] = Fields(master=self.components["frame_1"],text = "Distance(mm) ",dim=8, contain="configuration")
        self.components["largeur1"] = Fields(master=self.components["frame_1"],text = "Largeur(mm)   ",dim=8, contain="configuration")

        self.components["unite1"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["unite1"]))
        self.components["distance1"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["distance1"]))
        self.components["largeur1"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["largeur1"]))
	
        self.components["img1"] =tk.Label(master=self, text="")
        image = Image.open("images/motor.png").resize((100, 100))
        self.components["img1"].image = ImageTk.PhotoImage(image)
        self.components["img1"].configure(image=self.components["img1"].image)  

        # # FRAME 2
        
        self.components["unite2"] = Fields(master=self.components["frame_2"],text = "Unite(mm)        ",dim=8, contain="configuration")
        self.components["distance2"] = Fields(master=self.components["frame_2"],text = "Distance(mm)   ",dim=8, contain="configuration")
        self.components["vib2"] = Fields(master=self.components["frame_2"],text = "Distillation(mm) ",dim=8, contain="configuration")

        self.components["unite2"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["unite2"]))
        self.components["distance2"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["distance2"]))
        self.components["vib2"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["vib2"]))

        self.components["valider"] = tk.Button(master=self, text="Valider",font=("Arial",20,"bold"), width=9, height=3,background="#51B8F9",command=self.on_valid) 

        self.components["avancer1"] = tk.Button(master=self.components["frame_manuel1"],text="Avant",font=("Arial",17,"bold"), width=12, height=3,background="#51B8F9",command=self.on_avance1)
        self.components["reculer1"] = tk.Button(master=self.components["frame_manuel1"], text="Arriere",font=("Arial",17,"bold"), width=12, height=3,background="#51B8F9",command=self.on_recule1) 
 	
        self.components["avancer2"] = tk.Button(master=self.components["frame_manuel2"],text="Haut",font=("Arial",17,"bold"), width=13, height=3,background="#51B8F9",command=self.on_avance2)
        self.components["reculer2"] = tk.Button(master=self.components["frame_manuel2"], text="Bas",font=("Arial",17,"bold"), width=13, height=3,background="#51B8F9",command=self.on_recule2) 
	
        self.components["unite1"].set_value(load_config("M1")[0])
        self.components["distance1"].set_value(load_config("M1")[1])
        self.components["largeur1"].set_value(load_config("M1")[2])

        self.components["unite2"].set_value(load_config("M2")[0])
        self.components["distance2"].set_value(load_config("M2")[1])
        self.components["vib2"].set_value(load_config("M2")[2])
     

    def disp_components(self):

        self.components["frame_1"].place(relx=0.02, rely=0.33)
        self.components["frame_2"].place(relx=0.51, rely=0.33)
        self.components["frame_manuel1"].place(relx=0.025, rely=0.73)
        self.components["frame_manuel2"].place(relx=0.51, rely=0.73)
        self.components["img1"].place(relx=0.16, rely=0.12)

        self.components["top"].place(relx=0.05, rely=0.05)

        self.components["unite1"].grid(row=0, column=0, pady=4)
        self.components["distance1"].grid(row=1, column=0, pady=4)
        self.components["largeur1"].grid(row=2, column=0, pady=4)

        self.components["unite2"].grid(row=0, column=0, pady=4)
        self.components["distance2"].grid(row=1, column=0, pady=4)
        self.components["vib2"].grid(row=2, column=0, pady=4)

        self.components["avancer1"].grid(row=0, column=1, padx=4,pady=4)
        self.components["reculer1"].grid(row=0, column=0, padx=4,pady=4)
        self.components["avancer2"].grid(row=0, column=1, padx=4,pady=4)
        self.components["reculer2"].grid(row=0, column=0, padx=4,pady=4)

        self.components["valider"].place(relx=0.8, rely=0.05, width=120, height=80)
      
    
    def zone_clicked(self,entry_widget):

        self.focused_entry = entry_widget
        if str(self.focused_entry) != str(self.focused_entry_old):
            self.focused_entry_old = self.focused_entry
            if self.keyboard is None:
               self.keyboard= VkeyBoard(self)
            self.keyboard.destroy()
            self.keyboard= VkeyBoard(self)
            self.keyboard.show_keyboard()
            

    
    def validation(self):
        for k in [self.components["unite1"], self.components["unite2"],self.components["distance1"],self.components["distance2"],self.components["largeur1"],self.components["vib2"]]:
            
            if str(k.get_value()).isspace() and not str(k.get_value()).isalpha():
                messagebox.showwarning("champ incorrect","verifier l'etat des champs")
                return False
            
        return True    

               
    def on_valid(self):
        data = []
        for k in [self.components["unite1"], self.components["distance1"],self.components["largeur1"]]:
            data.append(k.get_value())
        
        
        save_config(data,"M1")
        data = []
        for k in [self.components["unite2"], self.components["distance2"],self.components["vib2"]]:
            data.append(k.get_value())

        save_config(data,"M2")

        self.main_wind.M1.config(distance = int(self.components["distance1"].get_value()),
                                 largeur = int(self.components["largeur1"].get_value()),
                                 unite = int(self.components["unite1"].get_value()),
                                 vibration = 0)

        self.main_wind.M2.config(distance = int(self.components["distance2"].get_value()),
                                 largeur = 0,
                                 unite = int(self.components["unite2"].get_value()),
                                 vibration = int(self.components["vib2"].get_value())
                                 )

        if self.keyboard is not None:
           self.keyboard.hide_keyboard()
        
        self.destroy()

    def on_recule1(self):
        self.main_wind.M1.backward(int(self.components["unite1"].get_value()))

    def on_avance1(self):
        self.main_wind.M1.forward(int(self.components["unite1"].get_value()))

    def on_recule2(self):
        self.main_wind.M2.backward(int(self.components["unite2"].get_value()))

    def on_avance2(self):
        self.main_wind.M2.forward(int(self.components["unite2"].get_value()))
 
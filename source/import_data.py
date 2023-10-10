
from ast import Delete
import tkinter as tk
from fields_data import Fields
from PIL import Image, ImageTk
from vkeyboard import VkeyBoard
from tkinter import messagebox
from database import add_data,retrieve_data, modify
import re

class ImportWindow(tk.Toplevel):
    _PROGRAM_DATA = None
    _SELECTED_PROGRAM_NAME = None
    _SELECTED_PROGRAM = None
    _SELECTED_TIMERS=None

    
    def __init__(self, main_wind):
        super().__init__()
        self.geometry("800x580+502+352")
        self.resizable(False, False)
        self.title("PROGRAMMATION")
        self.minsize(120, 1)
        self.maxsize(785, 580)
        self.attributes('-fullscreen', True)
        self.overrideredirect(True)
        self.geometry(f"+{10}+{10}")
        self.components = {}
        self.keyboard = None
        self.main_wind = main_wind
        self.focused_entry=None
        self.focused_entry_old = None
        
        self.init_components()
        self.disp_components()
        self.proglist_init()

    def init_components(self):
        
        self.components["top"] = tk.Label(master=self,text = "BLOC DE PROGRAMMATION", font=("Arial", 20,"bold"))
        self.components["frame_1"]= tk.LabelFrame(master=self,text = "PROGRAMMES", width=280,height=366,font=("Arial", 17,"bold"))
        self.components["frame_2"]= tk.LabelFrame(master=self,text = "CONFIGURATION", width=430,height=460,font=("Arial", 17,"bold"))
        self.components["temp_frame"] = tk.Frame(master=self.components["frame_2"])
        #Frame 1
        self.UP_BUT = tk.Button(self.components["frame_1"],width=35,height=60)
        image = Image.open("images/UPLIST.png")
        self.UP_BUT.image = ImageTk.PhotoImage(image)
        self.UP_BUT.configure(image=self.UP_BUT.image)
        self.UP_BUT.configure(command=self.scroll_up)

        self.DOWN_BUT = tk.Button(self.components["frame_1"],width=35,height=60)        
        image = Image.open("images/DOWNLIST.png")
        self.DOWN_BUT.image = ImageTk.PhotoImage(image)
        self.DOWN_BUT.configure(image=self.DOWN_BUT.image)
        self.DOWN_BUT.configure(command=self.scroll_down)

        self.PROG_LIST = tk.Listbox(master=self.components["frame_1"],font=("Arial",17),width=18,height=10)

        self.SELECT_BUT = tk.Button(master = self.components["frame_1"],text='''Choisir''',font=("Arial",20,"bold"), width=15, height=4,background="#51B8F9",command=self.on_choisir)
    
        # # FRAME 2
        self.components["title"] = Fields(master=self.components["frame_2"],text = "Titre ",dim=20)
        self.components["date"] = Fields(master=self.components["frame_2"],text = "Date ",dim=20)

        self.components["title"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["title"]))
        self.components["date"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["date"]))   
        self.components["vibration"] = Fields(master=self.components["frame_2"],text = "Destillation",dim=5)
        self.components["vibration"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["vibration"]))
        self.components["message"] = tk.Label(master=self,text = "Log:Chosir, ajouter et modifier un programme",wraplength=300, font=("Arial", 15,"bold"))

        for h in range(1,13):
            self.components["C{}".format(h)] = Fields(master=self.components["temp_frame"],text = "C{}".format(h),dim=6)


        self.components["C1".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C1".format(h)]))
        self.components["C2".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C2".format(h)]))
        self.components["C3".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C3".format(h)]))
        self.components["C4".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C4".format(h)]))
        self.components["C5".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C5".format(h)]))
        self.components["C6".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C6".format(h)]))
        self.components["C7".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C7".format(h)]))
        self.components["C8".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C8".format(h)]))
        self.components["C9".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C9".format(h)]))
        self.components["C10".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C10".format(h)]))
        self.components["C11".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C11".format(h)]))
        self.components["C12".format(h)].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["C12".format(h)]))

        self.components["Ajouter"] = tk.Button(master=self.components["frame_2"], text="Ajouter",font=("Arial",20,"bold"), width=8, height=2,background="#51B8F9",command=self.on_ajouter) 
        self.components["modefier"] = tk.Button(master=self.components["frame_2"], text="Modefier",font=("Arial",20,"bold"), width=8, height=2,background="#51B8F9",command=self.on_modefier)

        self.components["valider"] = tk.Button(master=self, text="Valider",font=("Arial",20,"bold"), width=8, height=2,background="#51B8F9",command=self.on_valid) 


    def disp_components(self):
        self.components["frame_1"].place(relx=0.03, rely=0.3)
        self.components["frame_2"].place(relx=0.42, rely=0.15)
        self.components["temp_frame"].place(relx=0.01, rely=0.28)
        self.UP_BUT.place(relx=0.8, rely=0.02)
        self.DOWN_BUT.place(relx=0.8, rely=0.5)
        self.PROG_LIST.place(relx=0, rely=0)
        self.SELECT_BUT.place(relx=0.52, rely=0.74,height=80, width=120, bordermode='ignore')
        self.components["top"].place(relx=0.05, rely=0.05)

        self.components["C1"].grid(row=2, column=0, pady=4)
        self.components["C2"].grid(row=2, column=1, pady=4)
        self.components["C3"].grid(row=2, column=2, pady=4)
        self.components["C4"].grid(row=3, column=0, pady=4)
        self.components["C5"].grid(row=3, column=1, pady=4)
        self.components["C6"].grid(row=3, column=2, pady=4)
        self.components["C7"].grid(row=4, column=0, pady=4)
        self.components["C8"].grid(row=4, column=1, pady=4)
        self.components["C9"].grid(row=4, column=2, pady=4)
        self.components["C10"].grid(row=5, column=0, pady=4)
        self.components["C11"].grid(row=5, column=1, pady=4)
        self.components["C12"].grid(row=5, column=2, pady=4)

        self.components["vibration"].place(relx=0, rely=0.68)

        self.components["Ajouter"].place(relx=0.4, rely=0.79,height=80, width=120)
        self.components["modefier"].place(relx=0.7,rely=0.79,height=80, width=120)
        self.components["valider"].place(relx=0.82, rely=0.02,height=70, width=120)
        self.components["title"].place(relx=0.03, rely=0.03)
        self.components["date"].place(relx=0.025, rely=0.15)
        self.components["message"].place(relx=0.02, rely=0.15)

    
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
        time_pathern = r'^\d{2}:\d{2}$'
        for k in [self.components["title"], self.components["date"]]:
            
            
            if str(k.get_value()).isspace():
                self.components["message"].configure(text = "Log : verifier l'état des champs",font=("Arial",12,"bold"),foreground="red")
                return False
            
        for i in range(1,13):
            if not bool(re.match(time_pathern,str(self.components["C{}".format(i)].get_value()))):
                self.components["message"].configure(text="Log : verifier le format des temporisteurs (mm:ss)",font=("Arial",12,"bold"),foreground="red")
                return False

        return True
    
    def on_choisir(self):
        
        self.cur_index = self.PROG_LIST.curselection()
        for i in range(self.PROG_LIST.size()):
            self.PROG_LIST.itemconfig(i, {'bg': 'white'})
        if self.cur_index:
            self._SELECTED_PROGRAM_NAME = self.PROG_LIST.get(self.cur_index[0])
            self.PROG_LIST.itemconfig(self.cur_index, {'bg': 'yellow'})

        for prg in self._PROGRAM_DATA:
            if prg[0]==self._SELECTED_PROGRAM_NAME:
                self._SELECTED_PROGRAM = prg
                
                self.components["title"].set_values(prg[0])
                self.components["date"].set_values(prg[1])

                for i in range(1,13):
                    self.components["C{}".format(i)].set_values(prg[i+1])

                self.components["vibration"].set_values(prg[14])
                break
        self.components["message"].configure(text="Log : programme choisi: {}".format(str(self._SELECTED_PROGRAM_NAME)),foreground="green")  

    def on_ajouter(self):
        if self.validation():
            self.components["message"].configure(text="Log : programme ajoute avec succes",foreground="green")
            sequence = [
                self.components["title"].get_value(),
                self.components["date"].get_value(),
            ]
            for i in range(1, 13):
                sequence.append(self.components["C{}".format(i)].get_value())

            sequence.append(self.components["vibration"].get_value())
            add_data(sequence)
            self.proglist_init()

    def on_modefier(self):
        if self.validation():
            sequence = [
                self.components["title"].get_value(),
                self.components["date"].get_value(),
            ]
            for i in range(1, 13):
                sequence.append(self.components["C{}".format(i)].get_value())

            modify(self.cur_index[0],sequence)
            self.proglist_init()

               
    def on_valid(self):
        if self._SELECTED_PROGRAM and self.validation():
            
            self._SELECTED_TIMERS = retrieve_data(self._SELECTED_PROGRAM_NAME)
            self.main_wind.timers_data = self._SELECTED_TIMERS[:12]
            self.main_wind.CONT1_TIME.configure(text=self._SELECTED_TIMERS[0], font=('Arial',12,'bold'))
            self.main_wind.CONT2_TIME.configure(text=self._SELECTED_TIMERS[1], font=('Arial',12,'bold'))
            self.main_wind.CONT3_TIME.configure(text=self._SELECTED_TIMERS[2], font=('Arial',12,'bold'))
            self.main_wind.CONT4_TIME.configure(text=self._SELECTED_TIMERS[3], font=('Arial',12,'bold'))
            self.main_wind.CONT5_TIME.configure(text=self._SELECTED_TIMERS[4], font=('Arial',12,'bold'))
            self.main_wind.CONT6_TIME.configure(text=self._SELECTED_TIMERS[5], font=('Arial',12,'bold'))
            self.main_wind.CONT7_TIME.configure(text=self._SELECTED_TIMERS[6], font=('Arial',12,'bold'))
            self.main_wind.CONT8_TIME.configure(text=self._SELECTED_TIMERS[7], font=('Arial',12,'bold'))
            self.main_wind.CONT9_TIME.configure(text=self._SELECTED_TIMERS[8], font=('Arial',12,'bold'))
            self.main_wind.CONT10_TIME.configure(text=self._SELECTED_TIMERS[9], font=('Arial',12,'bold'))
            self.main_wind.CONT11_TIME.configure(text=self._SELECTED_TIMERS[10], font=('Arial',12,'bold'))
            self.main_wind.CONT12_TIME.configure(text=self._SELECTED_TIMERS[11], font=('Arial',12,'bold'))
            self.main_wind.VIBRATION_LAB.configure(text=self._SELECTED_TIMERS[12], font=('Arial',12,'bold'))
            self.main_wind.vibration_val = int(self._SELECTED_TIMERS[12])
            if self.keyboard is not None:
               self.keyboard.hide_keyboard()
            self.destroy()

    
    def scroll_up(self):
        self.PROG_LIST.yview_scroll(-1, "units")

    def scroll_down(self):
        self.PROG_LIST.yview_scroll(1, "units")


    def proglist_init(self):
        self._PROGRAM_DATA = retrieve_data("ALL")
        self.PROG_LIST.delete(0,tk.END)
        for row in self._PROGRAM_DATA:
            self.PROG_LIST.insert(tk.END,row[0])

    

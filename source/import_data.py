
from ast import Delete
import tkinter as tk
from source.fields_data import Fields
from PIL import Image, ImageTk
from vkeyboard import VkeyBoard
from tkinter import messagebox
from source.database import add_data,retrieve_data
import re

class ImportWindow(tk.Toplevel):
    _PROGRAM_DATA = None
    _SELECTED_PROGRAM_NAME = None
    _SELECTED_PROGRAM = None
    _SELECTED_TIMERS=None

    
    def __init__(self, main_wind):
        super().__init__()
        self.geometry("700x400+502+352")
        self.resizable(True, False)
        self.title("PROGRAMMATION")
        self.minsize(120, 1)
        self.maxsize(685, 570)
        self.components = {}
        self.keyboard= VkeyBoard(self)
        self.main_wind = main_wind
        self.focused_entry=None
        self.focused_entry_old = None
        
        self.init_components()
        self.disp_components()
        self.proglist_init()

    def init_components(self):
        
        self.components["top"] = tk.Label(master=self,text = "BLOC DE PROGRAMMATION", font=("Arial", 15,"bold"))
        self.components["frame_1"]= tk.LabelFrame(master=self,text = "PROGRAMMES", width=240,height=330)
        self.components["frame_2"]= tk.LabelFrame(master=self,text = "CONFIGURATION", width=400,height=330)
        self.components["temp_frame"] = tk.Frame(master=self.components["frame_2"])
        #Frame 1
        self.UP_BUT = tk.Button(self.components["frame_1"],width=16,height=50)
        image = Image.open("images/UPLIST.png")
        self.UP_BUT.image = ImageTk.PhotoImage(image)
        self.UP_BUT.configure(image=self.UP_BUT.image)
        self.UP_BUT.configure(command=self.scroll_up)

        self.DOWN_BUT = tk.Button(self.components["frame_1"],width=16,height=50)        
        image = Image.open("images/DOWNLIST.png")
        self.DOWN_BUT.image = ImageTk.PhotoImage(image)
        self.DOWN_BUT.configure(image=self.DOWN_BUT.image)
        self.DOWN_BUT.configure(command=self.scroll_down)

        self.PROG_LIST = tk.Listbox(master=self.components["frame_1"],font=("Arial",12),width=23,height=14)

        self.SELECT_BUT = tk.Button(master = self.components["frame_1"],text='''Choisir''',font=("Arial",11,"bold"), width=7, height=1,background="#51B8F9",command=self.on_choisir)
    
        # # FRAME 2
        self.components["title"] = Fields(master=self.components["frame_2"],text = "Titre ",dim=24)
        self.components["date"] = Fields(master=self.components["frame_2"],text = "Date ",dim=24)
        self.components["title"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["title"]))
        self.components["date"].bind("<FocusIn>", lambda event: self.zone_clicked(self.components["date"]))

        for h in range(1,11):
            self.components["C{}".format(h)] = Fields(master=self.components["temp_frame"],text = "C{}".format(h),dim=8)

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

        self.components["Ajouter"] = tk.Button(master=self.components["frame_2"], text="Ajouter",font=("Arial",12,"bold"), width=7, height=1,background="#51B8F9",command=self.on_ajouter) 
        self.components["clavier"] = tk.Button(master=self.components["frame_2"], width=70, height=40,relief='groove',background="white") 
        self.components["valider"] = tk.Button(master=self, text="Valider",font=("Arial",12,"bold"), width=7, height=1,background="#51B8F9",command=self.on_valid) 

        image = Image.open("images/clavier.png").resize((40, 40))
        self.components["clavier"].image = ImageTk.PhotoImage(image)
        self.components["clavier"].configure(image=self.components["clavier"].image)  
        self.components["clavier"].configure(command=self.open_keyboard)  


    def disp_components(self):
        self.components["frame_1"].place(relx=0.03, rely=0.15)
        self.components["frame_2"].place(relx=0.4, rely=0.15)
        self.components["temp_frame"].place(relx=0.03, rely=0.3)
        self.UP_BUT.place(relx=0.9, rely=0.07)
        self.DOWN_BUT.place(relx=0.9, rely=0.53)
        self.PROG_LIST.place(relx=0, rely=0)
        self.SELECT_BUT.place(relx=0.3, rely=0.87,height=40, width=74, bordermode='ignore')
        self.components["top"].place(relx=0.3, rely=0.05)

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

        self.components["Ajouter"].place(relx=0.32, rely=0.77)
        self.components["valider"].place(relx=0.85, rely=0.02)
        self.components["clavier"].place(relx=0.78, rely=0.025)
        self.components["title"].place(relx=0.03, rely=0.03)
        self.components["date"].place(relx=0.025, rely=0.15)

    
    def zone_clicked(self,entry_widget):

        self.focused_entry = entry_widget
        if str(self.focused_entry) != str(self.focused_entry_old):
            self.focused_entry_old = self.focused_entry
            self.keyboard.destroy()
            self.keyboard = VkeyBoard(self)
        
    def open_keyboard(self):
        return VkeyBoard(self)

    
    def validation(self):
        for k in [self.components["title"], self.components["date"]]:
            
            time_pathern = r'^\d{2}:\d{2}$'
            if str(k.get_value()).isspace():
                messagebox.showwarning("champ vide","verifier l'état des champs")
                return False
            
        for i in range(1,11):
            if not bool(re.match(time_pathern,str(self.components["C{}".format(i)].get_value()))):
                messagebox.showwarning("format incorrect","verifier le format des temporisteurs (mm:ss)")
                return False

            return True
    
    def on_choisir(self):
        
        cur_index = self.PROG_LIST.curselection()
        for i in range(self.PROG_LIST.size()):
            self.PROG_LIST.itemconfig(i, {'bg': 'white'})
        if cur_index:
            self._SELECTED_PROGRAM_NAME = self.PROG_LIST.get(cur_index[0])
            self.PROG_LIST.itemconfig(cur_index, {'bg': 'yellow'})

        for prg in self._PROGRAM_DATA:
            if prg[0]==self._SELECTED_PROGRAM_NAME:
                self._SELECTED_PROGRAM = prg
                
                self.components["title"].set_values(prg[0])
                self.components["date"].set_values(prg[1])

                for i in range(1,11):
                    self.components["C{}".format(i)].set_values(prg[i+1])
                break

    def on_ajouter(self):
        if self.validation():
            sequence = [
                self.components["title"].get_value(),
                self.components["date"].get_value(),
            ]
            for i in range(1, 11):
                sequence.append(self.components["C{}".format(i)].get_value())
            
            add_data(sequence)
            self.proglist_init()
    
    def on_valid(self):
        if self._SELECTED_PROGRAM:

            self._SELECTED_TIMERS = retrieve_data(self._SELECTED_PROGRAM_NAME)
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

    
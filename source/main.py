#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.constants import *
from PIL import Image, ImageTk
from database import add_data, retrieve_data

class COLORISsystem(tk.Tk):
    _MODE = None #mode manuel or automatic
    _MACHINE_STAT = None #STOP or INWORK
    _KEYBOARD_STAT = None
    _PROGRAM_DATA = None
    _SELECTED_PROGRAM_NAME = None
    _SELECTED_PROGRAM = None
    

    def __init__(self,*args, **kwargs):             
        super().__init__(*args,**kwargs)
        self.WinConfig()
        self.timer=None
        self.init_components()
        self.proglist_init()
        

    def mode_auto(self):
        self._MODE = "automatic"
        self._KEYBOARD_STAT = False

    def mode_manuel(self):
        self._MODE = "manuel"
        self._KEYBOARD_STAT = True
    
    def stop_machine(self):
        self._MACHINE_STAT = False

    def start_machine(self):
        self._MACHINE_STAT = True

    def proglist_init(self):
        self._PROGRAM_DATA = retrieve_data()
        for row in self._PROGRAM_DATA:
            self.PROG_LIST.insert(tk.END,row[0])

    def proglist_select(self):
        cur_index = self.PROG_LIST.curselection()
        for i in range(self.PROG_LIST.size()):
            self.PROG_LIST.itemconfig(i, {'bg': 'white'})
        if cur_index:
            self._SELECTED_PROGRAM_NAME = self.PROG_LIST.get(cur_index[0])
            self.PROG_LIST.itemconfig(cur_index, {'bg': 'yellow'})

            for prg in self._PROGRAM_DATA:
                if prg[0]==self._SELECTED_PROGRAM_NAME:
                    self._SELECTED_PROGRAM = prg
                    
                    self.CONT1_TIME.configure(text=self.sec_to_min(prg[2]))
                    self.CONT2_TIME.configure(text=self.sec_to_min(prg[3]))
                    self.CONT3_TIME.configure(text=self.sec_to_min(prg[4]))
                    self.CONT4_TIME.configure(text=self.sec_to_min(prg[5]))
                    self.CONT5_TIME.configure(text=self.sec_to_min(prg[6]))
                    self.CONT6_TIME.configure(text=self.sec_to_min(prg[7]))
                    self.CONT7_TIME.configure(text=self.sec_to_min(prg[8]))
                    self.CONT8_TIME.configure(text=self.sec_to_min(prg[9]))
                    self.CONT9_TIME.configure(text=self.sec_to_min(prg[10]))
                    self.CONT10_TIME.configure(text=self.sec_to_min(prg[11]))
                    break
                    
    def update_timers(self):
        if self.timer> 0:
            self.timer -= 1
            self.CONT1_TIME.config(text=self.sec_to_min(self.timer))
        self.after(1000, self.update_timers)

    def start_countdown(self, number):

        if self.timer is not None and self.timer > 0:
            return

        self.timer = int(self._SELECTED_PROGRAM[number])
        self.update_timers()
        
    def sec_to_min(self,seconds):
        minutes, secs = divmod(int(seconds), 60)
        return f"{minutes:02d}:{secs:02d}"

    def WinConfig(self):
        self.geometry("800x480+502+352")
        self.minsize(120, 1)
        self.maxsize(785, 570)
        self.resizable(1, 1)
        self.title("COLORIS SYSTEM")
        self.configure(background="#ebebeb")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

    def init_components(self):

        self.containers_init()
        self.controle_init()
        self.programmes_init()
        self.porteuse_init()
        self.horloge_init()
        self.generale_init()

    def containers_init(self):

        self.CONTENEURS_FRAME = tk.LabelFrame(self)
        self.CONTENEURS_FRAME.place(relx=0.251, rely=0.208, relheight=0.521, relwidth=0.74)
        self.CONTENEURS_FRAME.configure(relief='groove')
        self.CONTENEURS_FRAME.configure(foreground="#000000")
        self.CONTENEURS_FRAME.configure(text='''CONTENEURS''')
        self.CONTENEURS_FRAME.configure(background="#e0e0e0")
        self.CONTENEURS_FRAME.configure(highlightbackground="#d9d9d9")
        self.CONTENEURS_FRAME.configure(highlightcolor="black")

        self.CONTIN_INDIC = tk.Canvas(self.CONTENEURS_FRAME)
        self.CONTIN_INDIC.place(relx=0.017, rely=0.392, relheight=0.084, relwidth=0.072, bordermode='ignore')
        self.CONTIN_INDIC.configure(background="#d9d9d9")
        self.CONTIN_INDIC.configure(borderwidth="2")
        self.CONTIN_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONTIN_INDIC.configure(highlightcolor="black")
        self.CONTIN_INDIC.configure(insertbackground="black")
        self.CONTIN_INDIC.configure(relief="ridge")
        self.CONTIN_INDIC.configure(selectbackground="#c4c4c4")
        self.CONTIN_INDIC.configure(selectforeground="black")

        self.CONTOUT_INDIC = tk.Canvas(self.CONTENEURS_FRAME)
        self.CONTOUT_INDIC.place(relx=0.017, rely=0.852, relheight=0.084, relwidth=0.072, bordermode='ignore')
        self.CONTOUT_INDIC.configure(background="#d9d9d9")
        self.CONTOUT_INDIC.configure(borderwidth="2")
        self.CONTOUT_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONTOUT_INDIC.configure(highlightcolor="black")
        self.CONTOUT_INDIC.configure(insertbackground="black")
        self.CONTOUT_INDIC.configure(relief="ridge")
        self.CONTOUT_INDIC.configure(selectbackground="#c4c4c4")
        self.CONTOUT_INDIC.configure(selectforeground="black")

        
        self.CONTIN_LABEL = tk.Label(self.CONTENEURS_FRAME)
        image = Image.open("images/DOWN.png").resize((50, 50))
        self.CONTIN_LABEL.image = ImageTk.PhotoImage(image)
        self.CONTIN_LABEL.configure(image=self.CONTIN_LABEL.image)

        self.CONTIN_LABEL.place(relx=0.017, rely=0.12, height=61, width=40, bordermode='ignore')
        self.CONTIN_LABEL.configure(activeforeground="#000000")
        self.CONTIN_LABEL.configure(background="#ffffff")
        self.CONTIN_LABEL.configure(compound='left')
        self.CONTIN_LABEL.configure(disabledforeground="#a3a3a3")
        self.CONTIN_LABEL.configure(foreground="#000000")
        self.CONTIN_LABEL.configure(highlightbackground="#d9d9d9")
        self.CONTIN_LABEL.configure(highlightcolor="black")



        self.CONTOUT_LABEL = tk.Label(self.CONTENEURS_FRAME)
        image = Image.open("images/UP.png").resize((50, 50))
        self.CONTOUT_LABEL.image = ImageTk.PhotoImage(image)
        self.CONTOUT_LABEL.configure(image=self.CONTOUT_LABEL.image)

        self.CONTOUT_LABEL.place(relx=0.019, rely=0.576, height=61, width=40, bordermode='ignore')
        self.CONTOUT_LABEL.configure(activeforeground="#000000")
        self.CONTOUT_LABEL.configure(background="#ffffff")
        self.CONTOUT_LABEL.configure(compound='left')
        self.CONTOUT_LABEL.configure(disabledforeground="#a3a3a3")
        self.CONTOUT_LABEL.configure(foreground="#000000")
        self.CONTOUT_LABEL.configure(highlightbackground="#d9d9d9")
        self.CONTOUT_LABEL.configure(highlightcolor="black")


        self.Frame1_2 = tk.Frame(self)
        self.Frame1_2.place(relx=0.332, rely=0.25, relheight=0.221, relwidth=0.651)
        self.Frame1_2.configure(relief='groove')
        self.Frame1_2.configure(borderwidth="2")
        self.Frame1_2.configure(relief="groove")
        self.Frame1_2.configure(background="#c0c0c0")
        self.Frame1_2.configure(highlightbackground="#d9d9d9")
        self.Frame1_2.configure(highlightcolor="black")

        self.CONT1_BUT = tk.Button(self.Frame1_2)
        self.CONT1_BUT.place(relx=0.012, rely=0.047, height=33, width=93)
        self.CONT1_BUT.configure(relief='groove')
        self.CONT1_BUT.configure(activeforeground="black")
        self.CONT1_BUT.configure(background="#d9d9d9")
        self.CONT1_BUT.configure(compound='left')
        self.CONT1_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT1_BUT.configure(foreground="#000000")
        self.CONT1_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT1_BUT.configure(highlightcolor="black")
        self.CONT1_BUT.configure(pady="0")
        self.CONT1_BUT.configure(text='''1''')
        

        self.CONT2_BUT = tk.Button(self.Frame1_2)
        self.CONT2_BUT.configure(relief='groove')
        self.CONT2_BUT.place(relx=0.209, rely=0.047, height=33, width=93)
        self.CONT2_BUT.configure(activeforeground="black")
        self.CONT2_BUT.configure(background="#d9d9d9")
        self.CONT2_BUT.configure(compound='left')
        self.CONT2_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT2_BUT.configure(foreground="#000000")
        self.CONT2_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT2_BUT.configure(highlightcolor="black")
        self.CONT2_BUT.configure(pady="0")
        self.CONT2_BUT.configure(text='''2''')

        self.CONT3_BUT = tk.Button(self.Frame1_2)
        self.CONT3_BUT.configure(relief='groove')
        self.CONT3_BUT.place(relx=0.407, rely=0.047, height=33, width=93)
        self.CONT3_BUT.configure(activeforeground="black")
        self.CONT3_BUT.configure(background="#d9d9d9")
        self.CONT3_BUT.configure(compound='left')
        self.CONT3_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT3_BUT.configure(foreground="#000000")
        self.CONT3_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT3_BUT.configure(highlightcolor="black")
        self.CONT3_BUT.configure(pady="0")
        self.CONT3_BUT.configure(text='''3''')

        self.CONT4_BUT = tk.Button(self.Frame1_2)
        self.CONT4_BUT.configure(relief='groove')
        self.CONT4_BUT.place(relx=0.609, rely=0.047, height=33, width=93)
        self.CONT4_BUT.configure(activeforeground="black")
        self.CONT4_BUT.configure(background="#d9d9d9")
        self.CONT4_BUT.configure(compound='left')
        self.CONT4_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT4_BUT.configure(foreground="#000000")
        self.CONT4_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT4_BUT.configure(highlightcolor="black")
        self.CONT4_BUT.configure(pady="0")
        self.CONT4_BUT.configure(text='''4''')

        self.CONT5_BUT = tk.Button(self.Frame1_2)
        self.CONT5_BUT.configure(relief='groove')
        self.CONT5_BUT.place(relx=0.806, rely=0.047, height=33, width=93)
        self.CONT5_BUT.configure(activeforeground="black")
        self.CONT5_BUT.configure(background="#d9d9d9")
        self.CONT5_BUT.configure(compound='left')
        self.CONT5_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT5_BUT.configure(foreground="#000000")
        self.CONT5_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT5_BUT.configure(highlightcolor="black")
        self.CONT5_BUT.configure(pady="0")
        self.CONT5_BUT.configure(text='''5''')


        self.CONT1_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT1_INDIC.place(relx=0.023, rely=0.726, relheight=0.198, relwidth=0.16)
        self.CONT1_INDIC.configure(background="#d9d9d9")
        self.CONT1_INDIC.configure(borderwidth="2")
        self.CONT1_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT1_INDIC.configure(highlightcolor="black")
        self.CONT1_INDIC.configure(insertbackground="black")
        self.CONT1_INDIC.configure(relief="ridge")
        self.CONT1_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT1_INDIC.configure(selectforeground="black")

        self.CONT2_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT2_INDIC.place(relx=0.219, rely=0.726, relheight=0.198, relwidth=0.16)
        self.CONT2_INDIC.configure(background="#d9d9d9")
        self.CONT2_INDIC.configure(borderwidth="2")
        self.CONT2_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT2_INDIC.configure(highlightcolor="black")
        self.CONT2_INDIC.configure(insertbackground="black")
        self.CONT2_INDIC.configure(relief="ridge")
        self.CONT2_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT2_INDIC.configure(selectforeground="black")

        self.CONT3_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT3_INDIC.place(relx=0.419, rely=0.736, relheight=0.198, relwidth=0.159)
        self.CONT3_INDIC.configure(background="#d9d9d9")
        self.CONT3_INDIC.configure(borderwidth="2")
        self.CONT3_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT3_INDIC.configure(highlightcolor="black")
        self.CONT3_INDIC.configure(insertbackground="black")
        self.CONT3_INDIC.configure(relief="ridge")
        self.CONT3_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT3_INDIC.configure(selectforeground="black")
        
        self.CONT4_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT4_INDIC.place(relx=0.617, rely=0.736, relheight=0.198, relwidth=0.159)
        self.CONT4_INDIC.configure(background="#d9d9d9")
        self.CONT4_INDIC.configure(borderwidth="2")
        self.CONT4_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT4_INDIC.configure(highlightcolor="black")
        self.CONT4_INDIC.configure(insertbackground="black")
        self.CONT4_INDIC.configure(relief="ridge")
        self.CONT4_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT4_INDIC.configure(selectforeground="black")

        self.CONT5_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT5_INDIC.place(relx=0.82, rely=0.736, relheight=0.198, relwidth=0.159)
        self.CONT5_INDIC.configure(background="#d9d9d9")
        self.CONT5_INDIC.configure(borderwidth="2")
        self.CONT5_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT5_INDIC.configure(highlightcolor="black")
        self.CONT5_INDIC.configure(insertbackground="black")
        self.CONT5_INDIC.configure(relief="ridge")
        self.CONT5_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT5_INDIC.configure(selectforeground="black")

        self.CONT1_TIME = tk.Label(self.Frame1_2)
        self.CONT1_TIME.place(relx=0.014, rely=0.406, height=31, width=90)
        self.CONT1_TIME.configure(activeforeground="#000000")
        self.CONT1_TIME.configure(background="#ffffff")
        self.CONT1_TIME.configure(compound='left')
        self.CONT1_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT1_TIME.configure(foreground="#000000")
        self.CONT1_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT1_TIME.configure(highlightcolor="black")
        self.CONT1_TIME.configure(relief="groove")
        self.CONT1_TIME.configure(text='''temps''')
        

        self.CONT2_TIME = tk.Label(self.Frame1_2)
        self.CONT2_TIME.place(relx=0.209, rely=0.406, height=31, width=91)
        self.CONT2_TIME.configure(activeforeground="#000000")
        self.CONT2_TIME.configure(background="#ffffff")
        self.CONT2_TIME.configure(compound='left')
        self.CONT2_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT2_TIME.configure(foreground="#000000")
        self.CONT2_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT2_TIME.configure(highlightcolor="black")
        self.CONT2_TIME.configure(relief="groove")
        self.CONT2_TIME.configure(text='''temps''')

        self.CONT3_TIME = tk.Label(self.Frame1_2)
        self.CONT3_TIME.place(relx=0.409, rely=0.406, height=31, width=90)
        self.CONT3_TIME.configure(activeforeground="#000000")
        self.CONT3_TIME.configure(background="#ffffff")
        self.CONT3_TIME.configure(compound='left')
        self.CONT3_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT3_TIME.configure(foreground="#000000")
        self.CONT3_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT3_TIME.configure(highlightcolor="black")
        self.CONT3_TIME.configure(relief="groove")
        self.CONT3_TIME.configure(text='''temps''')

        self.CONT4_TIME = tk.Label(self.Frame1_2)
        self.CONT4_TIME.place(relx=0.611, rely=0.406, height=31, width=90)
        self.CONT4_TIME.configure(activeforeground="#000000")
        self.CONT4_TIME.configure(background="#ffffff")
        self.CONT4_TIME.configure(compound='left')
        self.CONT4_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT4_TIME.configure(foreground="#000000")
        self.CONT4_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT4_TIME.configure(highlightcolor="black")
        self.CONT4_TIME.configure(relief="groove")
        self.CONT4_TIME.configure(text='''temps''')

        self.CONT5_TIME = tk.Label(self.Frame1_2)
        self.CONT5_TIME.place(relx=0.814, rely=0.406, height=31, width=90)
        self.CONT5_TIME.configure(activeforeground="#000000")
        self.CONT5_TIME.configure(background="#ffffff")
        self.CONT5_TIME.configure(compound='left')
        self.CONT5_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT5_TIME.configure(foreground="#000000")
        self.CONT5_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT5_TIME.configure(highlightcolor="black")
        self.CONT5_TIME.configure(relief="groove")
        self.CONT5_TIME.configure(text='''temps''')



        self.Frame1_1 = tk.Frame(self)
        self.Frame1_1.place(relx=0.332, rely=0.5, relheight=0.221, relwidth=0.651)
        self.Frame1_1.configure(relief='groove')
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(relief="groove")
        self.Frame1_1.configure(background="#c0c0c0")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")

        self.CONT6_BUT = tk.Button(self.Frame1_1)
        self.CONT6_BUT.configure(relief='groove')
        self.CONT6_BUT.place(relx=0.003, rely=0.047, height=33, width=93)
        self.CONT6_BUT.configure(activeforeground="black")
        self.CONT6_BUT.configure(background="#d9d9d9")
        self.CONT6_BUT.configure(compound='left')
        self.CONT6_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT6_BUT.configure(foreground="#000000")
        self.CONT6_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT6_BUT.configure(highlightcolor="black")
        self.CONT6_BUT.configure(pady="0")
        self.CONT6_BUT.configure(text='''6''')

        self.CONT7_BUT = tk.Button(self.Frame1_1)
        self.CONT7_BUT.configure(relief='groove')
        self.CONT7_BUT.place(relx=0.205, rely=0.047, height=33, width=93)
        self.CONT7_BUT.configure(activeforeground="black")
        self.CONT7_BUT.configure(background="#d9d9d9")
        self.CONT7_BUT.configure(compound='left')
        self.CONT7_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT7_BUT.configure(foreground="#000000")
        self.CONT7_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT7_BUT.configure(highlightcolor="black")
        self.CONT7_BUT.configure(pady="0")
        self.CONT7_BUT.configure(text='''7''')

        self.CONT8_BUT = tk.Button(self.Frame1_1)
        self.CONT8_BUT.configure(relief='groove')
        self.CONT8_BUT.place(relx=0.407, rely=0.047, height=33, width=93)
        self.CONT8_BUT.configure(activeforeground="black")
        self.CONT8_BUT.configure(background="#d9d9d9")
        self.CONT8_BUT.configure(compound='left')
        self.CONT8_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT8_BUT.configure(foreground="#000000")
        self.CONT8_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT8_BUT.configure(highlightcolor="black")
        self.CONT8_BUT.configure(pady="0")
        self.CONT8_BUT.configure(text='''8''')

        self.CONT9_BUT = tk.Button(self.Frame1_1)
        self.CONT9_BUT.configure(relief='groove')
        self.CONT9_BUT.place(relx=0.609, rely=0.047, height=33, width=93)
        self.CONT9_BUT.configure(activeforeground="black")
        self.CONT9_BUT.configure(background="#d9d9d9")
        self.CONT9_BUT.configure(compound='left')
        self.CONT9_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT9_BUT.configure(foreground="#000000")
        self.CONT9_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT9_BUT.configure(highlightcolor="black")
        self.CONT9_BUT.configure(pady="0")
        self.CONT9_BUT.configure(text='''9''')

        self.CONT10_BUT = tk.Button(self.Frame1_1)
        self.CONT10_BUT.configure(relief='groove')
        self.CONT10_BUT.place(relx=0.806, rely=0.047, height=33, width=93)
        self.CONT10_BUT.configure(activeforeground="black")
        self.CONT10_BUT.configure(background="#d9d9d9")
        self.CONT10_BUT.configure(compound='left')
        self.CONT10_BUT.configure(disabledforeground="#a3a3a3")
        self.CONT10_BUT.configure(foreground="#000000")
        self.CONT10_BUT.configure(highlightbackground="#d9d9d9")
        self.CONT10_BUT.configure(highlightcolor="black")
        self.CONT10_BUT.configure(pady="0")
        self.CONT10_BUT.configure(text='''10''')

        self.CONT6_INDIC = tk.Canvas(self.Frame1_1)
        self.CONT6_INDIC.place(relx=0.02, rely=0.726, relheight=0.198, relwidth=0.16)
        self.CONT6_INDIC.configure(background="#d9d9d9")
        self.CONT6_INDIC.configure(borderwidth="2")
        self.CONT6_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT6_INDIC.configure(highlightcolor="black")
        self.CONT6_INDIC.configure(insertbackground="black")
        self.CONT6_INDIC.configure(relief="ridge")
        self.CONT6_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT6_INDIC.configure(selectforeground="black")

        self.CONT7_INDIC = tk.Canvas(self.Frame1_1)
        self.CONT7_INDIC.place(relx=0.219, rely=0.726, relheight=0.198, relwidth=0.16)
        self.CONT7_INDIC.configure(background="#d9d9d9")
        self.CONT7_INDIC.configure(borderwidth="2")
        self.CONT7_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT7_INDIC.configure(highlightcolor="black")
        self.CONT7_INDIC.configure(insertbackground="black")
        self.CONT7_INDIC.configure(relief="ridge")
        self.CONT7_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT7_INDIC.configure(selectforeground="black")

        self.CONT8_INDIC = tk.Canvas(self.Frame1_1)
        self.CONT8_INDIC.place(relx=0.419, rely=0.726, relheight=0.198, relwidth=0.159)
        self.CONT8_INDIC.configure(background="#d9d9d9")
        self.CONT8_INDIC.configure(borderwidth="2")
        self.CONT8_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT8_INDIC.configure(highlightcolor="black")
        self.CONT8_INDIC.configure(insertbackground="black")
        self.CONT8_INDIC.configure(relief="ridge")
        self.CONT8_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT8_INDIC.configure(selectforeground="black")

        self.CONT9_INDIC = tk.Canvas(self.Frame1_1)
        self.CONT9_INDIC.place(relx=0.62, rely=0.726, relheight=0.198, relwidth=0.159)
        self.CONT9_INDIC.configure(background="#d9d9d9")
        self.CONT9_INDIC.configure(borderwidth="2")
        self.CONT9_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT9_INDIC.configure(highlightcolor="black")
        self.CONT9_INDIC.configure(insertbackground="black")
        self.CONT9_INDIC.configure(relief="ridge")
        self.CONT9_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT9_INDIC.configure(selectforeground="black")

        self.CONT10_INDIC = tk.Canvas(self.Frame1_1)
        self.CONT10_INDIC.place(relx=0.816, rely=0.736, relheight=0.198, relwidth=0.159)
        self.CONT10_INDIC.configure(background="#d9d9d9")
        self.CONT10_INDIC.configure(borderwidth="2")
        self.CONT10_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT10_INDIC.configure(highlightcolor="black")
        self.CONT10_INDIC.configure(insertbackground="black")
        self.CONT10_INDIC.configure(relief="ridge")
        self.CONT10_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT10_INDIC.configure(selectforeground="black")

        self.CONT6_TIME = tk.Label(self.Frame1_1)
        self.CONT6_TIME.place(relx=0.006, rely=0.406, height=31, width=92)
        self.CONT6_TIME.configure(activeforeground="#000000")
        self.CONT6_TIME.configure(background="#ffffff")
        self.CONT6_TIME.configure(compound='left')
        self.CONT6_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT6_TIME.configure(foreground="#000000")
        self.CONT6_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT6_TIME.configure(highlightcolor="black")
        self.CONT6_TIME.configure(relief="groove")
        self.CONT6_TIME.configure(text='''temps''')

        self.CONT7_TIME = tk.Label(self.Frame1_1)
        self.CONT7_TIME.place(relx=0.209, rely=0.406, height=31, width=91)
        self.CONT7_TIME.configure(activeforeground="#000000")
        self.CONT7_TIME.configure(background="#ffffff")
        self.CONT7_TIME.configure(compound='left')
        self.CONT7_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT7_TIME.configure(foreground="#000000")
        self.CONT7_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT7_TIME.configure(highlightcolor="black")
        self.CONT7_TIME.configure(relief="groove")
        self.CONT7_TIME.configure(text='''temps''')

        self.CONT8_TIME = tk.Label(self.Frame1_1)
        self.CONT8_TIME.place(relx=0.409, rely=0.406, height=31, width=90)
        self.CONT8_TIME.configure(activeforeground="#000000")
        self.CONT8_TIME.configure(background="#ffffff")
        self.CONT8_TIME.configure(compound='left')
        self.CONT8_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT8_TIME.configure(foreground="#000000")
        self.CONT8_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT8_TIME.configure(highlightcolor="black")
        self.CONT8_TIME.configure(relief="groove")
        self.CONT8_TIME.configure(text='''temps''')

        self.CONT9_TIME = tk.Label(self.Frame1_1)
        self.CONT9_TIME.place(relx=0.611, rely=0.406, height=31, width=90)
        self.CONT9_TIME.configure(activeforeground="#000000")
        self.CONT9_TIME.configure(background="#ffffff")
        self.CONT9_TIME.configure(compound='left')
        self.CONT9_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT9_TIME.configure(foreground="#000000")
        self.CONT9_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT9_TIME.configure(highlightcolor="black")
        self.CONT9_TIME.configure(relief="groove")
        self.CONT9_TIME.configure(text='''temps''')

        self.CONT10_TIME = tk.Label(self.Frame1_1)
        self.CONT10_TIME.place(relx=0.814, rely=0.406, height=31, width=90)
        self.CONT10_TIME.configure(activeforeground="#000000")
        self.CONT10_TIME.configure(background="#ffffff")
        self.CONT10_TIME.configure(compound='left')
        self.CONT10_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT10_TIME.configure(foreground="#000000")
        self.CONT10_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT10_TIME.configure(highlightcolor="black")
        self.CONT10_TIME.configure(relief="groove")
        self.CONT10_TIME.configure(text='''temps''')

    def controle_init(self):

        self.CONTROLE_FRAME = tk.LabelFrame(self)
        self.CONTROLE_FRAME.place(relx=0.668, rely=0.021, relheight=0.177, relwidth=0.321)
        self.CONTROLE_FRAME.configure(relief='groove')
        self.CONTROLE_FRAME.configure(foreground="#000000")
        self.CONTROLE_FRAME.configure(text='''CONTROLE''')
        self.CONTROLE_FRAME.configure(background="#e1e1e1")
        self.CONTROLE_FRAME.configure(highlightbackground="#d9d9d9")
        self.CONTROLE_FRAME.configure(highlightcolor="black")

        self.MANUEL_BUT = tk.Button(self.CONTROLE_FRAME)
        image = Image.open("images/manual.png").resize((50, 50))
        self.MANUEL_BUT.image = ImageTk.PhotoImage(image)
        self.MANUEL_BUT.configure(image=self.MANUEL_BUT.image)
        self.MANUEL_BUT.place(relx=0.04, rely=0.235, height=53, width=113, bordermode='ignore')
        self.MANUEL_BUT.configure(activeforeground="black")
        self.MANUEL_BUT.configure(background="#ffffff")
        self.MANUEL_BUT.configure(compound='left')
        self.MANUEL_BUT.configure(disabledforeground="#a3a3a3")
        self.MANUEL_BUT.configure(foreground="#000000")
        self.MANUEL_BUT.configure(highlightbackground="#d9d9d9")
        self.MANUEL_BUT.configure(highlightcolor="black")
        self.MANUEL_BUT.configure(padx="6")
        self.MANUEL_BUT.configure(pady="0")
        self.MANUEL_BUT.configure(text='''MANUEL''')
        self.MANUEL_BUT.configure(command=self.mode_manuel)

        self.AUTO_BUT = tk.Button(self.CONTROLE_FRAME)
        image = Image.open("images/automatique.png").resize((50, 50))
        self.AUTO_BUT.image = ImageTk.PhotoImage(image)
        self.AUTO_BUT.configure(image=self.AUTO_BUT.image)

        self.AUTO_BUT.place(relx=0.508, rely=0.235, height=53, width=113, bordermode='ignore')          
        self.AUTO_BUT.configure(activeforeground="black")
        self.AUTO_BUT.configure(background="#ffffff")
        self.AUTO_BUT.configure(compound='left')
        self.AUTO_BUT.configure(disabledforeground="#a3a3a3")
        self.AUTO_BUT.configure(foreground="#000000")
        self.AUTO_BUT.configure(highlightbackground="#d9d9d9")
        self.AUTO_BUT.configure(highlightcolor="black")
        self.AUTO_BUT.configure(padx="13")
        self.AUTO_BUT.configure(pady="0")
        self.AUTO_BUT.configure(text='''AUTO''')
        self.AUTO_BUT.configure(command=self.mode_auto)  

    def programmes_init(self):

        self.PROGRAMMES_FRAME = tk.LabelFrame(self)
        self.PROGRAMMES_FRAME.place(relx=0.008, rely=0.188, relheight=0.802, relwidth=0.232)
        self.PROGRAMMES_FRAME.configure(relief='groove')
        self.PROGRAMMES_FRAME.configure(foreground="#000000")
        self.PROGRAMMES_FRAME.configure(text='''PROGRAMMES''')
        self.PROGRAMMES_FRAME.configure(background="#d9d9d9")
        self.PROGRAMMES_FRAME.configure(highlightbackground="#d9d9d9")
        self.PROGRAMMES_FRAME.configure(highlightcolor="black")


        

        self.UP_BUT = tk.Button(self.PROGRAMMES_FRAME,width=16,height=50)
        self.UP_BUT.place(relx=0.88, rely=0.07)
        image = Image.open("images/UPLIST.png")
        self.UP_BUT.image = ImageTk.PhotoImage(image)
        self.UP_BUT.configure(image=self.UP_BUT.image)
        self.UP_BUT.configure(command=self.scroll_up)

        self.DOWN_BUT = tk.Button(self.PROGRAMMES_FRAME,width=16,height=50)
        self.DOWN_BUT.place(relx=0.88, rely=0.53)
        image = Image.open("images/DOWNLIST.png")
        self.DOWN_BUT.image = ImageTk.PhotoImage(image)
        self.DOWN_BUT.configure(image=self.DOWN_BUT.image)
        self.DOWN_BUT.configure(command=self.scroll_down)

        self.PROG_LIST = tk.Listbox(master=self.PROGRAMMES_FRAME,font=("Arial",10),width=22,height=16)
        self.PROG_LIST.place(relx=0, rely=0)

        self.SELECT_BUT = tk.Button(self.PROGRAMMES_FRAME)
        image = Image.open("images/choisir.png").resize((50, 50))
        self.SELECT_BUT.image = ImageTk.PhotoImage(image)
        self.SELECT_BUT.configure(image=self.SELECT_BUT.image)
        self.SELECT_BUT.place(relx=0.545, rely=0.787,height=74, width=77, bordermode='ignore')
        self.SELECT_BUT.configure(activeforeground="black")
        self.SELECT_BUT.configure(background="#d9d9d9")
        self.SELECT_BUT.configure(compound='top')
        self.SELECT_BUT.configure(disabledforeground="#a3a3a3")
        self.SELECT_BUT.configure(foreground="#000000")
        self.SELECT_BUT.configure(highlightbackground="#d9d9d9")
        self.SELECT_BUT.configure(highlightcolor="black")
        self.SELECT_BUT.configure(pady="0")
        self.SELECT_BUT.configure(text='''SELECT''')
        self.SELECT_BUT.configure(command=self.proglist_select)


        self.IMPORT_BUT = tk.Button(self.PROGRAMMES_FRAME)
        image = Image.open("images/import.png").resize((50, 50))
        self.IMPORT_BUT.image = ImageTk.PhotoImage(image)
        self.IMPORT_BUT.configure(image=self.IMPORT_BUT.image)  

        self.IMPORT_BUT.place(relx=0.038, rely=0.787, height=74, width=77, bordermode='ignore')
        self.IMPORT_BUT.configure(activeforeground="black")
        self.IMPORT_BUT.configure(background="#d9d9d9")
        self.IMPORT_BUT.configure(compound='top')
        self.IMPORT_BUT.configure(disabledforeground="#a3a3a3")
        self.IMPORT_BUT.configure(foreground="#000000")
        self.IMPORT_BUT.configure(highlightbackground="#d9d9d9")
        self.IMPORT_BUT.configure(highlightcolor="black")
        self.IMPORT_BUT.configure(pady="0")
        self.IMPORT_BUT.configure(text='''IMPORTER''')


    def porteuse_init(self):
        self.PORTEUSE_FRAME = tk.LabelFrame(self)
        self.PORTEUSE_FRAME.place(relx=0.349, rely=0.746, relheight=0.24, relwidth=0.386)
        self.PORTEUSE_FRAME.configure(relief='groove')
        self.PORTEUSE_FRAME.configure(foreground="#000000")
        self.PORTEUSE_FRAME.configure(text='''PORTEUSE''')
        self.PORTEUSE_FRAME.configure(background="#e9e9e9")
        self.PORTEUSE_FRAME.configure(highlightbackground="#d9d9d9")
        self.PORTEUSE_FRAME.configure(highlightcolor="black")

        self.DEMMARER_BUT = tk.Button(self.PORTEUSE_FRAME)
        image = Image.open("images/B2.png").resize((50, 50))
        self.DEMMARER_BUT.image = ImageTk.PhotoImage(image)
        self.DEMMARER_BUT.configure(image=self.DEMMARER_BUT.image)  

        self.DEMMARER_BUT.place(relx=0.053, rely=0.174, height=83, width=83, bordermode='ignore')
        self.DEMMARER_BUT.configure(activeforeground="black")
        self.DEMMARER_BUT.configure(background="#c0c0c0")
        self.DEMMARER_BUT.configure(compound='top')
        self.DEMMARER_BUT.configure(disabledforeground="#a3a3a3")
        self.DEMMARER_BUT.configure(foreground="#000000")
        self.DEMMARER_BUT.configure(highlightbackground="#d9d9d9")
        self.DEMMARER_BUT.configure(highlightcolor="black")
        self.DEMMARER_BUT.configure(pady="0")
        self.DEMMARER_BUT.configure(relief="groove")
        self.DEMMARER_BUT.configure(text='''DEMMARER''')
        self.DEMMARER_BUT.configure(command=self.start_machine)


        self.ARRETER_BUT = tk.Button(self.PORTEUSE_FRAME)
        image = Image.open("images/B1.png").resize((50, 50))
        self.ARRETER_BUT.image = ImageTk.PhotoImage(image)
        self.ARRETER_BUT.configure(image=self.ARRETER_BUT.image)  

        self.ARRETER_BUT.place(relx=0.353, rely=0.174, height=83, width=83, bordermode='ignore')
        self.ARRETER_BUT.configure(activeforeground="black")
        self.ARRETER_BUT.configure(background="#c0c0c0")
        self.ARRETER_BUT.configure(compound='top')
        self.ARRETER_BUT.configure(disabledforeground="#a3a3a3")
        self.ARRETER_BUT.configure(foreground="#000000")
        self.ARRETER_BUT.configure(highlightbackground="#d9d9d9")
        self.ARRETER_BUT.configure(highlightcolor="black")
        self.ARRETER_BUT.configure(pady="0")
        self.ARRETER_BUT.configure(relief="groove")
        self.ARRETER_BUT.configure(text='''ARRETER''')
        self.ARRETER_BUT.configure(command=self.stop_machine)

        self.RESET_BUT = tk.Button(self.PORTEUSE_FRAME)
        image = Image.open("images/reset.png").resize((50, 50))
        self.RESET_BUT.image = ImageTk.PhotoImage(image)
        self.RESET_BUT.configure(image=self.RESET_BUT.image)

        self.RESET_BUT.place(relx=0.66, rely=0.174, height=83, width=83, bordermode='ignore')
        self.RESET_BUT.configure(activeforeground="black")
        self.RESET_BUT.configure(background="#d9d9d9")
        self.RESET_BUT.configure(compound='top')
        self.RESET_BUT.configure(disabledforeground="#a3a3a3")
        self.RESET_BUT.configure(foreground="#000000")
        self.RESET_BUT.configure(highlightbackground="#d9d9d9")
        self.RESET_BUT.configure(highlightcolor="black")
        self.RESET_BUT.configure(relief="groove")
        self.RESET_BUT.configure(pady="0")
        self.RESET_BUT.configure(text='''Button''')

    def horloge_init(self): 
        self.DATE_LABEL = tk.Label(self)
        image = Image.open("images/calendar.png").resize((20, 20))
        self.DATE_LABEL.image = ImageTk.PhotoImage(image)
        self.DATE_LABEL.configure(image=self.DATE_LABEL.image)   

        self.DATE_LABEL.place(relx=0.535, rely=0.025, height=31, width=100)
        self.DATE_LABEL.configure(activeforeground="#000000")
        self.DATE_LABEL.configure(background="#ffffff")
        self.DATE_LABEL.configure(compound='left')
        self.DATE_LABEL.configure(padx = 5)
        self.DATE_LABEL.configure(disabledforeground="#a3a3a3")
        self.DATE_LABEL.configure(foreground="#000000")
        self.DATE_LABEL.configure(highlightbackground="#d9d9d9")
        self.DATE_LABEL.configure(highlightcolor="black")
        self.DATE_LABEL.configure(relief="solid")
        self.DATE_LABEL.configure(text='''00/00/0000''', font= ("Arial", 10))

        self.HORLOGE_LABEL = tk.Label(self)
        image = Image.open("images/horloge.png").resize((20, 20))
        self.HORLOGE_LABEL.image = ImageTk.PhotoImage(image)
        self.HORLOGE_LABEL.configure(image=self.HORLOGE_LABEL.image)

        self.HORLOGE_LABEL.place(relx=0.535, rely=0.104, height=31, width=80)
        self.HORLOGE_LABEL.configure(activeforeground="#000000")
        self.HORLOGE_LABEL.configure(background="#ffffff")
        self.HORLOGE_LABEL.configure(compound='left')
        self.HORLOGE_LABEL.configure(padx = 5)
        self.HORLOGE_LABEL.configure(disabledforeground="#a3a3a3")
        self.HORLOGE_LABEL.configure(foreground="#000000")
        self.HORLOGE_LABEL.configure(highlightbackground="#d9d9d9")
        self.HORLOGE_LABEL.configure(highlightcolor="black")
        self.HORLOGE_LABEL.configure(relief="solid")
        self.HORLOGE_LABEL.configure(text='''00:00:00''', font= ("Arial", 10))

        
    def generale_init(self):
        self.COLORIS_LABEL = tk.Label(self, text="")
        image = Image.open("images/COLORISLOGO.png").resize((240, 100))
        self.COLORIS_LABEL.image = ImageTk.PhotoImage(image)
        self.COLORIS_LABEL.configure(image=self.COLORIS_LABEL.image)

        self.COLORIS_LABEL.place(relx=0.013, rely=0.0, height=81, width=264)
        self.COLORIS_LABEL.configure(anchor='w')
        self.COLORIS_LABEL.configure(background="#ebebeb")
        self.COLORIS_LABEL.configure(compound='left')
        self.COLORIS_LABEL.configure(disabledforeground="#a3a3a3")
        self.COLORIS_LABEL.configure(foreground="#000000")
        self.COLORIS_LABEL.configure(highlightbackground="#d9d9d9")
        self.COLORIS_LABEL.configure(highlightcolor="black")

        self.logo = tk.Label(self)
        image = Image.open("images/com_logo.png").resize((60, 70))
        self.logo.image = ImageTk.PhotoImage(image)
        self.logo.configure(image=self.logo.image)

        self.logo.place(relx=0.9, rely=0.82, height=71, width=73)         
        self.logo.configure(anchor='w')
        self.logo.configure(background="#efefef")
        self.logo.configure(compound='left')
        self.logo.configure(disabledforeground="#a3a3a3")
        self.logo.configure(foreground="#000000")
        self.logo.configure(highlightbackground="#d9d9d9")
        self.logo.configure(highlightcolor="black")
        
    def scroll_up(self):
        self.PROG_LIST.yview_scroll(-1, "units")

    def scroll_down(self):
        self.PROG_LIST.yview_scroll(1, "units")


if __name__ == '__main__':
    COLORISsystem().mainloop()
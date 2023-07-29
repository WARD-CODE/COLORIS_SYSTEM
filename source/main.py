#! /usr/bin/env python3
# # -*- coding: utf-8 -*-
#             for prg in self._PROGRAM_DATA:
#                 if prg[0]==self._SELECTED_PROGRAM_NAME:
#                     self._SELECTED_PROGRAM = prg
                    
#                     self.CONT1_TIME.configure(text=self.sec_to_min(prg[1]))
#                     self.CONT2_TIME.configure(text=self.sec_to_min(prg[2]))
#                     self.CONT3_TIME.configure(text=self.sec_to_min(prg[3]))
#                     self.CONT4_TIME.configure(text=self.sec_to_min(prg[4]))
#                     self.CONT5_TIME.configure(text=self.sec_to_min(prg[5]))
#                     self.CONT6_TIME.configure(text=self.sec_to_min(prg[6]))
#                     self.CONT7_TIME.configure(text=self.sec_to_min(prg[7]))
#                     self.CONT8_TIME.configure(text=self.sec_to_min(prg[8]))
#                     self.CONT9_TIME.configure(text=self.sec_to_min(prg[9]))
#                     self.CONT10_TIME.configure(text=self.sec_to_min(prg[10]))
#                     break
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from source.fields_data import Fields
from source.import_data import ImportWindow

class COLORISsystem(tk.Tk):
    _MODE = None #mode manuel or automatic
    _MACHINE_STAT = None #STOP or INWORK
    _KEYBOARD_STAT = None

    def __init__(self,*args, **kwargs):             
        super().__init__(*args,**kwargs)
        self.WinConfig()
        self.timer=None
        self.table = None
        self.components = {}
        self.init_components()
        
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

    def on_import(self):
        return ImportWindow()
    

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

    # additional methods  
    def sec_to_min(self,seconds):
        minutes, secs = divmod(int(seconds), 60)
        return f"{minutes:02d}:{secs:02d}"

    def WinConfig(self):
        self.geometry("800x480+202+152")
        self.minsize(120, 1)
        self.maxsize(785, 570)
        self.resizable(1, 1)
        self.title("COLORIS SYSTEM")
        self.configure(background="#F7F7F7")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

    
    def init_components(self):

        self.containers_init()
        self.programmes_init()
        self.porteuse_init()
        self.horloge_init()
        self.generale_init()

    def containers_init(self):
        
        self.Frame1_2 = tk.Frame(self)
        self.Frame1_2.place(relx=0.05, rely=0.3, relheight=0.4, relwidth=0.9)
        self.Frame1_2.configure(relief='groove')
        self.Frame1_2.configure(borderwidth="2")
        self.Frame1_2.configure(relief="groove")
        self.Frame1_2.configure(background="#c0c0c0")
        self.Frame1_2.configure(highlightbackground="#d9d9d9")
        self.Frame1_2.configure(highlightcolor="black")

        
        self.CONTIN_LABEL = tk.Button(self.Frame1_2,text = "IN", font=("Arial", 12,"bold"))
        self.CONTIN_LABEL.place(relx=0.9, rely=0.06, height=65, width=50, bordermode='ignore')
        self.CONTIN_LABEL.configure(background="#EFEFEF")
        self.CONTIN_LABEL.configure(relief='groove')




        self.CONTOUT_LABEL = tk.Button(self.Frame1_2,text = "OUT", font=("Arial", 12,"bold"))
        self.CONTOUT_LABEL.place(relx=0.9, rely=0.47, height=65, width=50, bordermode='ignore')
        self.CONTOUT_LABEL.configure(background="#EFEFEF")
        self.CONTOUT_LABEL.configure(relief='groove')

        self.CONT1_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT1_BUT.place(relx=0.012, rely=0.047, height=75, width=50)
        self.CONT1_BUT.configure(relief='groove')
        self.CONT1_BUT.configure(background="#ADD5EE")
        self.CONT1_BUT.configure(text='''1''')
        

        self.CONT2_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT2_BUT.configure(relief='groove')
        self.CONT2_BUT.place(relx=0.1, rely=0.047, height=75,width=50)
        self.CONT2_BUT.configure(background="#ADD5EE")
        self.CONT2_BUT.configure(text='''2''')

        self.CONT3_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT3_BUT.configure(relief='groove')
        self.CONT3_BUT.place(relx=0.188, rely=0.047, height=75,width=50)
        self.CONT3_BUT.configure(background="#ADD5EE")
        self.CONT3_BUT.configure(text='''3''')

        self.CONT4_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT4_BUT.configure(relief='groove')
        self.CONT4_BUT.place(relx=0.276, rely=0.047, height=75,width=50)
        self.CONT4_BUT.configure(background="#ADD5EE")
        self.CONT4_BUT.configure(text='''4''')

        self.CONT5_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT5_BUT.configure(relief='groove')
        self.CONT5_BUT.place(relx=0.364, rely=0.047, height=75,width=50)
        self.CONT5_BUT.configure(background="#ADD5EE")
        self.CONT5_BUT.configure(text='''5''')


        self.CONT1_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT1_INDIC.place(relx=0.012, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT1_INDIC.configure(background="#d9d9d9")
        self.CONT1_INDIC.configure(borderwidth="2")
        self.CONT1_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT1_INDIC.configure(highlightcolor="black")
        self.CONT1_INDIC.configure(insertbackground="black")
        self.CONT1_INDIC.configure(relief="ridge")
        self.CONT1_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT1_INDIC.configure(selectforeground="black")

        self.CONT2_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT2_INDIC.place(relx=0.1, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT2_INDIC.configure(background="#d9d9d9")
        self.CONT2_INDIC.configure(borderwidth="2")
        self.CONT2_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT2_INDIC.configure(highlightcolor="black")
        self.CONT2_INDIC.configure(insertbackground="black")
        self.CONT2_INDIC.configure(relief="ridge")
        self.CONT2_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT2_INDIC.configure(selectforeground="black")

        self.CONT3_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT3_INDIC.place(relx=0.188, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT3_INDIC.configure(background="#d9d9d9")
        self.CONT3_INDIC.configure(borderwidth="2")
        self.CONT3_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT3_INDIC.configure(highlightcolor="black")
        self.CONT3_INDIC.configure(insertbackground="black")
        self.CONT3_INDIC.configure(relief="ridge")
        self.CONT3_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT3_INDIC.configure(selectforeground="black")
        
        self.CONT4_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT4_INDIC.place(relx=0.276, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT4_INDIC.configure(background="#d9d9d9")
        self.CONT4_INDIC.configure(borderwidth="2")
        self.CONT4_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT4_INDIC.configure(highlightcolor="black")
        self.CONT4_INDIC.configure(insertbackground="black")
        self.CONT4_INDIC.configure(relief="ridge")
        self.CONT4_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT4_INDIC.configure(selectforeground="black")

        self.CONT5_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT5_INDIC.place(relx=0.364, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT5_INDIC.configure(background="#d9d9d9")
        self.CONT5_INDIC.configure(borderwidth="2")
        self.CONT5_INDIC.configure(relief="ridge")


        self.CONT1_TIME = tk.Label(self.Frame1_2)
        self.CONT1_TIME.place(relx=0.012, rely=0.47, height=31, width=50)
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
        self.CONT2_TIME.place(relx=0.1, rely=0.47, height=31, width=50)
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
        self.CONT3_TIME.place(relx=0.188, rely=0.47, height=31, width=50)
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
        self.CONT4_TIME.place(relx=0.276, rely=0.47, height=31, width=50)
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
        self.CONT5_TIME.place(relx=0.364, rely=0.47, height=31, width=50)
        self.CONT5_TIME.configure(activeforeground="#000000")
        self.CONT5_TIME.configure(background="#ffffff")
        self.CONT5_TIME.configure(compound='left')
        self.CONT5_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT5_TIME.configure(foreground="#000000")
        self.CONT5_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT5_TIME.configure(highlightcolor="black")
        self.CONT5_TIME.configure(relief="groove")
        self.CONT5_TIME.configure(text='''temps''')
        
        self.CONT6_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT6_BUT.configure(relief='groove')
        self.CONT6_BUT.place(relx=0.452, rely=0.047, height=75,width=50)
        self.CONT6_BUT.configure(background="#ADD5EE")
        self.CONT6_BUT.configure(text='''6''')

        self.CONT7_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT7_BUT.configure(relief='groove')
        self.CONT7_BUT.place(relx=0.540, rely=0.047, height=75,width=50)
        self.CONT7_BUT.configure(background="#ADD5EE")
        self.CONT7_BUT.configure(text='''7''')

        self.CONT8_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT8_BUT.configure(relief='groove')
        self.CONT8_BUT.place(relx=0.628, rely=0.047, height=75,width=50)
        self.CONT8_BUT.configure(background="#ADD5EE")
        self.CONT8_BUT.configure(text='''8''')

        self.CONT9_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT9_BUT.configure(relief='groove')
        self.CONT9_BUT.place(relx=0.716, rely=0.047, height=75,width=50)
        self.CONT9_BUT.configure(background="#ADD5EE")
        self.CONT9_BUT.configure(text='''9''')

        self.CONT10_BUT = tk.Button(self.Frame1_2, font=("Arial",13,"bold"))
        self.CONT10_BUT.configure(relief='groove')
        self.CONT10_BUT.place(relx=0.804, rely=0.047, height=75,width=50)
        self.CONT10_BUT.configure(background="#ADD5EE")
        self.CONT10_BUT.configure(text='''10''')

        self.CONT6_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT6_INDIC.place(relx=0.452, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT6_INDIC.configure(background="#d9d9d9")
        self.CONT6_INDIC.configure(borderwidth="2")
        self.CONT6_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT6_INDIC.configure(highlightcolor="black")
        self.CONT6_INDIC.configure(insertbackground="black")
        self.CONT6_INDIC.configure(relief="ridge")
        self.CONT6_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT6_INDIC.configure(selectforeground="black")

        self.CONT7_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT7_INDIC.place(relx=0.540, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT7_INDIC.configure(background="#d9d9d9")
        self.CONT7_INDIC.configure(borderwidth="2")
        self.CONT7_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT7_INDIC.configure(highlightcolor="black")
        self.CONT7_INDIC.configure(insertbackground="black")
        self.CONT7_INDIC.configure(relief="ridge")
        self.CONT7_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT7_INDIC.configure(selectforeground="black")

        self.CONT8_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT8_INDIC.place(relx=0.628, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT8_INDIC.configure(background="#d9d9d9")
        self.CONT8_INDIC.configure(borderwidth="2")
        self.CONT8_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT8_INDIC.configure(highlightcolor="black")
        self.CONT8_INDIC.configure(insertbackground="black")
        self.CONT8_INDIC.configure(relief="ridge")
        self.CONT8_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT8_INDIC.configure(selectforeground="black")

        self.CONT9_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT9_INDIC.place(relx=0.716, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT9_INDIC.configure(background="#d9d9d9")
        self.CONT9_INDIC.configure(borderwidth="2")
        self.CONT9_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT9_INDIC.configure(highlightcolor="black")
        self.CONT9_INDIC.configure(insertbackground="black")
        self.CONT9_INDIC.configure(relief="ridge")
        self.CONT9_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT9_INDIC.configure(selectforeground="black")

        self.CONT10_INDIC = tk.Canvas(self.Frame1_2)
        self.CONT10_INDIC.place(relx=0.804, rely=0.65, relheight=0.15, relwidth=0.07)
        self.CONT10_INDIC.configure(background="#d9d9d9")
        self.CONT10_INDIC.configure(borderwidth="2")
        self.CONT10_INDIC.configure(highlightbackground="#d9d9d9")
        self.CONT10_INDIC.configure(highlightcolor="black")
        self.CONT10_INDIC.configure(insertbackground="black")
        self.CONT10_INDIC.configure(relief="ridge")
        self.CONT10_INDIC.configure(selectbackground="#c4c4c4")
        self.CONT10_INDIC.configure(selectforeground="black")

        self.CONT6_TIME = tk.Label(self.Frame1_2)
        self.CONT6_TIME.place(relx=0.452, rely=0.47, height=31, width=50)
        self.CONT6_TIME.configure(activeforeground="#000000")
        self.CONT6_TIME.configure(background="#ffffff")
        self.CONT6_TIME.configure(compound='left')
        self.CONT6_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT6_TIME.configure(foreground="#000000")
        self.CONT6_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT6_TIME.configure(highlightcolor="black")
        self.CONT6_TIME.configure(relief="groove")
        self.CONT6_TIME.configure(text='''temps''')

        self.CONT7_TIME = tk.Label(self.Frame1_2)
        self.CONT7_TIME.place(relx=0.540, rely=0.47, height=31, width=50)
        self.CONT7_TIME.configure(activeforeground="#000000")
        self.CONT7_TIME.configure(background="#ffffff")
        self.CONT7_TIME.configure(compound='left')
        self.CONT7_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT7_TIME.configure(foreground="#000000")
        self.CONT7_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT7_TIME.configure(highlightcolor="black")
        self.CONT7_TIME.configure(relief="groove")
        self.CONT7_TIME.configure(text='''temps''')

        self.CONT8_TIME = tk.Label(self.Frame1_2)
        self.CONT8_TIME.place(relx=0.628, rely=0.47, height=31, width=50)
        self.CONT8_TIME.configure(activeforeground="#000000")
        self.CONT8_TIME.configure(background="#ffffff")
        self.CONT8_TIME.configure(compound='left')
        self.CONT8_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT8_TIME.configure(foreground="#000000")
        self.CONT8_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT8_TIME.configure(highlightcolor="black")
        self.CONT8_TIME.configure(relief="groove")
        self.CONT8_TIME.configure(text='''temps''')

        self.CONT9_TIME = tk.Label(self.Frame1_2)
        self.CONT9_TIME.place(relx=0.716, rely=0.47, height=31, width=50)
        self.CONT9_TIME.configure(activeforeground="#000000")
        self.CONT9_TIME.configure(background="#ffffff")
        self.CONT9_TIME.configure(compound='left')
        self.CONT9_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT9_TIME.configure(foreground="#000000")
        self.CONT9_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT9_TIME.configure(highlightcolor="black")
        self.CONT9_TIME.configure(relief="groove")
        self.CONT9_TIME.configure(text='''temps''')

        self.CONT10_TIME = tk.Label(self.Frame1_2)
        self.CONT10_TIME.place(relx=0.804, rely=0.47, height=31, width=50)
        self.CONT10_TIME.configure(activeforeground="#000000")
        self.CONT10_TIME.configure(background="#ffffff")
        self.CONT10_TIME.configure(compound='left')
        self.CONT10_TIME.configure(disabledforeground="#a3a3a3")
        self.CONT10_TIME.configure(foreground="#000000")
        self.CONT10_TIME.configure(highlightbackground="#d9d9d9")
        self.CONT10_TIME.configure(highlightcolor="black")
        self.CONT10_TIME.configure(relief="groove")
        self.CONT10_TIME.configure(text='''temps''') 
        
    def programmes_init(self):

        self.PRG_BUT = tk.Button(self)
        image = Image.open("images/import.png").resize((50, 50))
        self.PRG_BUT.image = ImageTk.PhotoImage(image)
        self.PRG_BUT.configure(image=self.PRG_BUT.image)  

        self.PRG_BUT.place(relx=0.038, rely=0.8, height=74, width=100, bordermode='ignore')
        self.PRG_BUT.configure(activeforeground="black")
        self.PRG_BUT.configure(background="#d9d9d9")
        self.PRG_BUT.configure(compound='top')
        self.PRG_BUT.configure(disabledforeground="#a3a3a3")
        self.PRG_BUT.configure(foreground="#000000")
        self.PRG_BUT.configure(highlightbackground="#d9d9d9")
        self.PRG_BUT.configure(highlightcolor="black")
        self.PRG_BUT.configure(pady="0")
        self.PRG_BUT.configure(text='''PROGRAMMES''')
        self.PRG_BUT.configure(command=self.on_import)


    def porteuse_init(self):
        self.PORTEUSE_FRAME = tk.Frame(self)
        self.PORTEUSE_FRAME.place(relx=0.31, rely=0.746, relheight=0.24, relwidth=0.38)
        self.PORTEUSE_FRAME.configure(relief='groove')
        self.PORTEUSE_FRAME.configure(background="#F7F7F7")
        self.PORTEUSE_FRAME.configure(highlightbackground="#d9d9d9")
        self.PORTEUSE_FRAME.configure(highlightcolor="black")

        self.DEMMARER_BUT = tk.Button(self.PORTEUSE_FRAME)
        image = Image.open("images/B2.png").resize((50, 50))
        self.DEMMARER_BUT.image = ImageTk.PhotoImage(image)
        self.DEMMARER_BUT.configure(image=self.DEMMARER_BUT.image)  

        self.DEMMARER_BUT.place(relx=0.053, rely=0.174, height=83, width=83, bordermode='ignore')
        self.DEMMARER_BUT.configure(activeforeground="black")
        self.DEMMARER_BUT.configure(background="#51B8F9")
        self.DEMMARER_BUT.configure(compound='top')
        self.DEMMARER_BUT.configure(disabledforeground="#a3a3a3")
        self.DEMMARER_BUT.configure(foreground="#ffffff")
        self.DEMMARER_BUT.configure(highlightbackground="#d9d9d9")
        self.DEMMARER_BUT.configure(activebackground="green")
        self.DEMMARER_BUT.configure(highlightcolor="black")
        self.DEMMARER_BUT.configure(pady="0")
        self.DEMMARER_BUT.configure(relief="groove")
        self.DEMMARER_BUT.configure(text='''DEMMARER''', font=("Calibri", 11,"bold"))
        self.DEMMARER_BUT.configure(command=self.start_machine)


        self.ARRETER_BUT = tk.Button(self.PORTEUSE_FRAME)
        image = Image.open("images/B1.png").resize((50, 50))
        self.ARRETER_BUT.image = ImageTk.PhotoImage(image)
        self.ARRETER_BUT.configure(image=self.ARRETER_BUT.image)  

        self.ARRETER_BUT.place(relx=0.353, rely=0.174, height=83, width=83, bordermode='ignore')
        self.ARRETER_BUT.configure(activeforeground="black")
        self.ARRETER_BUT.configure(background="#51B8F9")
        self.ARRETER_BUT.configure(compound='top')
        self.ARRETER_BUT.configure(disabledforeground="#a3a3a3")
        self.ARRETER_BUT.configure(activebackground="red")
        self.ARRETER_BUT.configure(foreground="#ffffff")
        self.ARRETER_BUT.configure(highlightbackground="#d9d9d9")
        self.ARRETER_BUT.configure(highlightcolor="black")
        self.ARRETER_BUT.configure(pady="0")
        self.ARRETER_BUT.configure(relief="groove")
        self.ARRETER_BUT.configure(text='''ARRETER''', font=("Calibri", 11,"bold"))
        self.ARRETER_BUT.configure(command=self.stop_machine)

        self.RESET_BUT = tk.Button(self.PORTEUSE_FRAME)
        image = Image.open("images/reset.png").resize((50, 50))
        self.RESET_BUT.image = ImageTk.PhotoImage(image)
        self.RESET_BUT.configure(image=self.RESET_BUT.image)

        self.RESET_BUT.place(relx=0.66, rely=0.174, height=83, width=83, bordermode='ignore')
        self.RESET_BUT.configure(activeforeground="black")
        self.RESET_BUT.configure(background="#51B8F9")
        self.RESET_BUT.configure(compound='top')
        self.RESET_BUT.configure(disabledforeground="#a3a3a3")
        self.RESET_BUT.configure(activebackground="yellow")
        self.RESET_BUT.configure(foreground="#ffffff")
        self.RESET_BUT.configure(highlightbackground="#d9d9d9")
        self.RESET_BUT.configure(highlightcolor="black")
        self.RESET_BUT.configure(relief="groove")
        self.RESET_BUT.configure(pady="0")
        self.RESET_BUT.configure(text='''REDEMARER''', font=("Calibri", 11,"bold"))

    def horloge_init(self): 

        a = 0.03
        self.DATE_LABEL = tk.Label(self)
        image = Image.open("images/calendar.png").resize((20, 20))
        self.DATE_LABEL.image = ImageTk.PhotoImage(image)
        self.DATE_LABEL.configure(image=self.DATE_LABEL.image)   
        
        self.DATE_LABEL.place(relx=0.45+ a, rely=0.025, height=31, width=120)
        self.DATE_LABEL.configure(activeforeground="#000000")
        self.DATE_LABEL.configure(background="#F7F7F7")
        self.DATE_LABEL.configure(compound='left')
        self.DATE_LABEL.configure(padx = 5)
        self.DATE_LABEL.configure(highlightcolor="black")
        self.DATE_LABEL.configure(text='''00/00/0000''', font= ("Arial", 12))

        self.HORLOGE_LABEL = tk.Label(self)
        image = Image.open("images/horloge.png").resize((25, 25))
        self.HORLOGE_LABEL.image = ImageTk.PhotoImage(image)
        self.HORLOGE_LABEL.configure(image=self.HORLOGE_LABEL.image)

        self.HORLOGE_LABEL.place(relx=0.44+ a, rely=0.1, height=31, width=100)
        self.HORLOGE_LABEL.configure(activeforeground="#000000")
        self.HORLOGE_LABEL.configure(background="#F7F7F7")
        self.HORLOGE_LABEL.configure(compound='left')
        self.HORLOGE_LABEL.configure(padx = 5)
        self.HORLOGE_LABEL.configure(disabledforeground="#a3a3a3")
        self.HORLOGE_LABEL.configure(text='''00:00''', font= ("Arial", 12))
        
        self.TEMPERATURE_LABEL = tk.Label(self)
        image = Image.open("images/temperature.png").resize((30, 30))
        self.TEMPERATURE_LABEL.image = ImageTk.PhotoImage(image)
        self.TEMPERATURE_LABEL.configure(image=self.TEMPERATURE_LABEL.image)
        self.TEMPERATURE_LABEL.place(relx=0.62+ a, rely=0.015, height=40, width=190)
        self.TEMPERATURE_LABEL.configure(background="#F7F7F7")
        self.TEMPERATURE_LABEL.configure(compound='left')
        self.TEMPERATURE_LABEL.configure(padx = 5)
        self.TEMPERATURE_LABEL.configure(text='''Temperature    00.00 C°''', font= ("Arial", 10,"bold"))
        
        self.HUMIDITY_LABEL = tk.Label(self)
        image = Image.open("images/humidity.png").resize((30, 30))
        self.HUMIDITY_LABEL.image = ImageTk.PhotoImage(image)
        self.HUMIDITY_LABEL.configure(image=self.HUMIDITY_LABEL.image)
        self.HUMIDITY_LABEL.place(relx=0.61 + a, rely=0.087, height=40, width=190)
        self.HUMIDITY_LABEL.configure(background="#F7F7F7")
        self.HUMIDITY_LABEL.configure(compound='left')
        self.HUMIDITY_LABEL.configure(padx = 5)
        self.HUMIDITY_LABEL.configure(text='''Humidité      00.00 %''', font= ("Arial", 10,"bold"))
        
        self.VENTILLATEUR_LABEL = tk.Label(self)
        image = Image.open("images/ventillateur.png").resize((70, 70))
        self.VENTILLATEUR_LABEL.image = ImageTk.PhotoImage(image)
        self.VENTILLATEUR_LABEL.configure(image=self.VENTILLATEUR_LABEL.image)
        self.VENTILLATEUR_LABEL.place(relx=0.87 + a, rely=0.02, height=70, width=70)
        self.VENTILLATEUR_LABEL.configure(background="#F7F7F7")
        
        
        
    def generale_init(self):
        self.COLORIS_LABEL = tk.Label(self, text="")
        image = Image.open("images/COLORISLOGO.png").resize((300, 120))
        self.COLORIS_LABEL.image = ImageTk.PhotoImage(image)
        self.COLORIS_LABEL.configure(image=self.COLORIS_LABEL.image)

        self.COLORIS_LABEL.place(relx=0.013, rely=0.0, height=100, width=340)
        self.COLORIS_LABEL.configure(background="#F7F7F7")

        self.logo = tk.Label(self)
        image = Image.open("images/LOGO.png").resize((80, 100))
        self.logo.image = ImageTk.PhotoImage(image)
        self.logo.configure(image=self.logo.image)

        self.logo.place(relx=0.89, rely=0.78, height=100, width=80)         
        self.logo.configure(background="#F7F7F7")

        


if __name__ == '__main__':
    COLORISsystem().mainloop()
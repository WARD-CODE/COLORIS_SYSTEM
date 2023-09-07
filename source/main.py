#! /usr/bin/env python3
# # -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from source.import_data import ImportWindow
from datetime import datetime,time ,timedelta
import time as tm

from motors_prog import Motor
from sensors import PositionSensor, InSensor, OutSensor

class COLORISsystem(tk.Tk):
    _MACHINE_STAT = None #STOP or INWORK

    def __init__(self,*args, **kwargs):             
        super().__init__(*args,**kwargs)
        self.WinConfig()
        
        self.table = None
        
        self.components = {}
        self.timers = []
        self.timers_lab = []
        self.timers_ind = []
        self.init_components()

        
        #hard init
        self.M1 = Motor(4,3,200)
        self.M2 = Motor(7,5, 200)
        self.SP = PositionSensor(2)
        self.SI = InSensor(0)
        self.SOut = OutSensor(1)

        #flags
        
        self.forward_allow = False
        self.lift_allow = False
        self.fallout_allow = False

        self.sensor_position = 0

        self.running_timer = False
        
        
        self.posit = False
        self.atHome = False
        self.atEnd = False
        self._MACHINE_STAT = False

        self.ventilation = True
        self.l = True

        self.DATE_TIME_ROUTINE()
        self.FAN_ROUTINE()

        

    def in_end(self):
        self.atEnd = True
        
    
    def stop_machine(self):
        self._MACHINE_STAT = False

    def start_machine(self):

        if self.CHECK_HOME():
            self._MACHINE_STAT=True
            self.CONTIN_LABEL.configure(background="#EFEFEF")
            

        if self._MACHINE_STAT:

            if self.CHECK_HOME():
                self.PICK_UP_ROUTINE()
                tm.sleep(2)
                self.atHome = False
                self.forward_allow = True
                self.fallout_allow = True
            
            if self.forward_allow:   
                self.FORWARD_ROUTINE()
                tm.sleep(1)
                self.forward_allow = False

            if self.CHECK_POSITION():

                if self.check_timer():

                    if self.fallout_allow: 
                        self.FALLOUT_ROUTINE()
                        self.fallout_allow = False
                self.posit = False

            if self.lift_allow:
                tm.sleep(1)
                self.LIFT_ROUTINE()
                self.forward_allow = True
                self.lift_allow = False
                tm.sleep(1)
    
            if self.CHECK_ARRIVE() or (self.sensor_position > 10):
                
                self.DROP_DOWN_ROUTINE()
                tm.sleep(1)
                self.GOHOME_ROUTINE()
                self._MACHINE_STAT = False
                self.sensor_position = 0
                return
  
        self.after(1000, self.start_machine)   

    def PICK_UP_ROUTINE(self):
        print("PICK UP ROUTINE")
        self.M2.forward(self.M2.FORWARD_VERTICAL_REV)
        tm.sleep(0.02)
        self.M2.forward(self.M2.PICK_REV)
        tm.sleep(0.02)
        self.M2.forward(self.M2.BACKWARD_VERTICAL_REV)

    def DROP_DOWN_ROUTINE(self):
        print("DROP DOWN ROUTINE")
        self.M2.forward(self.M2.FORWARD_VERTICAL_REV)
        tm.sleep(0.02)
        self.M2.backward(self.M2.PICK_REV)
        tm.sleep(0.02)
        self.M2.forward(self.M2.BACKWARD_VERTICAL_REV)

    def GOHOME_ROUTINE(self):
        print("GO HOME")
        if not self.SI.read() and self.SOut.read():
            self.M1.backward(self.M1.HOME_HORIZONTAL_REV)
        
        elif not self.SI.read() and not self.SOut.read():
            self.M1.backward(self.M1.BACKWARD_HORIZONTAL_REV * self.SP.sensor_position)

    def CHECK_HOME(self):
        if self.SI.read() and self.atHome:
            self.CONTIN_LABEL.configure(background="red")
            self.CONTOUT_LABEL.configure(background="#EFEFEF")
            return True
        self.CONTIN_LABEL.configure(background="#EFEFEF")
        return False

    def CHECK_ARRIVE(self):
        if self.SOut.read() and self.atEnd:
            self.CONTOUT_LABEL.configure(background="red")
            self.CONTIN_LABEL.configure(background="#EFEFEF")
            return True
        self.CONTOUT_LABEL.configure(background="#EFEFEF")
        return False
    
    def CHECK_POSITION(self):
            
        if self.SP.read() and self.posit:
            self.sensor_position += 1
            return True
        return False

    def FALLOUT_ROUTINE(self):
        self.M2.forward(self.M2.FORWARD_VERTICAL_REV*5)
        self.current_ind = self.timers_ind[self.sensor_position-1]
        self.current_ind.configure(background="red")
        tm.sleep(1)
        self.start_timers()

    def LIFT_ROUTINE(self):
        self.M2.backward(self.M2.BACKWARD_VERTICAL_REV*5)

    def FORWARD_ROUTINE(self):
        self.M1.forward(self.M1.FORWARD_HORIZONTAL_REV*20)

    def TEMPERATURE_ROUTINE(self):
        pass

    def HUMIDITY_ROUTINE(self):
        pass

    def FAN_ROUTINE(self):

        if self.ventilation:

            if self.l:
                m = "ventillateur"
            else:
                m = "ventillateur2"

            image = Image.open("images/{}.png".format(m)).resize((70, 70))
            self.VENTILLATEUR_LABEL.image = ImageTk.PhotoImage(image)
            self.VENTILLATEUR_LABEL.configure(image=self.VENTILLATEUR_LABEL.image)

            self.l = not self.l

        self.after(200,self.FAN_ROUTINE)

    def DATE_TIME_ROUTINE(self):

        current_t = datetime.now()
        
        date_t = current_t.date().strftime("%d/%m/%Y")
        time_t = current_t.time().strftime("%H:%M:%S")

        self.DATE_LABEL.configure(text = date_t)
        self.HORLOGE_LABEL.configure(text = time_t)

        self.after(1000,self.DATE_TIME_ROUTINE)
      
    def on_import(self):
        return ImportWindow(self)
    
    def check_timer(self):
        self.current_count = self.timers_lab[self.sensor_position-1]
        self.current_time = datetime.strptime(self.current_count.cget('text'), "%M:%S").time()
        if self.current_time == time(0, 0):
            
            self.forward_allow = True
            self.fallout_allow = False
            self.lift_allow = False

            self.current_ind.configure(background="#d9d9d9")
            return False
        
        self.fallout_allow = True
        return True

    def start_timers(self):
        self.current_count = self.timers_lab[self.sensor_position-1]
        self.current_time = datetime.strptime(self.current_count.cget('text'), "%M:%S").time()   
        self.running_timer = True
        self.update_timers()

    def stop_timers(self):
        self.running_timer = False

    def update_timers(self):
        if self.running_timer:
            if self.current_time == time(0, 0):
                self.stop_timers()
                self.lift_allow = True
                self.current_ind.configure(background="#d9d9d9")
                return
            
            self.current_time = (datetime.combine(datetime.today(), self.current_time) - timedelta(seconds=1)).time()
            self.current_count.config(text=self.current_time.strftime("%M:%S"))
            self.after(1000, self.update_timers)  


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

        
        self.CONTIN_LABEL = tk.Label(self.Frame1_2,text = "IN", font=("Arial", 12,"bold"))
        self.CONTIN_LABEL.place(relx=0.9, rely=0.06, height=65, width=50, bordermode='ignore')
        self.CONTIN_LABEL.configure(background="#EFEFEF")
        self.CONTIN_LABEL.configure(relief='groove')
        



        self.CONTOUT_LABEL = tk.Label(self.Frame1_2,text = "OUT", font=("Arial", 12,"bold"))
        self.CONTOUT_LABEL.place(relx=0.9, rely=0.47, height=65, width=50, bordermode='ignore')
        self.CONTOUT_LABEL.configure(background="#EFEFEF")
        self.CONTOUT_LABEL.configure(relief='groove')

        self.CONT1_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
        self.CONT1_BUT.place(relx=0.012, rely=0.047, height=75, width=50)
        self.CONT1_BUT.configure(relief='groove')
        self.CONT1_BUT.configure(background="#ADD5EE")
        self.CONT1_BUT.configure(text='''1''')

        self.CONT2_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
        self.CONT2_BUT.configure(relief='groove')
        self.CONT2_BUT.place(relx=0.1, rely=0.047, height=75,width=50)
        self.CONT2_BUT.configure(background="#ADD5EE")
        self.CONT2_BUT.configure(text='''2''')

        self.CONT3_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
        self.CONT3_BUT.configure(relief='groove')
        self.CONT3_BUT.place(relx=0.188, rely=0.047, height=75,width=50)
        self.CONT3_BUT.configure(background="#ADD5EE")
        self.CONT3_BUT.configure(text='''3''')

        self.CONT4_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
        self.CONT4_BUT.configure(relief='groove')
        self.CONT4_BUT.place(relx=0.276, rely=0.047, height=75,width=50)
        self.CONT4_BUT.configure(background="#ADD5EE")
        self.CONT4_BUT.configure(text='''4''')

        self.CONT5_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
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
        self.CONT1_TIME.configure(text="temps", font=('Arial',12,'bold'))
        

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
        self.CONT2_TIME.configure(text="temps", font=('Arial',12,'bold'))

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
        self.CONT3_TIME.configure(text="temps", font=('Arial',12,'bold'))

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
        self.CONT4_TIME.configure(text="temps", font=('Arial',12,'bold'))

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
        self.CONT5_TIME.configure(text="temps", font=('Arial',12,'bold'))
        
        self.CONT6_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
        self.CONT6_BUT.configure(relief='groove')
        self.CONT6_BUT.place(relx=0.452, rely=0.047, height=75,width=50)
        self.CONT6_BUT.configure(background="#ADD5EE")
        self.CONT6_BUT.configure(text='''6''')

        self.CONT7_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
        self.CONT7_BUT.configure(relief='groove')
        self.CONT7_BUT.place(relx=0.540, rely=0.047, height=75,width=50)
        self.CONT7_BUT.configure(background="#ADD5EE")
        self.CONT7_BUT.configure(text='''7''')

        self.CONT8_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
        self.CONT8_BUT.configure(relief='groove')
        self.CONT8_BUT.place(relx=0.628, rely=0.047, height=75,width=50)
        self.CONT8_BUT.configure(background="#ADD5EE")
        self.CONT8_BUT.configure(text='''8''')

        self.CONT9_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
        self.CONT9_BUT.configure(relief='groove')
        self.CONT9_BUT.place(relx=0.716, rely=0.047, height=75,width=50)
        self.CONT9_BUT.configure(background="#ADD5EE")
        self.CONT9_BUT.configure(text='''9''')

        self.CONT10_BUT = tk.Button(self.Frame1_2, font=("Arial",20,"bold"))
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
        self.CONT6_TIME.configure(text="temps", font=('Arial',13,'bold'))

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
        self.CONT7_TIME.configure(text="temps", font=('Arial',13,'bold'))

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
        self.CONT8_TIME.configure(text="temps", font=('Arial',13,'bold'))

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
        self.CONT9_TIME.configure(text="temps", font=('Arial',13,'bold'))

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
        self.CONT10_TIME.configure(text="temps", font=('Arial',13,'bold')) 

        self.timers_lab = [self.CONT1_TIME,
                           self.CONT2_TIME,
                           self.CONT3_TIME,
                           self.CONT4_TIME,
                           self.CONT5_TIME,
                           self.CONT6_TIME,
                           self.CONT7_TIME,
                           self.CONT8_TIME,
                           self.CONT9_TIME,
                           self.CONT10_TIME]
        
        self.timers_ind = [self.CONT1_INDIC,
                           self.CONT2_INDIC,
                           self.CONT3_INDIC,
                           self.CONT4_INDIC,
                           self.CONT5_INDIC,
                           self.CONT6_INDIC,
                           self.CONT7_INDIC,
                           self.CONT8_INDIC,
                           self.CONT9_INDIC,
                           self.CONT10_INDIC]
        
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
        
        self.DATE_LABEL.place(relx=0.44+ a, rely=0.025, height=31, width=120)
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
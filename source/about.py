import tkinter as tk 



class AboutWindow(tk.Toplevel):
      def __init__(self, text):
        super().__init__()
        self.geometry("250x370+302+352")
        self.resizable(False, False)
        self.title("about")
        self.minsize(120, 1)
        self.maxsize(245, 320)
        self.texto = text
        
        self.components = {}
     
        self.init_components()
        self.disp_components()
     
      def init_components(self):
          self.components["title"] = tk.Label(master = self,text = "COLORIS System V1 (R)",font=("Arial",14,"bold"),foreground="#51B8F9")
          self.components["context"] = tk.Text(master = self, width=30,height=15,font=("Arial",12),background="#c0c0c0")
          self.components["context"].insert(tk.END,self.texto)
          self.components["fermer"] = tk.Button(master = self,text = "fermer",font=("Arial",12,"bold"), width=7, height=2,background="#51B8F9",command=self.on_fermer)


      def disp_components(self):
          self.components["title"].grid(row = 0, column=0,pady = 5)
          self.components["context"].grid(row = 1, column=0,pady = 3)
          self.components["fermer"].grid(row = 2, column=0,pady = 5)
      
      def on_fermer(self):
          self.destroy()
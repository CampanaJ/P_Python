from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop
import PIL 

class login:
    def __init__(self):
        self.ventana = Tk ()
        self.ventana.geometry("400x700")
        
        fondo = "#03bb85"
        
        #Frames
        
        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)
        
        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)
        
        
        mainloop()

login()
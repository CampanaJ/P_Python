from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop
from PIL import Image, ImageTk
import PIL.Image 

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
        
        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)
        
        #Titulo
        
        self.titulo = Label(self.frame_superior,
                            text= "Login",
                            font = ("calisto MT", 36, "bold"),
                            bg=fondo)
        self.titulo.pack(side = "top", pady= 20)
        
        #Imagen
        
        self.img = Image.open("Imagenes\\User_login.png")
        self.img = self.img.resize((150,150))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image = self.render, bg = fondo)
        self.fondo.pack(expand=True, fill="both", side="top")
        
        #Partes_Datos
        
        self.label_usuario = Label(self.frame_inferior,
                                   text="Usuario:",
                                   font= ("Arial", 18),
                                   bg = fondo,
                                   fg="black")
        self.label_usuario.grid(row=0, column=0, padx=10, sticky="e")
        
        self.entry_usuario = Entry (self.frame_inferior,
                                    bd=0,
                                    width=14,
                                    font=("Arial", 18))
        self.entry_usuario.grid(row= 0, column=1, columnspan=3, padx=5, sticky="w")
        
        
        self.label_contraseña = Label(self.frame_inferior,
                                   text="Contraseña:",
                                   font= ("Arial", 18),
                                   bg = fondo,
                                   fg="black")
        self.label_contraseña.grid(row=1, column=0, padx=10, sticky="e")
        
        self.entry_contraseña = Entry (self.frame_inferior,
                                    bd=0,
                                    width=14,
                                    font=("Arial", 18),
                                    show="*")
        self.entry_contraseña.grid(row= 1, column=1, columnspan=3, padx=5, sticky="w")
        
        #Boton para ingresar
        
        self.boton_ingresar = Button(self.frame_inferior,
                                     text="Ingresar",
                                     width=16,
                                     font=("Arial",12),
                                     command=self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=35)     
                
        mainloop()
        
    def entrar(self):
        nombre = self.entry_usuario.get()
        contra = self.entry_contraseña.get()
            
        if nombre == "Admin" and contra == "Admin123":
            messagebox.showinfo("Acceso Correcto", "Ingresando...")
        else:
            messagebox.showerror("Acceso Denegado", "Usuario y/o Contraseña INCORRECTO")
login()
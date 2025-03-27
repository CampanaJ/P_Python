from tkinter import Tk, mainloop, OptionMenu, Label, StringVar, Entry, Button, Spinbox, IntVar, messagebox

class Gui:
    def __init__(self):
        ventana = Tk()
        fondo = "#03bb85"
        ventana.title = "Formulario"
        ventana.config(bg=fondo)
        
        self.titulo = Label(ventana, text= "Formulario", font=("Calisto Mt", 30), bg=fondo, fg="white")
        
        self.especialidad = StringVar()
        edad = StringVar()
        
        self.etiqueta_1 = Label(ventana, text="Nombre\s: ", bg=fondo, fg="white")
        self.etiqueta_2 = Label(ventana, text="Apellido\s: ", bg=fondo, fg="white")
        self.etiqueta_3 = Label(ventana, text="Especialidad: ", bg=fondo, fg="white")
        self.etiqueta_4 = Label(ventana, text="Edad: ", bg=fondo, fg="white")
        
        self.entrada_nombre = Entry(ventana)
        self.entrada_apellido = Entry(ventana)
        
        self.boton = Button(ventana, text="Agregar", width=30, cursor="hand2", command=self.datos)
        
        self.lista = ["Carrera 1", "Carrera 2", "Carrera 3","Carrera 4"] 
        
        self.opciones = OptionMenu(ventana, self.especialidad, *self.lista)
        
        self.opciones.configure(width=40,
                                activebackground="gray",
                                bd= 0,
                                cursor="hand2")
        self.especialidad.set("Seleccione su carrera")
        
        self.spin_edad = Spinbox(ventana,
                                 textvariable=edad,
                                 from_=0,
                                 to=100,
                                 increment=1)
        
        self.titulo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.boton.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        self.etiqueta_1.grid(row=1, column=0, padx=10, pady=10)
        self.etiqueta_2.grid(row=2, column=0, padx=10, pady=10)
        self.etiqueta_3.grid(row=3, column=0, padx=10, pady=10)
        self.etiqueta_4.grid(row=4, column=0, padx=10, pady=10)
        
        self.entrada_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.entrada_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        
        self.opciones.grid(row=3, column=1, padx=10, pady=10)
        self.spin_edad.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        
        
        mainloop()
                
    def datos(self):
        nombre = self.entrada_nombre.get()
        apellido = self.entrada_apellido.get()
        carrera = self.especialidad.get()
        
        print("Registro Exitoso!")
        
        messagebox.showinfo("Registro", f"El alumno {nombre} {apellido}, de la carrera {carrera} ha sido registrado con exito")
        
Gui()
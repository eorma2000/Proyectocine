from tkinter import *
from Proyectocine.Dialogo.dialogo import *
from Proyectocine.procesosGui.procesosGui import *
from Proyectocine.Ayuda.quienessomos import *
from Proyectocine.Mantenimiento.cliente import *
from Proyectocine.Mantenimiento.pelicula import *
from Proyectocine.Mantenimiento.empleado import *



class Panelm():
    def __init__(self, titulo=None):
        self.obC = ProcesosGui()
        self.getWindows(titulo)
        self.getMarco()
        self.getlabel()
        self.getButtons()
        self.ventana.mainloop()

    def getWindows(self, titulo=None):
        self.ventana = Tk()
        self.ventana.iconbitmap("C:\\Users\\Hector\\PycharmProjects\\Proyectocine\\Proyectocine\\logo.ico")
        self.obC.center(self.ventana, 425, 410)
        self.ventana.config(bg="#2271B3")
        self.ventana.title("Uso de personal autorizado")
        self.ventana.resizable(0, 0)

    def getlabel(self):
        eti1 = Label(self.ventana, fg="black", bg="black", font=("courier", 26, "italic", "bold"),
                     text="------------------").place(x=20, y=20)
        eti2 = Label(self.ventana, fg="white", bg="black", font=("courier", 20, "italic", "bold"),
                     text="PANEL DE MANTENIMIENTO").place(x=29, y=20)

    def getMarco(self):
        self.marco = Frame(self.ventana,bd=7,bg="#3D403D", highlightthickness=11, highlightbackground="silver")
        self.marco.pack(fill="both",expand=2)
        self.marco.config(cursor="star")
        self.marco.config(bd=11)
        self.marco.config(relief="ridge")

    def getButtons(self):
        # BOTON SALIR
        self.Empleado = Button(self.ventana, relief="flat", text="Empleado", bg="#B07CDA", font=("Century", 16),
                            fg="black", cursor="hand1", command=self.empleado).place(x=118, y=98, width=189,height=65)
        self.Cliente = Button(self.ventana, relief="flat", text="Cliente", bg="#3BC6B6", font=("Century", 16),
                            fg="black", cursor="hand1", command=self.cliente).place(x=118, y=198, width=189,height=65)
        self.Pelicula = Button(self.ventana, relief="flat", text="Pelicula", bg="#6BA7D6", font=("Century", 16),
                             fg="black", cursor="hand1", command=self.pelicula).place(x=118, y=298, width=189,height=65)


    def empleado(self):
        empleado = RegistroEmpleado()

    def cliente(self):
        cliente = RegistroCliente()

    def pelicula(self):
        pelicula = RegistroPelicula()





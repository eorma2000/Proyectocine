from tkinter import *
from Proyectocine.Dialogo.dialogo import *
from Proyectocine.procesosGui.procesosGui import *
from Proyectocine.Ayuda.quienessomos import *
from Proyectocine.Mantenimiento.Panelmantenimiento import *
from Proyectocine.Factura.factura import *
from Proyectocine.Gestion.Panelgestion import *
from Proyectocine.Dominio.entidades import *

class MenuApp:

    def __init__(self, obj=None):
        titulo=""
        if obj!=None:
            self.objU=obj
            titulo = "Usuario: "+obj.nombre+"."
        self.obC = ProcesosGui()
        self.getWindows(titulo)
        self.getMenu()
        self.getMarco()
        self.Labels()
        self.getButtons()
        self.ventana.mainloop()


    def getWindows(self, titulo=None):
        self.ventana = Tk()
        self.ventana.iconbitmap("C:\\Users\\Hector\\PycharmProjects\\Proyectocine\\Proyectocine\\logo.ico")
        self.ventana.config(bg="#3D403D")
        self.ventana.title("---Bienvenidos---al sistema de control de cine")
        self.obC.center(self.ventana, 748, 550)
        self.ventana.resizable(0, 0)

    def getMarco(self):
        self.marco = Frame(self.ventana,bd=7,bg="#3D403D", highlightthickness=11, highlightbackground="silver")
        self.marco.pack(fill="both",expand=2)
        self.marco.config(cursor="star")
        self.marco.config(bd=11)
        self.marco.config(relief="ridge")

    def Labels(self):
        eti1 = Label(self.ventana, fg="black", bg="black", font=("courier", 30, "italic", "bold"),
                     text="-----------------------------").place(x=22, y=20)
        eti2 = Label(self.ventana, fg="white", bg="black", font=("courier", 25, "italic", "bold"),
                     text="SISTEMA DE CONTROL DE CINE").place(x=105, y=20)
        eti3 = Label(self.ventana, fg="#2271B3", bg="#2271B3", font=("courier", 30, "italic", "bold"),
                     text="-----------------------------").place(x=22, y=71)
        eti4 = Label(self.ventana, fg="black", bg="#2271B3", font=("courier", 25, "italic", "bold"),
                     text="Panel de control").place(x=200, y=71)


    def getMenu(self):
        self.menuP = Menu(self.ventana)
        self.ventana.config(menu=self.menuP)
        # INCIO
        self.items = Menu(self.menuP)
        self.menuP.add_cascade(label="INCIO", menu=self.items, font=("courier", 30, "italic", "bold"))
        self.items.add_command(label="CERRAR SESIÓN", command=self.ventana.destroy)
        # MANTENIMIENTO
        self.item2 = Menu(self.menuP)
        self.menuP.add_cascade(label="AYUDA", menu=self.item2)
        self.item2.add_cascade(label="NOSOTROS", command=self.ayuda)


    def ayuda(self):
        ayuda = Help()

    def getButtons(self):
        # BOTONES
        self.Registro = Button(self.ventana, relief="flat", text="GESTIÓN", bg="silver",
                               font=("Century", 16),fg="black", cursor="hand1", command=self.acciong).place(x=210, y=260, width=270, height=66)
        self.Mantenimiento = Button(self.ventana, relief="flat", text="MANTENIMIENTO", bg="silver", font=("Century", 16),
                               fg="black", cursor="hand1", command=self.accionm).place(x=210, y=159, width=270,height=66)
        self.Funciones = Button(self.ventana, relief="flat", text="FACTURA", bg="silver", font=("Century", 16),
                            fg="black", cursor="hand1", command=self.accionf).place(x=210, y=359, width=270,height=66)


    def accionm(self):
        accion= Panelm()

    def accionf(self):
        fac=Factura()

    def acciong(self):
        gestion = Panelg()

    """
    def accionm(self):
      
        # self.cont=self.cont + 1
        # print("Contador: ",self.cont)
        dial = Dialogo()
        if self.usuario.get() == "Proyectocine" and self.contraseña.get() == "12345":
            self.ventana.destroy()
            menu1 = MenuApp()
            # self.msg="Usuario loguedo!"
        else:
            self.dial.setValues("Advertencia", 250, 150)
            self.dial.setMensaje("Usuario Invalido!")
            # self.dial.getDialogo()
        
    #def accion(self):
        #print("opcion 1")



    def nuevo(self):
        print("opcion 2")


"""


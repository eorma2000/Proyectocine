from tkinter import *
from Proyectocine.procesosGui.procesosGui import *
from Proyectocine.Dialogo.dialogo import *
from Proyectocine.Dao.crud import *
from Proyectocine.Entidades.entidades import *
import tkinter as tk


class RegistroCliente():

    def __init__(self,titulo =None):
        self.crud = CrudClientes()
        self.obC = ProcesosGui()
        self.dlg = Dialogo()
        self.getWindow(titulo)
        self.getMarco()
        self.getLabels()
        self.getInputs()
        self.getButtons()
        self.activate("disable", DISABLED)


    def getWindow(self,titulo=None):
        self.ven1 = Toplevel()
        self.ven1.iconbitmap("C:\\Users\\Hector\\PycharmProjects\\Proyectocine\\Proyectocine\\logo.ico")
        self.obC.center(self.ven1,700,450)
        self.ven1.config(bg="#3BC6B6")
        self.ven1.title("REGISTRO DE CLIENTES")
        self.ven1.resizable(0, 0)

    def getMarco(self):
        self.marco = Frame(self.ven1,bd=7,bg="#3BC6B6", highlightthickness=11, highlightbackground="silver")
        self.marco.pack(fill="both",expand=2)
        self.marco.config(cursor="star")
        self.marco.config(bd=11)
        self.marco.config(relief="ridge")


    def getLabels(self):
        posX=120
        eti = Label(self.marco, fg="black", bg="black", font=("courier", 30, "italic", "bold"),
                    text="---------------------------").place(x=0, y=0)
        eti1 = Label(self.marco, fg="white", bg="black", font=("courier", 25, "italic", "bold"),
                     text="REGISTRO CLIENTE").place(x=180, y=0)
        eti2 = Label(self.marco,fg="black",bg="#3BC6B6",text="C.I:",
                     font=("italic",18, "bold")).place(x=posX,y=100)

        eti3 = Label(self.marco,fg="black",bg="#3BC6B6",text="CONTRASEÑA:",
                     font=("italic",18, "bold")).place(x=posX,y=155)

        eti4 = Label(self.marco,fg="black",bg="#3BC6B6",text="NOMBRE:",
                     font=("italic",18, "bold")).place(x=posX,y=210)

        eti5 = Label(self.marco,fg="black",bg="#3BC6B6",text="CORREO:",
                     font=("italic",18, "bold")).place(x=posX,y=265)

    def getInputs(self):
        posX = 350
        self.id_cedula = Entry(self.marco,font=("italic",18))
        self.id_cedula.place(x=posX,y=100,width=180,height=25)

        self.nombre = Entry(self.marco,font=("italic",18))
        self.nombre.place(x=posX,y=200,width=180,height=25)

        self.correo = Entry(self.marco,font=("italic",18))
        self.correo.place(x=posX,y=250,width=180,height=25)

        self.contraseña = Entry(self.marco,font=("italic",18))
        self.contraseña.place(x=posX,y=150,width=180,height=25)


    def getButtons(self):
        self.buscar = Button(self.marco, relief="groove",
                              text="Buscar", bg="#0051C8",
                              font=("Arial",16),fg="white",
                              cursor="hand1",
                              activebackground="#0051C8",
                              activeforeground="White",
                              command=self.getUser
                              )
        self.buscar.place(x=550,y=95, width=90,height=30)

        self.aceptar = Button(self.marco, relief="groove",
                                  text="Guardar", bg="#0051C8",
                                  font=("Arial", 16), fg="white",
                                  cursor="hand1",
                                  activebackground="#0051C8",
                                  activeforeground="White",
                                  command=self.grabar
                                  )
        self.aceptar.place(x=200, y=325,width=110)

        self.cancelar = Button(self.marco, relief="groove",
                                   text="Cancelar", bg="#0051C8",
                                   font=("Arial", 16), fg="white",
                                   activebackground="#0051C8",
                                   activeforeground="White",
                                   cursor="hand1",
                                   command=self.ven1.destroy).place(x=360, y=325,
                                                                    width=110, height=40)
    def grabar(self):
        datos=(self.id_cedula.get(),self.nombre.get(),
               self.correo.get(),self.contraseña.get())
        msg = self.crud.insertCliente("proyectocine",datos)
        self.dlg.setValues("Registro",250,150)
        self.dlg.setMensaje(msg)
        self.dlg.getDialogo()

    def getUser(self):
        datos=(self.id_cedula.get(),)
        obj = self.crud.validateCliente("proyectocine",datos)
        if obj==None:
            self.activate("normal",NORMAL)
        else:
            self.activate("disable",DISABLED)

    def activate(self,estado,estadoB):

        self.nombre['state'] = estado
        self.correo['state']=estado
        self.contraseña['state'] = estado
        self.aceptar.config(state=estadoB)

from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, END, HORIZONTAL, Frame, Toplevel
import tkinter
from tkinter import *
import tkinter as tk
from Proyectocine.Menu.menu import *
from Proyectocine.Dialogo.dialogo import *
from Proyectocine.procesosGui.procesosGui import *
from Proyectocine.Dominio.entidades import *
from Proyectocine.Dao.crud import *
import mysql.connector as mc

class Login(Frame):

    def __init__(self, nombre=None):
        self.obC = ProcesosGui()
        self.crud = CrudClientes()
        self.crud2 = CrudEmpleados()
        self.msg = ""
        self.dial = Dialogo()
        self.getWindows(nombre)
        self.getLabels()
        self.getInputs()
        self.getButtons()
        self.ventana.mainloop()

    def getWindows(self, nombre):
        self.ventana = Tk()
        self.ventana.iconbitmap("C:\\Users\\Hector\\PycharmProjects\\Proyectocine\\Proyectocine\\logo.ico")
        self.obC.center(self.ventana, 550, 400)
        self.imagen()

        self.ventana.title(nombre)

        self.ventana.resizable(0, 0)

    def imagen(self):
        self.deslogo = PhotoImage(file=r"C:\Users\Hector\PycharmProjects\Proyectocine\Proyectocine\1.png")
        self.etiqueta6 = Label(self.ventana, image=self.deslogo, bg="black").place(width=550, height=400, x=0, y=0)

    def getMarco(self):
        self.marco = Frame(self.ventana,bd=7,bg="#3D403D", highlightthickness=11, highlightbackground="silver")
        self.marco.pack(fill="both",expand=2)
        self.marco.config(cursor="star")
        self.marco.config(bd=11)
        self.marco.config(relief="ridge")

    def getLabels(self):
        eti3 = Label(self.ventana, fg="white", bg="#3D403D",
                     font=("courier", 18, "italic", "bold"), text="USUARIO").place(x=200, y=120)
        eti4 = Label(self.ventana, fg="white", bg="#3D403D",
                     font=("courier", 18, "italic", "bold"), text="CONTRASEÑA").place(x=190, y=205)

        self.eti5 = Label(self.ventana, fg="white", bg="#3D403D", text="",font=("courier", 18, "italic", "bold"))
        self.eti5.place(x=20, y=350)

    def getInputs(self):
        # INGRESO DE USUARIO POR TECLADO
        self.usuario = Entry(self.ventana, font=("italic", 15))
        self.usuario.place(x=150, y=155)

        # INGRESO DE CONTRASEÑA POR TECLADO
        self.contraseña = Entry(self.ventana, font=("italic", 15))
        self.contraseña.place(x=150, y=235)
        self.contraseña.config(show="►")

    def getButtons(self):
        # BOTONES
        self.Ingresar = Button(self.ventana, relief="flat", text="Ingresar", bg="#4A9746", font=("Century", 16),
                               fg="white", cursor="hand1", command=self.accion1)
        self.Ingresar.place(x=205, y=280, width=110,height=40)
        self.Salir = Button(self.ventana, relief="flat", text="Cancelar", bg="#B81616", font=("Century", 16),
                            fg="white", cursor="hand1", command=self.ventana.destroy)
        self.Salir.place(x=205, y=330, width=110,height=40)


    def accion1(self):
        datos = (self.usuario.get(), self.contraseña.get())
        obj = self.crud.getLogin("proyectocine", datos)
        obj2 = self.crud2.getLogin("proyectocine", datos)
        self.dialogo1 = Dialogo()
        self.dialogo1.setValues("Atención!", 150, 260)
        if obj!=None or obj2!=None:
              self.msg1 = "Usuario logueado!"
              self.eti5["text"] = self.msg1
              self.ventana.iconify()
              self.usuario.delete(0, END)
              self.contraseña.delete(0, END)
              #self.ventana.destroy()
              menu1 = MenuApp(obj)

        else:
              self.eti5["text"] = self.msg
              self.msg1 = "Verificando...!"
              self.dialogo1.setValues("Atención!", 350, 200)
              self.dialogo1.setMensaje("Usuario invalido")
              self.dialogo1.getDialogo()


vent = Login("Proyectocine")

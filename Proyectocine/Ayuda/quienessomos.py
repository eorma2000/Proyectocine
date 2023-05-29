from tkinter import *
from Proyectocine.Dialogo.dialogo import *
from Proyectocine.Menu.menu import *
from Proyectocine.procesosGui.procesosGui import *


class Help():
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
        self.obC.center(self.ventana, 427, 410)
        self.ventana.config(bg="#128187")
        self.ventana.title("Contactanos para poder ayudarte")
        self.ventana.resizable(0, 0)

    def getlabel(self):
        eti1 = Label(self.ventana, fg="black", bg="black", font=("courier", 25, "italic", "bold"),
                     text="----------------------------------------------").place(x=0, y=0)
        eti2 = Label(self.ventana, fg="white", bg="black", font=("courier", 20, "italic", "bold"),
                     text="SISTEMA DE CINE").place(x=76, y=2)
        eti3 = Label(self.ventana, fg="black", bg="#128187", font=("courier", 15, "italic", "bold"),
                     text="AUTORES").place(x=149, y=65)
        eti4 = Label(self.ventana, fg="black", bg="#128187", font=("courier", 14, "italic"),
                     text="EMILY GABRIELA ORTEGA MATA").place(x=16,y=110)
        eti5 = Label(self.ventana, fg="black", bg="#128187", font=("courier", 14, "italic"),
                     text="CRISTOPHER ANDRES MARTINEZ ESPINOZA").place(x=16,y=155)
        eti6 = Label(self.ventana, fg="black", bg="#128187", font=("courier", 15, "italic", "bold"),
                     text="CONTACTOS").place(x=149, y=220)
        eti7 = Label(self.ventana, fg="black", bg="#128187", font=("courier", 14, "italic"),
                     text="emgortega@est.itsgg.edu.ec").place(x=16, y=265)
        eti8 = Label(self.ventana, fg="black", bg="#128187", font=("courier", 14, "italic"),
                     text="cramartinez@est.itsgg.edu.ec").place(x=16, y=310)


    def getButtons(self):
        # BOTON SALIR
        self.Salir = Button(self.ventana, relief="flat", text="Salir", bg="#B81616", font=("Century", 16),
                            fg="white", cursor="hand1", command=self.ventana.destroy).place(x=167, y=340)

    def getMarco(self):
        self.marco = Frame(self.ventana,bd=7,bg="#128187", highlightthickness=6, highlightbackground="silver")
        self.marco.pack(fill="both",expand=2)
        self.marco.config(cursor="star")
        self.marco.config(bd=11)
        self.marco.config(relief="ridge")





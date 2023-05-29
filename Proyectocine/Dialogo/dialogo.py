from tkinter import*
from Proyectocine.procesosGui.procesosGui import *

class Dialogo:

    def __init__(self):
        self.titulo=""
        self.ancho =0
        self.alto =0
        self.__mensaje =""
        self.obC = ProcesosGui()



    def getDialogo(self):
        self.dlg = Toplevel()
        self.obC.center(self.dlg,self.ancho,self.alto)
        self.dlg.title(self.titulo)
        self.dlg.resizable(0,0)
        self.dlg.config(bg="silver")
        eti1 = Label(self.dlg, fg="black", bg="silver",
                     font=("Century", 14, "bold"), text=self.getMensaje()
                     ).place(x=24, y=30)
        self.aceptar = Button(self.dlg,relief="flat",text="Aceptar", bg="#0051C8",
                              font =("Century",13, "bold"),command=self.dlg.destroy,
                              fg="white",cursor="hand1").place(x=65,y=90,width=125,height=43)



    def setValues(self,titulo,ancho,alto):
        self.titulo= titulo
        self.ancho= ancho
        self.alto= alto

    def setMensaje(self,msg):
        self.__mensaje= msg

    def getMensaje(self):
        return self.__mensaje


class About:

    def __init__(self):
        self.titulo=""
        self.ancho =0
        self.alto =0
        self.n_letra=5
        self.__mensaje =""
        self.obC = ProcesosGui()

    def getAbout(self):
        self.dlg = Toplevel()
        self.obC.center(self.dlg,self.ancho,self.alto)
        self.dlg.title(self.titulo)
        self.dlg.resizable(0,0)
        self.dlg.config(bg="silver")
        eti1 = Label(self.dlg, fg="black", bg="silver",
                     font=("Tahoma", self.n_letra), text=self.getMensaje()
                     ).place(x=10, y=30)
        self.aceptar = Button(self.dlg,relief="flat",
                              text="Aceptar", bg="#0051C8",
                              font =("Tahoma",16),command=self.dlg.destroy,
                              fg="white",cursor="hand1").place(x=80,y=140,
                                                            width=90)


    def setAbaut(self,titulo,ancho,alto,n_letra):
        self.titulo= titulo
        self.ancho= ancho
        self.alto= alto
        self.n_letra=n_letra

    def setMensaje(self,msg):
        self.__mensaje= msg

    def getMensaje(self):
        return self.__mensaje
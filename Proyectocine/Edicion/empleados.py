from tkinter import *
from Proyectocine.Dialogo.dialogo import *
from Proyectocine.procesosGui.procesosGui import *
from Proyectocine.Dominio.entidades import*
from Proyectocine.Dao.crud import *
import tkinter as tk


class EdicionEmpleado:

    def __init__(self, obj=None):
        titulo = "Editar empleado: "+ obj.nombre_empleado+" "+ obj.correo_empleado +"."
        self.crud = CrudEmpleados()
        self.obC = ProcesosGui()
        self.dlg = Dialogo()
        self.getWindow(titulo)
        self.getLabels()
        self.getButtons()
        self.getInputs()



        if obj != None:
            self.cargarDatos(obj)

        self.activate("disable", DISABLED)
        self.ven1.mainloop()




    def getWindow(self, titulo=None):
        self.ven1 = tk.Toplevel()
        self.obC.center(self.ven1, 650, 380)
        self.ven1.config(bg="#B07CDA")
        self.ven1.title(titulo)
        self.ven1.iconbitmap("C:\\Users\\Hector\\PycharmProjects\\Proyectocine\\Proyectocine\\logo.ico")
        self.ven1.resizable(0, 0)




    def getLabels(self):
        posX=70
        tam = 14
        eti45 = Label(self.ven1, fg="black", bg="black", font=("courier", 30, "italic", "bold"),
                    text="---------------------------").place(x=0, y=0)
        eti45 = Label(self.ven1, fg="white", bg="black", font=("courier", 25, "italic", "bold"),
                     text="EDITAR EMPLEADOS").place(x=135, y=0)
        eti1 = Label(self.ven1, fg="white",
                     bg="#B07CDA", text="Cedula:",
                     font=("Calibri", tam)).place(x=posX, y=73)
        eti2 = Label(self.ven1, fg="white",
                     bg="#B07CDA", text="Nombres:",
                     font=("Calibri", tam)).place(x=posX, y=123)
        eti3 = Label(self.ven1, fg="white",
                     bg="#B07CDA", text="Correo:",
                     font=("Calibri", tam)).place(x=posX, y=173)
        eti4 = Label(self.ven1, fg="white",
                     bg="#B07CDA", text="Contraseña:",
                     font=("Calibri", tam)).place(x=posX, y=223)



    def getInputs(self):
        # ENTRY PARA VENTANA DE REGISTRO DE CLIENTES
        posenX=230
        self.id_cedula_empleado = Entry(self.ven1, font=("Calibri", 14))
        self.id_cedula_empleado.place(x=posenX, y=75)

        self.nombre_empleado = Entry(self.ven1, font=("Calibri", 14))
        self.nombre_empleado.place(x=posenX, y=125)

        self.correo_empleado = Entry(self.ven1, font=("Calibri", 14))
        self.correo_empleado.place(x=posenX, y=175)

        self.contraseña_empleado = Entry(self.ven1, font=("Calibri", 14))
        self.contraseña_empleado.place(x=posenX, y=225)


    def getButtons(self):
        #BOTON DE BUSCAR

        self.eliminare = Button(self.ven1,
                               relief="groove",
                               text="Eliminar",
                               bg="#B81616",
                               font=("Calibri Bold", 14),
                               fg="White",
                               cursor="hand1",
                               activebackground="#B81616",
                               activeforeground="White",
                               command=self.eliminar)
        self.eliminare.place(x=460, y=75, width=100, height=30)

        # BOTON DE GRABAR

        self.actualizare = Button(self.ven1,
                              relief="groove",
                              text="Actualizar",
                              bg="#0051C8",
                              font=("Calibri Bold", 14),
                              fg="White",
                              cursor="hand1",
                              activebackground="#0051C8",
                              activeforeground="White",
                              command=self.actualizarEmpl)
        self.actualizare.place(x=460, y=115, width=100, height=30)

        # BOTON DE CANCELAR

        self.cancelar1 = Button(self.ven1,
                              relief="groove",
                              text="Cancelar",
                              bg="#0394fc",
                              font=("Calibri Bold", 14),
                              fg="White",
                              cursor="hand1",
                              activebackground="#03f4fc",
                              activeforeground="White",
                              command=self.ven1.destroy
                              ).place(x=460, y=155, width=100, height=30)


    def actualizarEmpl(self):
        datos = (self.nombre_empleado.get(),
                self.correo_empleado.get(),
                self.contraseña_empleado.get(),
                self.id_cedula_empleado.get())
        msg = self.crud.updateEmpleado("proyectocine", datos)
        self.dlg.setMensaje(msg)
        self.dlg.setValues("Atención! ", 350, 200)
        self.dlg.getDialogo()

    def eliminar(self):
        datos = (self.id_cedula_empleado.get(),)
        msg = self.crud.deleteEmpleado("proyectocine", datos)
        self.dlg.setMensaje(msg)
        self.dlg.setValues("Atención! ", 350, 200)
        self.dlg.getDialogo()


    def vaciar(self):
        self.id_cedula_empleado.delete(0, END)
        self.nombre_empleado.delete(0, END)
        self.correo_empleado.delete(0, END)
        self.contraseña_empleado.delete(0, END)

    def cargarDatos(self, obj):
        self.vaciar()
        self.id_cedula_empleado.insert(0, obj.id_cedula_empleado)
        self.nombre_empleado.insert(0, obj.nombre_empleado)
        self.correo_empleado.insert(0, obj.correo_empleado)
        self.contraseña_empleado.insert(0, obj.contraseña_empleado)


    def activate(self, estado, estadoA):

        self.id_cedula_empleado['state'] = estado
        self.id_cedula_empleado.config(state=estadoA)


#obP = EdicionCliente()


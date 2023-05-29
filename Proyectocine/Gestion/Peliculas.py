from tkinter import *
from tkinter import ttk
import tkinter as tk
from Proyectocine.Edicion.peliculas import *
from Proyectocine.procesosGui.procesosGui import *
from Proyectocine.Dominio.entidades import *
from Proyectocine.Dao.crud import *
from Proyectocine.procesosGui.proceso import *

class Gpeliculas():

    def __init__(self, titulo=None):
        self.cade = Cadenas()
        self.clk = 0
        self.nfila = [-1, -1]
        self.crud = CrudPeliculas()
        self.lista = self.crud.getAllPelicula("proyectocine")
        self.obC = ProcesosGui()
        self.getWindow(titulo)
        self.getMarco()
        self.getLabels()
        self.getButtons()
        self.setEntry()
        self.Registro()
        self.Busque()
        self.ShowTable(self.lista)
        self.ven1.mainloop()

    # VENTANA
    def getWindow(self, titulo=None):
        self.ven1 = tk.Toplevel()
        self.obC.center(self.ven1, 700, 400)
        self.ven1.config(bg="#6BA7D6")
        self.ven1.title(titulo)
        self.ven1.iconbitmap("C:\\Users\\Hector\\PycharmProjects\\Proyectocine\\Proyectocine\\logo.ico")
        self.ven1.resizable(0, 0)


    def getMarco(self):
        self.marco = Frame(self.ven1,bd=7,bg="#6BA7D6", highlightthickness=11, highlightbackground="silver")
        self.marco.pack(fill="both",expand=2)
        self.marco.config(cursor="star")
        self.marco.config(bd=11)
        self.marco.config(relief="ridge")

    def getLabels(self):
        eti = Label(self.ven1, fg="black", bg="black", font=("courier", 30, "italic", "bold"),
                    text="---------------------------").place(x=22, y=20)
        eti1 = Label(self.ven1, fg="white", bg="black", font=("courier", 25, "italic", "bold"),
                     text="GESTIÓN EMPLEADOS").place(x=180, y=20)
        eti2 = Label(self.ven1, fg="black",bg="#6BA7D6",text="Ingrese Código:",font=("Calibri", 15)).place(x=80, y=90)

    def getButtons(self):
        # BOTÓN DE REGISTRO
        self.registro = Button(self.ven1,
                               relief="groove",
                               text="Refrescar",
                               bg="#0051C8",
                               font=("Calibri Bold", 18),
                               fg="White",
                               cursor="hand1",
                               activebackground="#0051C8",
                               activeforeground="White",
                               command=lambda: self.Actualizar()).place(x=335, y=327, width=106, height=38)

        self.buscar = Button(self.ven1,
                             relief="groove",
                             text="Buscar",
                             bg="#0051C8",
                             font=("Calibri Bold", 18),
                             fg="White",
                             cursor="hand1",
                             activebackground="#0051C8",
                             activeforeground="White",
                             command=self.filtro)
        self.buscar.place(x=420, y=82, width=100, height=35)

        # BOTÓN DE CANCELAR
        self.cancelar = Button(self.ven1,
                               relief="groove",
                               text="Cancelar",
                               bg="#0051C8",
                               font=("Calibri Bold", 18),
                               fg="White",
                               cursor="hand1",
                               activebackground="#0051C8",
                               activeforeground="White",
                               command=lambda: self.ven1.destroy()).place(x=460, y=327, width=106, height=38)


    def setEntry(self):
        self.validate1 = self.ven1.register(self.validarCodigo)
        self.codigo = Entry(self.ven1, font=("Calibri", 12), validate="key",
                            validatecommand=(self.validate1, "%d", "%S", "%s"))
        self.codigo.place(x=250, y=90)

    def Registro(self):
        pass

    def Busque(self):
        pass

    def ShowTable(self, lista=None):
        self.tabla = ttk.Treeview(self.ven1, columns=(1, 2, 3, 4, 5),
                                  show="headings",
                                  height=8, )
        self.tabla.bind("<1>", self.onClick)
        # SCROLLBAR
        vsb = ttk.Scrollbar(self.ven1,
                            orient="vertical",
                            command=self.tabla.yview)
        vsb.place(x=605, y=129, height=185)
        self.tabla.configure(yscrollcommand=vsb.set)

        estilo = ttk.Style()
        estilo.theme_use("vista")
        estilo.configure("Treeview.Heading", bg="0051C8")
        # ANCHO DE LAS COLUMNAS
        self.tabla.column(1, anchor=CENTER, width=50)
        self.tabla.column(2, anchor=CENTER, width=90)
        self.tabla.column(3, anchor=CENTER, width=130)
        self.tabla.column(4, anchor=CENTER, width=140)
        self.tabla.column(5, anchor=CENTER, width=120)


        # AQUÍ LE PONEMOS DATOS A NUESTRA TABLA

        tupla2 = ("Id", "Código", "Título", "Categoría", "Fecha de estreno")

        for i in range(len(tupla2)):
            self.tabla.heading((i + 1), text=tupla2[i])

        for i in range(len(tupla2)):
            self.tabla.column((i + 1), anchor=CENTER)

        for i in range(len(lista)):
            self.tabla.insert("", "end", values=(str(i + 1),
                                                 lista[i].id_codigo,
                                                 lista[i].titulo,
                                                 lista[i].categoria,
                                                 lista[i].fecha_estreno))


        self.tabla.place(x=80, y=128)

    def onClick(self, event):
        item = event.widget.identify("item", event.x, event.y)
        text = self.cade.getCadena(item)
        if text != "":
            self.clk += 1
            posi = int(text)
            if self.clk == 1:
                self.nfila[0] = posi
            if self.clk == 2:
                self.nfila[1] = posi
                self.clk = 0

            if self.clk == 0 and self.nfila[0] == self.nfila[1]:
                frm = EdicionPelicula(self.lista[posi - 1])
        else:
            self.clk = 0

    def validarCodigo(self, accion, user, texto):
        if accion != "1":
            return True
        return user in "1234567890" and len(texto) < 10

    def filtro(self):

        datos = (self.codigo.get(),)
        self.lista = self.crud.filterPelicula("proyectocine", datos)
        if self.lista != []:
            self.ShowTable(self.lista)
            self.codigo.delete(0, END)
        else:
            self.lista = self.crud.getAllPelicula("proyectocine")
            self.ShowTable(self.lista)

    def Actualizar(self):
        self.lista = self.crud.getAllPelicula("proyectocine")
        self.ShowTable(self.lista)
from tkinter import *
from Proyectocine.procesosGui.procesosGui import *
from Proyectocine.Dialogo.dialogo import *
import random


class Factura():

    def __init__(self,titulo =None):
        #self.crud = CrudUsuario()
        self.obC = ProcesosGui()
        self.dlg = Dialogo()
        self.getWindow(titulo)
        self.Variables()
        self.getMarco()
        self.getLabels()
        self.getButtons()
        #self.activate("disable",DISABLED)

    def getWindow(self,titulo=None):
        self.ven1 = Toplevel()
        self.ven1.iconbitmap("C:\\Users\\Hector\\PycharmProjects\\Proyectocine\\Proyectocine\\logo.ico")
        self.obC.center(self.ven1,1032,640)
        self.ven1.config(bg="#128187")
        self.ven1.title("VENTANA DE FACTURACIÓN ")
        self.ven1.resizable(0, 0)


    def Variables(self):
        # ====================Variables========================#
        self.ci = IntVar()
        self.nombre = StringVar()
        self.telefono = StringVar()
        self.email = StringVar()
        self.ciudad = StringVar()
        self.npelicula = StringVar()
        self.genero = StringVar()
        self.sala = StringVar()
        self.asientos = StringVar()
        self.fecha = StringVar()
        self.hora = StringVar()
        self.general = IntVar()
        self.tresD = IntVar()
        self.premium = IntVar()
        self.discapacidad = IntVar()
        self.promocion = IntVar()

        self.total_pagar = StringVar()
        self.t_iva= StringVar()
        self.total = StringVar()




    def getMarco(self):
        self.marco = Frame(self.ven1,bd=7,bg="#128187", highlightthickness=11, highlightbackground="silver")
        self.marco.pack(fill="both",expand=2)
        self.marco.config(cursor="star")
        self.marco.config(bd=11)
        self.marco.config(relief="ridge")




    def getLabels(self):
        eti = Label(self.marco, fg="black", bg="black", font=("courier", 32, "italic", "bold"),
                    text="--------------------------------------").place(x=0, y=0)
        eti1 = Label(self.marco, fg="white", bg="black", font=("courier", 25, "italic", "bold"),
                     text="FACTURA").place(x=395, y=0)
        # ===============DATOS CLIENTES===========#
        F1 = Label(self.marco,bg="#128187", text = "DATOS DEL CLIENTE",font = ("time new roman",15,"bold"),fg = "gold").place(x = 0,y = 80)
        # ===============Nombre del cliente===========#
        cname_lbl = Label(self.marco, bg="#128187",text="C.I: ", font=("times new roman", 15, "bold")).place(x =5,y = 119)
        self.ci = Entry(self.marco,F1,textvariable = self.ci)
        self.ci.place(x=100, y=120,width=180,height=25)
        # ===============Telefono===========#
        c_tel = Label(self.marco, bg="#128187", text="Nombre: ", font=("times new roman", 15, "bold")).place(x=5,y=155)
        self.c_nom = Entry(self.marco, F1,textvariable = self.nombre)
        self.c_nom.place(x=100, y=156, width=180, height=25)
        # ===============Correo===========#
        c_email= Label(self.marco, bg="#128187", text="Teléfono: ", font=("times new roman", 15, "bold")).place(x=5,y=191)
        self.c_telefono = Entry(self.marco, F1,textvariable = self.telefono)
        self.c_telefono.place(x=100, y=192, width=180, height=25)

        c_ciudad = Label(self.marco, bg="#128187", text="E-Mail: ", font=("times new roman", 15, "bold")).place(x=5,y=227)
        self.c_email= Entry(self.marco, F1,textvariable = self.email)
        self.c_email.place(x=100, y=228, width=180, height=25)

        c_fechacompra = Label(self.marco, bg="#128187", text="Ciudad: ", font=("times new roman", 15, "bold")).place(x=5,y=263)
        self.c_ciudad = Entry(self.marco, F1,textvariable = self.ciudad)
        self.c_ciudad.place(x=100, y=264, width=180, height=25)

        # ===============DATOS PELICULA===========#
        F2 = Label(self.marco, bg="#128187", text="PELICULA", font=("time new roman", 15, "bold"),fg="gold").place(x=0, y=336)
        # ===============Pelicula===========#
        cpelicula_lbl = Label(self.marco, bg="#128187", text="Nombre: ", font=("times new roman", 15, "bold")).place(x=5, y=372)
        self.n_pelicula = Entry(self.marco, F2,textvariable = self.npelicula)
        self.n_pelicula.place(x=100, y=373, width=180, height=25)
        # ===============genero===========#
        cgenero_lbl = Label(self.marco, bg="#128187", text="Género: ", font=("times new roman", 15, "bold")).place(x=5,y=408)
        self.c_genero= Entry(self.marco, F2,textvariable = self.genero)
        self.c_genero.place(x=100, y=409, width=180, height=25)
        # ===============genero===========#
        cgenero_lbl = Label(self.marco, bg="#128187", text="Sala: ", font=("times new roman", 15, "bold")).place(x=5,y=444)
        self.c_sala = Entry(self.marco, F2,textvariable = self.sala)
        self.c_sala.place(x=100, y=445, width=180, height=25)
        # ===============genero===========#
        cgenero_lbl = Label(self.marco, bg="#128187", text="Asientos: ",font=("times new roman", 15, "bold")).place(x=5, y=480)
        self.c_asientos = Entry(self.marco, F2,textvariable = self.asientos)
        self.c_asientos.place(x=100, y=481, width=180, height=25)
        # ===============genero===========#
        cgenero_lbl = Label(self.marco, bg="#128187", text="Fecha: ", font=("times new roman", 15, "bold")).place(x=5,y=516)
        self.c_fecha = Entry(self.marco, F2,textvariable = self.fecha)
        self.c_fecha.place(x=100, y=517, width=180, height=25)
        # ===============genero===========#
        cgenero_lbl = Label(self.marco, bg="#128187", text="Hora: ", font=("times new roman", 15, "bold")).place(x=5,y=552)
        self.c_hora = Entry(self.marco, F2,textvariable = self.hora)
        self.c_hora.place(x=100, y=553, width=180, height=25)

        # ===============DATOS ENTRADA===========#
        F3 = Label(self.marco, bg="#128187", text="TIPO DE ENTRADA- cantidades", font=("time new roman", 15, "bold"),
                   fg="gold").place(x=325, y=80)
        # ===============Nombre del cliente===========#
        cname_lbl = Label(self.marco, bg="#128187", text="General: ", font=("times new roman", 15, "bold")).place(x=320,y=119)
        self.c_general = Entry(self.marco, F3,textvariable = self.general)
        self.c_general.place(x=460, y=120, width=180, height=25)
        # ===============Telefono===========#
        c_tel = Label(self.marco, bg="#128187", text="3D: ", font=("times new roman", 15, "bold")).place(x=320,y=155)
        self.c_tresD = Entry(self.marco, F3,textvariable = self.tresD)
        self.c_tresD.place(x=460, y=156, width=180, height=25)
        # ===============Correo===========#
        c_email = Label(self.marco, bg="#128187", text="Premium: ", font=("times new roman", 15, "bold")).place(x=320,y=191)
        self.c_premium = Entry(self.marco, F3,textvariable = self.premium)
        self.c_premium.place(x=460, y=192, width=180, height=25)

        c_ciudad = Label(self.marco, bg="#128187", text="Discapacidad: ", font=("times new roman", 15, "bold")).place(x=320,y=227)
        self.c_discapacidad = Entry(self.marco, F3,textvariable = self.discapacidad)
        self.c_discapacidad.place(x=460, y=228, width=180, height=25)

        c_fechacompra = Label(self.marco, bg="#128187", text="Promoción: ", font=("times new roman", 15, "bold")).place(x=320, y=263)
        self.c_promocion = Entry(self.marco, F3,textvariable = self.promocion)
        self.c_promocion.place(x=460, y=264, width=180, height=25)


        F4 = Label(self.marco, bg="#128187", text="RESULTADO", font=("time new roman", 15, "bold"),fg="gold").place(x=325, y=336)

        r_total = Label(self.marco, bg="#128187", text="Total: ", font=("times new roman", 15, "bold")).place(x=325, y=372)
        totalp = Entry(self.marco,F4, textvariable=self.total_pagar)
        totalp.place(x=460, y=373, width=180, height=25)

        r_iva = Label(self.marco, bg="#128187", text="I.V.A: ", font=("times new roman", 15, "bold")).place(x=325, y=408)
        IVA = Entry(self.marco,F4, textvariable=self.t_iva)
        IVA.place(x=460, y=409, width=180, height=25)

        r_total = Label(self.marco, bg="#128187", text="Total a pagar: ", font=("times new roman", 15, "bold")).place(x=325,y=444)
        total = Entry(self.marco, F4, textvariable=self.total)
        total.place(x=460, y=445, width=180, height=25)



        #        Área de Facturación
        F5 = Label(self.marco,bd = 10,relief = GROOVE)
        F5.place(x=665, y=75,width = 325,height = 380)
        #===========
        bill_title = Label(F5,text = "Área de Facturación",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)


        #============
        scroll_y = Scrollbar(F5,orient = VERTICAL)
        self.txt = Text(F5,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)




    def getButtons(self):
        """
        self.buscar = Button(self.marco, relief="flat",
                              text="Buscar", bg="#0051C8",
                              font=("Arial",16),fg="white",
                              cursor="hand1",
                              command=self.getUser
                              )
        self.buscar.place(x=550,y=95, width=90,height=30)

        self.aceptar = Button(self.marco, relief="flat",
                                  text="Guardar", bg="#0051C8",
                                  font=("Arial", 16), fg="white",
                                  cursor="hand1"
                                  ,command=self.grabar
                                  )
        self.aceptar.place(x=200, y=325,width=110)


        bill_btn = Button(self.marco, fg="white", text="INGRESAR", font=("times new roman", 12, "bold"), bg="#0051C8")
        bill_btn.place(x=750, y=490, width=180, height=25)
        """
        btotal = Button(self.marco, fg="white", text="CALCULAR", font=("times new roman", 14, "bold"), command=self.totalfactura, bg="#0051C8")
        btotal.place(x=325, y=505, width=150, height=50)

        bareaf = Button(self.marco, fg="white",text="GENERAR FACT.",font=("times new roman", 14, "bold"),command=self.Areafactura, bg="#0051C8")
        bareaf.place(x=487, y=505, width=180, height=50)

        blimpiar = Button(self.marco, fg="white", text="LIMPIAR", font=("times new roman", 14, "bold"), command=self.Limpiar, bg="#0051C8")
        blimpiar.place(x=680, y=505, width=140, height=50)

        bexit = Button(self.marco, fg="white",text="SALIR",font=("times new roman", 14, "bold"),command=self.ven1.destroy, bg="#0051C8")
        bexit.place(x=830, y=505, width=140, height=50)

    def totalfactura(self):
        #=================Total A Pagar
        self.total_pagar_precios = (
            (self.general.get() * 7)+
            (self.tresD.get() * 12)+
            (self.premium.get() * 18)+
            (self.discapacidad.get() * 3.25)+
            (self.promocion.get() * 2.50)
        )
        self.total_pagar.set(str(self.total_pagar_precios))
        self.t_iva.set(str(round(self.total_pagar_precios*0.12)))
        self.total.set(str(round(self.total_pagar_precios+self.total_pagar_precios*0.12)))


    def texto_f(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Proyecto Cine S.A\n")
        self.txt.insert(END,"-----------------------------------")
        self.txt.insert(END,"\nDatos del cliente\n")
        self.txt.insert(END,"-----------------------------------")
        self.txt.insert(END,f"\nC.I: {str(self.ci.get())}")
        self.txt.insert(END,f"\nNombre  : {str(self.nombre.get())}")
        self.txt.insert(END,f"\nTelefono : {str(self.telefono.get())}")
        self.txt.insert(END,f"\nCorreo  : {str(self.email.get())}")
        self.txt.insert(END,f"\nCiudad : {str(self.ciudad.get())}\n")
        self.txt.insert(END,"-----------------------------------")
        self.txt.insert(END,"\nDatos de la película\n")
        self.txt.insert(END,"-----------------------------------")
        self.txt.insert(END,f"\nPelícula: {str(self.npelicula.get())}")
        self.txt.insert(END,f"\nGénero  : {str(self.genero.get())}")
        self.txt.insert(END,f"\nSala : {str(self.sala.get())}")
        self.txt.insert(END,f"\nAsientos  : {str(self.asientos.get())}")
        self.txt.insert(END,f"\nFecha : {str(self.fecha.get())}")
        self.txt.insert(END,f"\nHora : {str(self.hora.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nPelícula    ||  Cantidad   || Valor")
        self.txt.insert(END,"\n===================================")

    def Limpiar(self):
        self.txt.delete('1.0',END)

    def Areafactura(self):
        self.texto_f()
        if self.general.get() != 0:
            self.txt.insert(END,f"\nGeneral     ||   {self.general.get()}         || {self.general.get() * 5.00}")
        if self.tresD.get() != 0:
            self.txt.insert(END,f"\n3D          ||   {self.tresD.get()}         || {self.tresD.get() * 12.00}")
        if self.premium.get() != 0:
            self.txt.insert(END,f"\nPremium     ||   {self.premium.get()}         || {self.premium.get() * 18.00}")
        if self.discapacidad.get() != 0:
            self.txt.insert(END,f"\nDiscapacidad||   {self.discapacidad.get()}         || {self.discapacidad.get() * 3.00}")
        if self.promocion.get() != 0 :
            self.txt.insert(END,f"\nPromoción   ||   {self.promocion.get()}         || {self.promocion.get() * 2.50}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : {self.total_pagar_precios+self.total_pagar_precios * 0.14}")


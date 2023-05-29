from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, END, HORIZONTAL, Frame, Toplevel
import tkinter as tk
import time
from Proyectocine.Menu.menu import *
from Proyectocine.Dialogo.dialogo import *
from Proyectocine.procesosGui.procesosGui import *
from Proyectocine.Dominio.entidades import *
from Proyectocine.Dao.crud import *
import mysql.connector as mc



class Login(Frame):
    def _init_(self, master, *args):
        super()._init_(master, *args)
        self.user_marcar = "Ingrese su correo"
        self.contra_marcar = "Ingrese su contraseña"
        self.fila1 = ''
        self.fila2 = ''
        self.imagen()
        self.entrys()
        self.Windows()
        self.crud = CrudClientes()
        self.crud2 = CrudEmpleados()
        self.msg = ""
        self.dial = Dialogo()

    def Windows(self):
        self.ventana = Tk()
        self.ventana.config(bg='black')
        self.ventana.geometry('500x500+400+50')
        # ventana.overrideredirect         #para quitarle el borde a la ventana
        self.ventana.title()
        self.ventana.resizable(0, 0)
        self.app.mainloop()


    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) == 0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
        if self.entry2.get() != 'Ingrese su contraseña':
            self.entry2['show'] = ""
        if self.entry2.get() != 'Ingrese su correo':
            self.entry2['show'] = "*"

    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)

        if self.entry2.get() != 'Ingrese su contraseña':
            self.entry2['show'] = "*"

        if self.entry2.get() == 'Ingrese su contraseña':
            self.entry2['show'] = ""

    def salir(self):
        self.master.destroy()
        self.master.quit()

    def acceder_ventana_dos(self):
        for i in range(101):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.02)

        self.master.withdraw()
        self.ventana_dos = Toplevel()
        self.ventana_dos.title('Segunda Ventana')
        self.ventana_dos.geometry('500x500+400+80')
        self.ventana_dos.protocol("WM_DELETE_WINDOW", self.salir)
        self.ventana_dos.config(bg='white')
        self.ventana_dos.state('zoomed')

        Label(self.ventana_dos, text='VENTANA DOS', font='Arial 40', bg='white').pack(expand=True)
        Button(self.ventana_dos, text='Salir', font='Arial 10', bg='red', command=self.salir).pack(expand=True)

    def verificacion_users(self):
        self.indica1['text'] = ''
        self.indica2['text'] = ''
        users_entry = self.entry1.get()
        password_entry = self.entry2.get()

        if users_entry != self.user_marcar or self.contra_marcar != password_entry:
            users_entry = str("'" + users_entry + "'")
            password_entry = str("'" + password_entry + "'")

            dato1 = self.datos.busca_users(users_entry)
            dato2 = self.datos.busca_password(password_entry)

            self.fila1 = dato1
            self.fila2 = dato2

            if self.fila1 == self.fila2:
                if dato1 == [] and dato2 == []:
                    self.indica2['text'] = 'Contraseña incorrecta'
                    self.indica1['text'] = 'Usuario incorrecto'
                else:

                    if dato1 == []:
                        self.indica1['text'] = 'Usuario incorrecto'
                    else:
                        dato1 = dato1[0][1]

                    if dato2 == []:
                        self.indica2['text'] = 'Contraseña incorrecta'
                    else:
                        dato2 = dato2[0][2]

                    if dato1 != [] and dato2 != []:
                        self.acceder_ventana_dos()
            else:
                self.indica1['text'] = 'Usuario incorrecto'
                self.indica2['text'] = 'Contraseña incorrecta'

    def imagen(self):
        self.deslogo = PhotoImage(file=r"C:\Users\Hector\PycharmProjects\Proyectocine\peli-removebg-preview.png")
        self.etiqueta6 = Label(self.master, image=self.deslogo, bg="black").place(width=800, height=430, x=30, y=170)


    def entrys(self):
        #letra de correo
        self.entry1 = Entry(self.master, font=('Comic Sans MS', 13), justify='center', fg='grey', bg= "#565151")
        self.entry1.insert(0, self.user_marcar)
        self.entry1.bind("<FocusIn>", lambda args: self.entry_in(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: self.entry_out(self.entry1, self.user_marcar))
        self.entry1.place(x=40,y=140)#pack(pady=4)
        self.indica1 = Label(self.master, bg='black', fg='black', font=('Arial', 8, 'bold'))
        self.indica1.pack(pady=2)

        # contraseña y entry
        #Label(self.master, text='INICIO', bg='black', fg='white', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        eti1= Label(self.master, fg="white", bg="black",
                font=("Arial", 35, "bold"), text="INICIAR SESION").place(x=27, y=50)
        self.entry2 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey', bg= "#565151")

        self.entry2.insert(0, self.contra_marcar)
        self.entry2.bind("<FocusIn>", lambda args: self.entry_in(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: self.entry_out(self.entry2, self.contra_marcar))
        self.entry2.place(x= 40, y=180)#pack(pady=4)

        self.indica2 = Label(self.master, bg='black', fg='black', font=('Arial', 8, 'bold'))
        self.indica2.pack(pady=2)


        #Iniciar Sesion boton
        Button(self.master, text='Iniciar Sesion', fg= "white", command=self.accion1, activebackground='silver', # para darle color al boton cuando se lo pulse
               bg='#D82C16', font=('Arial', 12, 'bold')).place(x=85,y=230)
        # Salir boton
        Button(self.master, text='Salir', bg='silver', activebackground='silver', bd=0, fg='black',
               font=('Lucida Sans', 15, 'italic'), command=self.salir).place(x=110,y=350) #pack(pady=35)

        #barra de progreso
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TProgressbar", foreground='red', background='black', troughcolor='black',
                         bordercolor='white', lightcolor='#970BD9', darkcolor='black')
        self.barra = ttk.Progressbar(self.master, orient=HORIZONTAL, length=230, mode='determinate').place(x=20,y=300)#, maximum=100,style="TProgressbar")
        #self.barra.pack()


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
              #self.ventana.destroy()
              self.usuario.delete(0, END)
              self.contraseña.delete(0, END)
              menu1 = MenuApp(obj)
        else:
              self.eti5["text"] = self.msg
              self.msg1 = "Verificando...!"
              self.dialogo1.setValues("Atención!", 350, 200)
              self.dialogo1.setMensaje("Usuario invalido")
              self.dialogo1.getDialogo()


vent = Login("Proyectocine")

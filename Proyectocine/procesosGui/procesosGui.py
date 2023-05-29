from tkinter import*


class ProcesosGui:

    def center(self, obj, ancho, alto):
        ven_alto = alto
        ven_ancho = ancho
        panta_ancho = obj.winfo_screenwidth()
        panta_alto = obj.winfo_screenheight()
        x_coord = int((panta_ancho / 2) - (ven_ancho / 2))
        y_coord = int((panta_alto / 2) - (ven_alto / 2))
        obj.geometry("{}x{}+{}+{}".format(ven_ancho, ven_alto, x_coord, y_coord))


class Cadenas:

   def getStringNumber(self, valor):
      msg = ""
      for i in range(1, len(valor)):
         msg = msg + valor[i]
      return msg
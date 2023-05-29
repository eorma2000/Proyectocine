class Busqueda:

    def getPosicion(self, p, lista):
        res = -1
        for i in range(len(lista)):
            if p == lista[i].getP():
                res = i
                break
        return res

    def getObject(self, p, lista):
        obj = None
        for i in range(len(lista)):
            if p== lista[i].getP():
                obj = lista[i]
                break
        return obj


class Entradas:

    def inInt(self, cadena):
        x = -1
        while x < 0:
            try:
                x = int(input(cadena))
            except:
                x = -1
                print("Error de valor!")
        return x

    def inFloat(self, cadena):
        x = -1
        while x < 0:
            try:
                x = float(input(cadena))
            except:
                x = -1
                print("Error de valor!")
        return x


class Cadenas:
    def getCadena(self, cadena):
        msg = ""
        for i in range(1, len(cadena)):
            msg = msg + cadena[i]
        return msg
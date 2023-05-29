class Clientes:

    def __init__(self, *param):
        self.id_cedula = param[0]
        self.nombre = param[1]
        self.correo = param[2]
        self.contraseña =  param[3]

    def getData(self):
        return self.id_cedula +" "\
               + self.nombre+""\
                + self.correo+" "\
                + self.contraseña

class Empleado:

    def __init__(self, *param):
        self.id_cedula_empleado = param[0]
        self.nombre_empleado = param[1]
        self.correo_empleado = param[2]
        self.contraseña_empleado =  param[3]

    def getData(self):
        return self.id_cedula_empleado +" "\
               + self.nombre_empleado+""\
                + self.correo_empleado+" "\
                + self.contraseña_empleado


class Peliculas:

    def __init__(self, *param):
        self.id_codigo = param[0]
        self.titulo = param[1]
        self.categoria = param [2]
        self.fecha_estreno = param[3]



    def getData(self):
        return self.id_codigo + " " \
               + self.titulo + "" \
               + self.categoria + " "\
               + self.fecha_estreno + " " \


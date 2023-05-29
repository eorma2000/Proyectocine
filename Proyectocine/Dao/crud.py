from Proyectocine.Entidades.entidades import *
from Proyectocine.Dao.conexion import *
import mysql.connector as mc

class CrudEmpleados:

    def __init__(self):
        self.con = Conexion()

#METODO PARA INSERTAR DATOS EN LA TABLA EMPLEADO

    def insertEmpleado(self, base, datos):
        self.cone = self.con.conectar(base)
        self.cursor1 = self.cone.cursor()
        sql = "insert into empleado(id_cedula_empleado, nombre_empleado, correo_empleado, contraseña_empleado)" + \
                  "values(%s, %s, %s, %s)"
        self.cursor1.execute(sql, datos)
        self.cone.commit()
        self.cone.close()
        return str(self.cursor1.rowcount) + " registro(s) afectados."

# METODO PARA EDITAR DATOS EN LA TABLA EMPLEADO
    def updateEmpleado(self, base, datos):
        msg = ""
        try:
            self.cone = self.con.conectar(base)
            self.cursor1 = self.cone.cursor()
            sql = "update empleado set nombre_empleado=%s, correo_empleado=%s, contraseña_empleado=%s"+ " where id_cedula_empleado=%s "
            self.cursor1.execute(sql, datos)
            self.cone.commit()
            msg = str(self.cursor1.rowcount) + " registro(s) afectados."
            self.cone.close()
        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return str(self.cursor1.rowcount) + " registro(s) afectados."

# METODO PARA ELIMINAR DATOS EN LA TABLA EMPLEADO

    def deleteEmpleado(self, base, datos):
        msg = ""
        try:
            self.cone = self.con.conectar(base)
            self.cursor1 = self.cone.cursor()
            sql = "delete from empleado where id_cedula_empleado=%s"
            self.cursor1.execute(sql, datos)
            self.cone.commit()
            self.cone.close()
            msg = str(self.cursor1.rowcount) + " Registro(s) eliminado(s)."

        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return msg

# METODO PARA VERIFICAR LOGIN EN EMPLEADOS
    def getLogin(self, base, datos):
        obj = None

        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql="select * from empleado where id_cedula_empleado=%s and contraseña_empleado=%s"
        cursor1.execute(sql, datos)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0 :
            obj = Empleados(result[0][0], result[0][1], result[0][2], result[0][3])
        return obj

#METODO PARA VALIDAR EMPLEADOS EN LOGIN
    def validateEmpleado(self, base, datos):
        obj = None
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = "select * from empleado where id_cedula_empleado=%s"
        cursor1.execute(sql, datos)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            obj = Empleados(result[0][0], result[0][1], result[0][2], result[0][3])
            return obj

#MÉTODO PARA FILTRAR EMPLEADOS
    def filterEmpleado(self, base, datos):
        lista = []
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = 'select * from empleado where id_cedula_empleado=%s'
        cursor1.execute(sql, datos)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            for i in range(len(result)):
                obj = Empleados(result[i][0], result[i][1], result[i][2], result[i][3])
                lista.append(obj)
        return lista

#CODIGO PARA LISTAR USUARIOS:

    def getAllEmpleados(self, base):
        lista = []
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = "select * from empleado order by nombre_empleado"
        cursor1.execute(sql)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            for i in range(len(result)):
                obj = Empleados(result[i][0],result[i][1],result[i][2],result[i][3])
                lista.append(obj)
        return lista


class CrudClientes:

    def __init__(self):
        self.con = Conexion()

# METODO PARA INSERTAR DATOS EN LA TABLA CLIENTES

    def insertCliente(self, base, datos):
        self.cone = self.con.conectar(base)
        self.cursor1 = self.cone.cursor()
        sql = "insert into usuario(id_cedula, nombre, correo, contraseña)" + \
              "values(%s, %s, %s, %s)"
        self.cursor1.execute(sql, datos)
        self.cone.commit()
        self.cone.close()
        return str(self.cursor1.rowcount) + " registro(s) afectados."

# METODO PARA EDITAR DATOS EN LA TABLA CLIENTES
    def updateCliente(self, base, datos):
        msg = ""
        try:
            self.cone = self.con.conectar(base)
            self.cursor1 = self.cone.cursor()
            sql = "update usuario set nombre=%s, correo=%s, contraseña=%s" + " where id_cedula=%s "
            self.cursor1.execute(sql, datos)
            self.cone.commit()
            msg = str(self.cursor1.rowcount) + " registro(s) afectados."
            self.cone.close()
        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return str(self.cursor1.rowcount) + " registro(s) afectados."

    # METODO PARA ELIMINAR DATOS EN LA TABLA CLIENTES

    def deleteCliente(self, base, datos):
        msg = ""
        try:
            self.cone = self.con.conectar(base)
            self.cursor1 = self.cone.cursor()
            sql = "delete from usuario where id_cedula=%s"
            self.cursor1.execute(sql, datos)
            self.cone.commit()
            self.cone.close()
            msg = str(self.cursor1.rowcount) + " Registro(s) eliminado(s)."

        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return msg

    # METODO PARA VERIFICAR LOGIN EN CLIENTES
    def getLogin(self, base, datos):
        obj = None

        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = "select * from usuario where id_cedula=%s and contraseña=%s"
        cursor1.execute(sql, datos)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            obj = Clientes(result[0][0], result[0][1], result[0][2], result[0][3])
        return obj

    # METODO PARA VALIDAR CLIENTES EN LOGIN
    def validateCliente(self, base, datos):
        obj = None
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = "select * from usuario where id_cedula=%s"
        cursor1.execute(sql, datos)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            obj = Clientes(result[0][0], result[0][1], result[0][2], result[0][3])
            return obj

    # MÉTODO PARA FILTRAR CLIENTES
    def filterCliente(self, base, datos):
        lista = []
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = 'select * from usuario where id_cedula=%s'
        cursor1.execute(sql, datos)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            for i in range(len(result)):
                obj = Clientes(result[i][0], result[i][1], result[i][2], result[i][3])
                lista.append(obj)
        return lista

    # CODIGO PARA LISTAR CLIENTES

    def getAllCliente(self, base):
        lista = []
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = "select * from usuario order by nombre"
        cursor1.execute(sql)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            for i in range(len(result)):
                obj = Clientes(result[i][0], result[i][1], result[i][2], result[i][3])
                lista.append(obj)
        return lista

class CrudPeliculas:

    def __init__(self):
        self.con = Conexion()

# METODO PARA INSERTAR DATOS EN LA TABLA PELICULAS

    def insertPelicula(self, base, datos):
        self.cone = self.con.conectar(base)
        self.cursor1 = self.cone.cursor()
        sql = "insert into peliculas(id_codigo, titulo, categoria, fecha_estreno)" + \
              "values(%s, %s, %s, %s)"
        self.cursor1.execute(sql, datos)
        self.cone.commit()
        self.cone.close()
        return str(self.cursor1.rowcount) + " registro(s) afectados."

# METODO PARA EDITAR DATOS EN LA TABLA PELICULAS
    def updatePelicula(self, base, datos):
        msg = ""
        try:
            self.cone = self.con.conectar(base)
            self.cursor1 = self.cone.cursor()
            sql = "Update peliculas set titulo=%s, categoria=%s, fecha_estreno=%s" + " where id_codigo=%s "
            self.cursor1.execute(sql, datos)
            self.cone.commit()
            msg = str(self.cursor1.rowcount) + " registro(s) afectados."
            self.cone.close()
        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return str(self.cursor1.rowcount) + " registro(s) afectados."

# METODO PARA ELIMINAR DATOS EN LA TABLA PELICULAS

    def deletePelicula(self, base, datos):
        msg = ""
        try:
            self.cone = self.con.conectar(base)
            self.cursor1 = self.cone.cursor()
            sql = "delete from peliculas where id_codigo=%s"
            self.cursor1.execute(sql, datos)
            self.cone.commit()
            self.cone.close()
            msg = str(self.cursor1.rowcount) + " Registro(s) eliminado(s)."

        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return msg

# MÉTODO PARA FILTRAR CLIENTES

    def filterPelicula(self, base, datos):
        lista = []
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = 'select * from peliculas where id_codigo=%s'
        cursor1.execute(sql, datos)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            for i in range(len(result)):
                obj = Peliculas(result[i][0], result[i][1], result[i][2], result[i][3])
                lista.append(obj)
        return lista

# CODIGO PARA LISTAR PELICULAS

    def getAllPelicula(self, base):
        lista = []
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = "select * from peliculas order by titulo"
        cursor1.execute(sql)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            for i in range(len(result)):
                obj = Peliculas(result[i][0], result[i][1], result[i][2], result[i][3])
                lista.append(obj)
        return lista

    def validatePelicula(self, base, datos):
        obj = None
        cone = self.con.conectar(base)
        cursor1 = cone.cursor()
        sql = "select * from peliculas where id_codigo=%s"
        cursor1.execute(sql, datos)
        result = cursor1.fetchall()
        cone.close()
        if len(result) > 0:
            obj = Peliculas(result[0][0], result[0][1], result[0][2], result[0][3])
            return obj

"""
obcr = CrudEmpleados()
tupla=("1234567891","Gabriel Mata Rodas","hector_7@hotmail.com","12345")
print(obcr.insertEmpleados("proyectocine", tupla))"""
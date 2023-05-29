import mysql.connector as mc

class Conexion:

    def conectar(self,base):
        cone= None
        credenciales= {
            "host" : "Localhost",
            "port" : "3306",
            "user" : "root",
            "password" : "1rm9d31981",
            "database" : base,
            "auth_plugin" : "mysql_native_password"
        }
        try:
            cone = mc.connect(**credenciales)
        except(mc.errors.ProgrammingError, mc.errors.InterfaceError) as ex:
            print(str(ex))
        return cone
#obC = Conexion()
#print(obC.conectar("proyectocine"))


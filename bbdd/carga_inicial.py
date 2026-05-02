import mysql.connector
from mysql.connector import errorcode
from lib.profesor import Profesor


class CargaInicial:
    # a lo mejor se puede poner un init con cursor y conexión
    def _vaciar_bbdd(self):
        conexion, cursor = self._abrir_conexion()
        vaciar = ('TRUNCATE TABLE PROFESORES')
        cursor.execute(vaciar)
        # self._cerrar_conexion(cursor, conexion)

    def _abrir_conexion(self):
        # todo: ponerse el try
        conexion = mysql.connector.connect(user='root', password='',
                                           host='127.0.0.1',
                                           database='gestion_guardias')
        conexion.autocommit = True
        cursor = conexion.cursor()
        # except mysql.connector.Error as err:
        #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #         print("Error de conexión.")
        #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #         print("No existe dicha base de datos.")
        #     else:
        #         print(err)  # esto me saca el error como es
        return conexion, cursor

    def _generar_profesor(self):
        datos_profesor: list = []
        try:
            with (open('fichero_delphos', encoding = 'utf-8',
                       mode = 'r') as f):
                for index, line in enumerate(f.readlines()):
                    if index > 0:
                        datos_profesor = line.strip('"\n').split(',')
                        profesor = Profesor(datos_profesor[0].strip(),
                                            datos_profesor[1].strip())

                        self._cargar_profesores_bbdd(profesor)
        except OSError: # todo desarrollar las excepciones
            print(f'No se pudo abrir el fichero.')
        except:
            print('error')

    def _cargar_profesores_bbdd(self, profesor: Profesor):
        conexion, cursor = self._abrir_conexion()
        aniadir_profesor = (f"INSERT INTO PROFESORES VALUES('{profesor.id}',"
                                f"'{profesor.nombre}','{profesor.apellidos}',"
                                f"'{profesor.clave_encriptada}')")
        cursor.execute(aniadir_profesor)
        # self._cerrar_conexion(cursor, conexion)

    def _cerrar_conexion(self, cursor, conexion):
        cursor.close()
        conexion.close()

# c = CargaInicial()
# c._vaciar_bbdd()
# c._generar_profesor()

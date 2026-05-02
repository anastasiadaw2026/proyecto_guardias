import mysql.connector
from mysql.connector import errorcode
from lib.profesor import Profesor


class CargaInicial:
    def __init__(self): # a lo mejor no necesito la conexión
        self._conexion, self._cursor = self._abrir_conexion()

    def _vaciar_bbdd(self):
        vaciar = ('TRUNCATE TABLE PROFESORES')
        self._cursor.execute(vaciar)

    def _abrir_conexion(self):
        # todo: ponerse el try
        conexion = mysql.connector.connect(user='root', password='',
                      host='127.0.0.1', database='gestion_guardias')
        conexion.autocommit = True
        cursor = conexion.cursor()
        return conexion, cursor

    def _generar_profesor(self):
        datos_profesor: list = []
        try:
            with (open('fichero_delphos', 'r', encoding = 'utf-8') as f):
                for index, line in enumerate(f.readlines()):
                    if index > 0:
                        datos_profesor = line.strip('"\n').split(',')
                        profesor = Profesor(datos_profesor[0].strip(),
                                            datos_profesor[1].strip())
                        self._cargar_profesores_bbdd(profesor)
        except OSError: # todo: desarrollar las excepciones
            print(f'No se pudo abrir el fichero.')
        except:
            print('error')

    def _cargar_profesores_bbdd(self, profesor: Profesor):
        aniadir_profesor = (f"INSERT INTO PROFESORES VALUES('{profesor.id}',"
                                f"'{profesor.nombre}','{profesor.apellidos}',"
                                f"'{profesor.clave_encriptada}')")
        self._cursor.execute(aniadir_profesor)

    def _cerrar_conexion(self):
        self._cursor.close()
        self._conexion.close()

c = CargaInicial()
c._vaciar_bbdd()
c._generar_profesor()
c._cerrar_conexion()

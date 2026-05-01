from lib.profesor import Profesor
import mysql.connector
from mysql.connector import errorcode

class App:
    def main(self):
        pass

    def _generar_profesor(self):
        # sacar nombre_app, introducir en la bbdd
        datos_profesor: list = []
        try:
            with (open('../bbdd/fichero_delphos', encoding = 'utf-8',
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
        try:
            conexion = mysql.connector.connect(user='root', password='',
                        host='127.0.0.1', database='gestion_guardias')
            conexion.autocommit = True
            cursor = conexion.cursor()
            aniadir_profesor = (f"INSERT INTO PROFESORES VALUES('{profesor.id}',"
                                f"'{profesor.nombre}','{profesor.apellidos}',"
                                f"'{profesor.clave_encriptada}')")
            cursor.execute(aniadir_profesor)
        # con los errores hay que trabajar mejor
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de conexión.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe dicha base de datos.")
            else:
                print(err)  # esto me saca el error como es
        if conexion.is_connected():
            cursor.close()
            conexion.close()


App()._generar_profesor()
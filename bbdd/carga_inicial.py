import mysql.connector
from mysql.connector import errorcode
from lib.profesor import Profesor

# Eres tonta? tienes las clases para algo, deberias transformar las clases o
# algo, a er l¡no tengo ni puta idea que hacer pero oye centra.


class CargaInicial:
    def __init__(self):
        self._conexion = mysql.connector.connect(user='root', password='',
                            host='127.0.0.1', database='gestion_guardias')
        self._cursor = self._conexion.cursor()
        self._conexion.autocommit = True

    def vaciar_bbdd(self):
        vaciar = ['SET FOREIGN_KEY_CHECKS = 0',
                  'TRUNCATE TABLE AULAS',
                  'TRUNCATE TABLE PROFESORES',
                  'TRUNCATE TABLE aulas',
                  'truncate table cursos',
                  'truncate table horas',
                  'SET FOREIGN_KEY_CHECKS = 1']
        for truncate in vaciar:
            self._cursor.execute(truncate)

    

    def _generar_profesor(self):
        datos_profesor: list = []
        try:
            with (open('fichero_delphos_profesores', 'r', encoding ='utf-8') as f):
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

    def cargar_horas(self):
        with open('horas', mode='r', encoding='utf-8') as f:
            for hora in f.readlines():
                aniadir_horas = (f'INSERT INTO HORAS VALUES("{hora.strip()}")')
                self._cursor.execute(aniadir_horas)

    def cargar_aulas(self):
        with open('aulas', mode='r', encoding='utf-8') as f:
            for aula in f.readlines():
                aniadir_aulas = (f'INSERT INTO aulas VALUES("'
                                 f'{aula.strip().upper()}")')
                self._cursor.execute(aniadir_aulas)

    def cargar_cursos(self):
        with open('cursos.csv', mode='r', encoding='utf-8') as f:
            for linea in f.readlines():
                curso, letras = linea.split(',')
                for letra in letras.split(';'):
                    aniadir_curso = (f'INSERT INTO cursos VALUES'
                                     f'("{curso + "-" + letra}")')
                    self._cursor.execute(aniadir_curso)

    def _cerrar_conexion(self):
        self._cursor.close()
        self._conexion.close()


# c = CargaInicial()
# c.vaciar_bbdd()
# c.cargar_horas()
# c.cargar_aulas()
# c.cargar_cursos()
# c._generar_profesor()
# # c.hacer_select()
# c._cerrar_conexion()

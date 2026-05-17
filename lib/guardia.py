from datetime import date

from claves.conexion_bbdd import CONEXION
from lib.aula import Aula
from lib.curso import Curso
from lib.hora import Hora
from lib.profesor import Profesor


class Guardia:
    NO_TAREA: str = "N"
    SI_TAREA: str = "S"

    def __init__(self):
        self.id: Profesor = Profesor(' ',' ')
        self.dia: date = ''
        self.hora: Hora = Hora()
        self.curso: Curso = Curso()
        self.clase: Aula = Aula()
        self.tarea: str = Guardia.NO_TAREA
        self.ficheros: str = ''

#todo: ver como cambiar el formato de fecha
    def __str__(self):
        return (f'Profesor: {self.id}\n'
                f'Día de la guardia: {self.dia}\n'
                f'Hora: {self.hora}\n'
                f'Curso: {self.curso}\n'
                f'Clase: {self.clase}\n'
                f'{"SIN TAREA" if self.tarea == Guardia.NO_TAREA
                    else "Hay tarea"}\n'
                f'{self.ficheros if self.ficheros else "No hay ficheros adjuntos"}')

    def insertar_guardia(self):
        cursor = CONEXION.cursor()
        insertion = (f'insert into guardias values('
                     f'"{self.id.id}", "{self.dia}", "{self.hora}",'
                     f'"{self.curso.nombre}", "{self.clase}", '
                     f'"{self.tarea}", "{self.ficheros}" '
                     f')')
        cursor.execute(insertion)
        cursor.close()

    def borrar_guardia(self):
        eliminacion_guardia = (f'DELETE FROM GUARDIAS where id = '
                               f'"{self.id.id}" '
                               f'and dia = "{self.dia}" and hora = '
                               f'"{self.hora}"')
        cursor = CONEXION.cursor()
        cursor.execute(eliminacion_guardia)
        filas_afectadas = cursor.rowcount
        cursor.close()
        return filas_afectadas
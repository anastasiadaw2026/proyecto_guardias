from lib.aula import Aula
from lib.curso import Curso
from lib.hora import Hora
from lib.profesor import Profesor


class Guardia:
    NO_TAREA: str = "N"
    SI_TAREA: str = "S"

    def __init__(self):
        self.id: Profesor = Profesor(' ',' ')
        self.dia: str = '' #todo
        self.hora: Hora = Hora()
        self.curso: Curso = Curso()
        self.clase: Aula = Aula()
        self.tarea: str = Guardia.NO_TAREA
        self.ficheros: str = '' #todo

#todo: ver como cambiar el formato de fecha
    def __str__(self):
        return (f'Profesor: {self.id}\n'
                f'Día de la guardia: {self.dia}\n'
                f'Hora: {self.hora}\n'
                f'Curso: {self.curso}\n'
                f'Clase: {self.clase}\n'
                f'{"SIN TAREA" if self.tarea == Guardia.NO_TAREA
                    else "Tarea: " + self.ficheros}\n')


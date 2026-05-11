import mysql.connector
from lib.guardia import Guardia
from lib.profesor import Profesor
import copy


class RecuperacionDatos:
    def __init__(self):
        self._conexion = mysql.connector.connect(user='root', password='',
                                                 host='127.0.0.1',
                                                 database='gestion_guardias')
        self._cursor = self._conexion.cursor()
        self._conexion.autocommit = True

    def seleccionar_guardias_semana(self, fecha_inicio, fecha_fin) -> list[Guardia]:
        guardias = []
        seleccion_guardias = (
            'select nombre, apellidos, dia, hora, curso, aula, tarea, ficheros '
            'from guardias natural join profesores '
            'where dia between %s and %s '
            'order by dia, hora'
        )
        self._cursor.execute(seleccion_guardias, (fecha_inicio, fecha_fin))

        for guardia in self._cursor:
            g = Guardia()
            g.id = Profesor(guardia[0], guardia[1])
            g.dia = guardia[2]
            g.hora = guardia[3]
            g.curso = guardia[4]
            g.clase = guardia[5]
            g.tarea = guardia[6]
            g.ficheros = guardia[7]
            guardias.append(copy.deepcopy(g))

        self._cursor.close()
        self._conexion.close()
        return guardias



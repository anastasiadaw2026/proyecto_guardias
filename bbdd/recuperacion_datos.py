import bcrypt
import mysql.connector

from claves.conexion_bbdd import CONEXION
from lib.aula import Aula
from lib.curso import Curso
from lib.guardia import Guardia
from lib.hora import Hora
from lib.profesor import Profesor
import copy


class RecuperacionDatos:
    def __init__(self):
        self._conexion = mysql.connector.connect(user='root', password='root',
                                                 host='127.0.0.1',
                                                 database='gestion_guardias')
        self._cursor = self._conexion.cursor()
        self._conexion.autocommit = True

    def sacar_prof_por_id(self, id_prof):
        selecioonar_profe = (f'select nombre, apellidos from profesores '
                             f'where id = "{id_prof}"')
        self._cursor.execute(selecioonar_profe)
        profesor = self._cursor.fetchone()
        self._cursor.close()
        return profesor

    def seleccionar_guardias_semana(self, fecha_inicio, fecha_fin) -> list[Guardia]:
        seleccion_guardias = (
            'select nombre, apellidos, dia, hora, curso, aula, tarea, ficheros '
            'from guardias natural join profesores '
            'where dia between %s and %s '
            'order by dia, hora')
        self._cursor.execute(seleccion_guardias, (fecha_inicio, fecha_fin))
        guardias = self.almacenar_guardias()
        self._cursor.close()
        return guardias

    def almacenar_guardias(self) -> list[Guardia]:
        guardias = []
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
        return guardias

    def sacar_las_guardias_existentes(self):
        seleccion_guardias = (
            'select nombre, apellidos, dia, hora, curso, aula, tarea, ficheros '
            'from guardias natural join profesores '
            'order by dia, hora')
        self._cursor.execute(seleccion_guardias)
        guardias = self.almacenar_guardias()
        self._cursor.close()
        return guardias

    def sacar_guardias_profesor(self, id_prof):
        seleccion_guardias = (
            f'select nombre, apellidos, dia, hora, curso, aula, tarea, '
            f'ficheros from guardias natural join profesores '
            f'where id = "{id_prof}" '
            f'order by dia, hora')
        self._cursor.execute(seleccion_guardias)
        guardias = self.almacenar_guardias()
        self._cursor.close()
        return guardias

    def sacar_profesores(self):
        profesores = []
        selecioonar_profe = ('select nombre, apellidos from profesores '
                             'order by nombre, apellidos')
        self._cursor.execute(selecioonar_profe)
        for profesor in self._cursor:
            profesores.append(Profesor(profesor[0], profesor[1]))
        self._cursor.close()
        return profesores

    def sacar_horas(self):
        horas = []
        seleccionar_horas = ('select nombre from horas '
                            'order by length(nombre)')
        self._cursor.execute(seleccionar_horas)
        for nombre in self._cursor:
            hora = Hora()
            hora.nombre = nombre[0]
            horas.append(hora)
        self._cursor.close()
        return horas

    def sacar_cursos(self):
        cursos = []
        seleccionar_cursos = ('select nombre from cursos '
                             'order by nombre')
        self._cursor.execute(seleccionar_cursos)
        for nombre in self._cursor:
            curso = Curso()
            curso.nombre = nombre[0].strip()
            cursos.append(curso)
        self._cursor.close()
        return cursos

    def sacar_aulas(self):
        aulas = []
        seleccionar_aulas = ('select nombre from aulas '
                             'order by nombre')
        self._cursor.execute(seleccionar_aulas)
        for nombre in self._cursor:
            aula = Aula()
            aula.nombre = nombre[0].strip()
            aulas.append(aula)
        self._cursor.close()
        return aulas

    def autentificar_profesor(self, id_introducido, clave_introducida):
        cursor = CONEXION.cursor()
        comprobacion = (f'select clave from profesores '
                        f'where id = "{id_introducido}"')
        cursor.execute(comprobacion)
        clave = cursor.fetchone()
        if clave:
            clave = clave[0]
            return bcrypt.checkpw(clave_introducida.encode('utf-8'), clave.encode('utf-8'))
        else:
            return False



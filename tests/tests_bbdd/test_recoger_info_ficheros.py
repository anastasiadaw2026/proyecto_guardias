import unittest

from lib.profesor import Profesor
from recursos_externos.bbdd.base_datos import BaseDatos

class TestRecogerInfoFicheros(unittest.TestCase):
    # todo: preguntar al profe pq no va
    def test_recoger_info_ficheros(self):
        resultado = BaseDatos.recoger_info_ficheros()

        self.assertTrue(isinstance(resultado, tuple))
        self.assertEqual(len(resultado), 4)

        cursos, aulas, horas, profesores = resultado

        self.assertTrue(len(cursos) > 0)
        self.assertTrue(len(aulas) > 0)
        self.assertTrue(len(horas) > 0)
        self.assertTrue(len(profesores) > 0)

        self.assertTrue(all(isinstance(curso, str) for curso in cursos))
        self.assertTrue(all(isinstance(aula, str) for aula in aulas))
        self.assertTrue(all(isinstance(hora, str) for hora in horas))
        self.assertTrue(all(isinstance(profesor, Profesor) for profesor in profesores))


if __name__ == "__main__":
    unittest.main()

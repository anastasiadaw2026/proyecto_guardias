import unittest
from claves.conexion_bbdd import CONEXION
from recursos_externos.base_datos import BaseDatos


class TestCargarTablas(unittest.TestCase):
    def test_cargar_tablas_exitoso(self):
        conexion = CONEXION
        conexion.autocommit = False

        resultado = BaseDatos.cargar_tablas()

        self.assertTrue(resultado)
        cursor = conexion.cursor()

        cursor.execute("SELECT COUNT(*) FROM cursos")
        self.assertTrue(cursor.fetchone()[0] > 0)

        cursor.execute("SELECT COUNT(*) FROM AULAS")
        self.assertTrue(cursor.fetchone()[0] > 0)

        cursor.execute("SELECT COUNT(*) FROM horas")
        self.assertTrue(cursor.fetchone()[0] > 0)

        cursor.execute("SELECT COUNT(*) FROM PROFESORES")
        self.assertTrue(cursor.fetchone()[0] > 0)

        conexion.rollback()
        conexion.autocommit = True

    def test_cargar_tablas_error(self):
        metodo_original = BaseDatos.recoger_info_ficheros

        try:
            def recoger_info_ficheros_error():
                return False
            BaseDatos.recoger_info_ficheros = recoger_info_ficheros_error
            resultado = BaseDatos.cargar_tablas()
            self.assertFalse(resultado)
        finally:
            BaseDatos.recoger_info_ficheros = metodo_original


if __name__ == "__main__":
    unittest.main()

import unittest
from recursos_externos.bbdd.base_datos import BaseDatos


class TestGuardarClavesProfesores(unittest.TestCase):
    #aquí igual no me abre el ficehro por akguan raozón extraña
    def test_guardar_claves_profesores_exitoso(self):
        resultado = BaseDatos.guardar_claves_profesores()

        self.assertEqual(resultado,
            "Las claves de acceso de los profesores se han guardado en "
            "un fichero externo en caso de que las quiera consultar."
        )

    def test_guardar_claves_profesores_error(self):
        metodo_original = BaseDatos.recoger_info_ficheros

        try:
            def recoger_info_ficheros_error():
                return False
            BaseDatos.recoger_info_ficheros = recoger_info_ficheros_error

            resultado = BaseDatos.guardar_claves_profesores()

            self.assertEqual(resultado,
                "El fichero para guardar las claves no se pudo abrir, "
                "por tanto, las claves de los profesores no se pueden ver.")

        finally:
            BaseDatos.recoger_info_ficheros = metodo_original


if __name__ == "__main__":
    unittest.main()

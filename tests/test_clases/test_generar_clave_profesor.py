import unittest

from lib.profesor import Profesor


class TestGenerarClave(unittest.TestCase):

    def test_generar_clave_correcta(self):
        profesor = Profesor("Juan", "Perez Gonzalez")
        clave_esperada = "juan17"
        self.assertEqual(clave_esperada, profesor._generar_clave())

    def test_generar_clave_with_spaces(self):
        profesor = Profesor(" Juan  ", "  Gonzalez   ")
        clave_esperada = "juan12"
        self.assertEqual(clave_esperada, profesor._generar_clave())

    def test_generar_clave_empty_nombre_apellidos(self):
        profesor = Profesor("", "")
        clave_esperada = "0"
        self.assertEqual(clave_esperada, profesor._generar_clave())

    def test_generar_clave_edge_case(self):
        profesor = Profesor("A", "B")
        clave_esperada = "a2"
        self.assertEqual(clave_esperada, profesor._generar_clave())


if __name__ == "__main__":
    unittest.main()

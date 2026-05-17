import unittest

from lib.profesor import Profesor


class TestGenerarId(unittest.TestCase):
    def test_generar_id_nombre_y_apellido_simples(self):
        profesor = Profesor("Juan", "Pérez")
        id_esperado = "jpérez"
        id_actual = profesor._generar_id()
        self.assertEqual(id_esperado, id_actual)

    def test_generar_id_nombres_y_apellidos_compuestos(self):
        profesor = Profesor("María Clara", "López Díaz")
        id_esperado = "mlópezdíaz"
        id_actual = profesor._generar_id()
        self.assertEqual(id_esperado, id_actual)

    def test_generar_id_nombre_simple_apellidos_compuestos_con_espacios(self):
        profesor = Profesor("David", "De La Cruz")
        id_esperado = "ddelacruz"
        id_actual = profesor._generar_id()
        self.assertEqual(id_esperado, id_actual)

    def test_generar_id_nombre_con_caracteres_especiales(self):
        profesor = Profesor("José", "García-Márquez")
        id_esperado = "jgarcía-márquez"
        id_actual = profesor._generar_id()
        self.assertEqual(id_esperado, id_actual)

    def test_generar_id_nombre_y_apellido_vacios(self):
        profesor = Profesor("", "")
        id_esperado = ""
        id_actual = profesor._generar_id()
        self.assertEqual(id_esperado, id_actual)

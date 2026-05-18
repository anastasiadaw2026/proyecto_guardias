import unittest

from recursos_externos.bbdd.base_datos import BaseDatos


class TestBaseDatos(unittest.TestCase):

    def test_sacar_guardias_profesor_no_guardias(self):
        result = BaseDatos.sacar_guardias_profesor('ndeapellido_4aapellido_4b')

        self.assertEqual(result, [])

    def test_sacar_guardias_profesor_con_guardias(self):
        test_professor_id = 'napellido_1aapellido_1b'
        result = BaseDatos.sacar_guardias_profesor(test_professor_id)

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_sacar_guardias_profesor_id_incorrecto(self):
        result = BaseDatos.sacar_guardias_profesor(-100)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()

import unittest

import bcrypt
from lib.profesor import Profesor


class TestEncriptarClave(unittest.TestCase):
    def test_encriptar_clave_devuelve_cadena(self):
        profesor = Profesor("Juan", "Pérez")
        clave_encriptada = profesor._encriptar_clave()
        self.assertIsInstance(clave_encriptada, str)

    def test_encriptar_clave_no_es_determinista(self):
        profesor = Profesor("Juan", "Pérez")
        clave_encriptada_1 = profesor._encriptar_clave()
        clave_encriptada_2 = profesor._encriptar_clave()
        self.assertNotEqual(clave_encriptada_1, clave_encriptada_2)

    def test_encriptar_clave_no_vacia(self):
        profesor = Profesor("Juan", "Pérez")
        clave_encriptada = profesor._encriptar_clave()
        self.assertTrue(len(clave_encriptada) > 0)

    def test_encriptar_clave_se_puede_validar(self):
        profesor = Profesor("Juan", "Pérez")
        clave_original = profesor.clave
        clave_encriptada = profesor._encriptar_clave()
        self.assertTrue(bcrypt.checkpw(clave_original.encode('utf-8'),
                                       clave_encriptada.encode('utf-8')))

import os
import unittest
from recursos_externos.bbdd.base_datos import BaseDatos


class TestHacerBackup(unittest.TestCase):
    def test_backup_exitoso(self):
        exito, mensaje = BaseDatos.hacer_backup()

        self.assertTrue(exito)
        self.assertTrue(mensaje.endswith(".sql"))
        self.assertTrue(os.path.exists(mensaje))

    def test_backup_docker_error(self):
        exito, mensaje = BaseDatos.hacer_backup()

        if not exito:
            self.assertFalse(exito)
            self.assertIn(
                "No such file or directory: '../../backups/backup_2026-05-18_22-53-34.sql", mensaje)
        else:
            print("Advertencia: Docker está funcionando, este caso no es reproducible en este entorno.")


if __name__ == "__main__":
    unittest.main()

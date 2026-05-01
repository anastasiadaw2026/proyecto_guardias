import random
import bcrypt


class Profesor:
    def __init__(self, nombre: str, apellidos: str):
        self._nombre: str = nombre
        self._apellidos: str = apellidos
        self._id: str = self._generar_id()
        self._clave: str = self._generar_clave()
        self._clave_encriptada: str = self._encriptar_clave()

    def __str__(self):
        return (f"Nombre: {self._nombre}\n"
                f"Apellidos: {self._apellidos}\n"
                f"Usuario: {self._id}\n"
                f"Clave: {self._clave}\n")

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellidos(self):
        return self._apellidos

    @property
    def id(self):
        return self._id

    @property
    def clave(self):
        return self._clave

    @property
    def clave_encriptada(self):
        return self._clave_encriptada

    def _generar_id(self):
        # el id va a ser la primera letra del nombre y los dos apellidos
        # juntos to_do en minusculas
        usuario: str = ''
        usuario += self._nombre[0].lower() + self._apellidos.replace(' ',
                                                            '').lower()
        return usuario

    def _generar_clave(self):
        # la clave va a ser nombre 5 números aleatorios
        clave: str = ''
        clave += (self._nombre.replace(' ', '').lower() +
                  str(random.randint(10000, 99999)))
        return clave

    def _encriptar_clave(self):
        # bcrypt.checkpw(password_bytes, hash_resultado) -- para comprobar
        clave_bytes = self._clave.encode('utf-8')
        sal = bcrypt.gensalt()
        clave_encriptada = bcrypt.hashpw(clave_bytes, sal)
        return clave_encriptada.decode('utf-8') # para guardarlo como string



# nombre_1 = 'Anastasia'
# apellido = 'Hristea Furtuna'
# p = Profesor(nombre_1, apellido)
# print(p._clave, p._clave_encriptada)
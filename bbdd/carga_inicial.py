import datetime
import subprocess
from claves.conexion_bbdd import CONEXION, CONTRASENIA
from lib.profesor import Profesor


class CargaInicial:
    def hacer_backup(self):
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archivo_backup = f"../backups/backup_{fecha_hora}.sql"
        with open(archivo_backup, "w", encoding = 'utf-8') as archivo:
            proceso = subprocess.run(
                [ "docker", "exec", "-e", f"MYSQL_PWD={CONTRASENIA}",
                    "mysql_daw1", "mysqldump", "-u", "root",
                    "--single-transaction", "--set-gtid-purged=OFF",
                    "gestion_guardias"], stdout=archivo)
        return proceso.returncode == 0, archivo_backup

    # todo: cuando acabare de hacer los test tengo que crear el truncate
    #  guardias también
    def vaciar_bbdd(self):
        cursor = CONEXION.cursor()
        vaciar = ['SET FOREIGN_KEY_CHECKS = 0',
                  'TRUNCATE TABLE AULAS',
                  'TRUNCATE TABLE PROFESORES',
                  'TRUNCATE TABLE aulas',
                  'truncate table cursos',
                  'truncate table horas',
                  'SET FOREIGN_KEY_CHECKS = 1']
        for truncate in vaciar:
            cursor.execute(truncate)

    def rellenar_tablas(self):
        self.cargar_aulas()
        self.cargar_cursos()
        self._generar_profesor()
        self.cargar_horas()

    def _generar_profesor(self):
        datos_profesor: list = []
        profesores = []
        try:
            with (open('..\\bbdd\\fichero_delphos_profesores', 'r', encoding
            = 'utf-8') as f):
                for index, line in enumerate(f.readlines()):
                    if index > 0:
                        datos_profesor = line.strip('').replace('\"',
                                        '').split(',')
                        profesor = Profesor(datos_profesor[0].strip(),
                                            datos_profesor[1].strip())
                        profesores.append(profesor)
                        self._cargar_profesores_bbdd(profesor)
            with open('../claves/claves_profesores.txt', 'w', encoding =
                    'utf-8') as fclaves:
                for profesor in profesores:
                    fclaves.write(profesor.id + ' - ' + profesor.clave + '\n')
        except OSError:
            print(f'No se pudo abrir el fichero.')
        except:
            print('error')

    def _cargar_profesores_bbdd(self, profesor: Profesor):
        cursor = CONEXION.cursor()
        aniadir_profesor = (f"INSERT INTO PROFESORES VALUES('{profesor.id}',"
                                f"'{profesor.nombre}','{profesor.apellidos}',"
                                f"'{profesor.clave_encriptada}')")
        cursor.execute(aniadir_profesor)
        cursor.close()

    def cargar_horas(self):
        cursor = CONEXION.cursor()
        with open('..\\bbdd\\horas', mode='r', encoding='utf-8') as f:
            for hora in f.readlines():
                aniadir_horas = (f'INSERT INTO HORAS VALUES("{hora.strip()}")')
                cursor.execute(aniadir_horas)


    def cargar_aulas(self):
        cursor = CONEXION.cursor()
        with open('..\\bbdd\\aulas', mode='r', encoding='utf-8') as f:
            for aula in f.readlines():
                aniadir_aulas = (f'INSERT INTO aulas VALUES("'
                                 f'{aula.strip().upper()}")')
                cursor.execute(aniadir_aulas)


    def cargar_cursos(self):
        cursor = CONEXION.cursor()
        with open('..\\bbdd\\cursos.csv', mode='r',
                  encoding='utf-8') as f:
            for linea in f.readlines():
                curso, letras = linea.strip().split(',')
                for letra in letras.strip().split(';'):
                    aniadir_curso = (f'INSERT INTO cursos VALUES'
                                     f'("{curso + "-" + letra}")')
                    cursor.execute(aniadir_curso)

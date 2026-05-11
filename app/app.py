from bbdd.carga_inicial import CargaInicial
from bbdd.recuperacion_datos import RecuperacionDatos
from lib.administrador import Administrador
from menus.menu_admin import MenuAdmin
from menus.menu_lector import MenuLector
from menus.menu_universal import MenuUniversal
from datetime import date, timedelta, datetime
from claves import claves_admin as ad


class App:
    def main(self):
        MenuUniversal.imprimir_menu_inicio()
        opcion_elegida = input(': ')
        match opcion_elegida.strip():
            case '1':
                print('Para registrarte y poder acceder a los derechos de '
                      'Administrador introduce el id y la clave.')
                id_admin = input('ID: ')
                clave_admin = input('CLAVE: ')
                if (Administrador(ad.ID, ad.CLAVE) ==
                        Administrador(id_admin, clave_admin)):
                    print('Autentificación correcta.')
                    self.gestionar_opciones_admin()
                else:
                    self.gestionar_fallo_autentificacion()
            case '2':
                pass
            case '3':
                self.gestionar_lector()
            case '4':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(self.main)

    def gestionar_opciones_admin(self):
        MenuAdmin().imprimir_menu_inicial_admin()
        opcion = input(': ')
        match opcion.strip().lower():
            case '1':
                pass
            case '2':
                self.visualizar_parte_guardias()
            case '3':
                pass
            case '4':
                pass
            case '5':
                CargaInicial().vaciar_bbdd()
            case '6':
                pass
            case '7':
                pass
            case '8':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(self.gestionar_opciones_admin())

    def gestionar_fallo_autentificacion(self):
        print('Usuario y/o contraseña incorrectos. Si quieres  intentar de '
              'nuevo introduce S, si quieres salir introduce N.')
        opcion = input(': ')
        match opcion.strip().lower():
            case 's':
                self.main()
            case 'n':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(self.gestionar_fallo_autentificacion)

    def gestionar_lector(self):
        MenuLector.imprimir_menu_lector_inicio()
        opcion_elegida = input(': ')
        match opcion_elegida.strip():
            case '1':
                self.visualizar_parte_guardias()
            case '2':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(self.gestionar_lector)

    def visualizar_parte_guardias(self):
        fecha_inicio = date.today()
        fecha_fin = date.today() + timedelta(days = 7)
        guardias = RecuperacionDatos().seleccionar_guardias_semana(
                                       fecha_inicio, fecha_fin)
        for guardia in guardias:
            print(guardia)
        self.cambiar_semana()

    def cambiar_semana(self):
        MenuLector().imprimir_elegir_semana()
        opcion = input(': ')
        match opcion.strip().lower():
            case 's':
                print('Introduce los datos del día a partir de las cual '
                      'quieres visualizar las guardias. Aparecerán lso datos de los siguientes 7 días a partir de la fecha introducida.')
                dia = int(input('Introduce el día: '))
                mes = int(input('Introduce el mes: '))
                anio = int(input('Introduce el año: \n'))
                fecha_inicio = date(anio, mes, dia)
                fecha_fin = date(anio, mes, dia) + timedelta(days = 7)
                guardias = RecuperacionDatos().seleccionar_guardias_semana(
                                                   fecha_inicio, fecha_fin)
                for guardia in guardias:
                    print(guardia)
            case 'n':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(self.cambiar_semana)

    def gestionar_entrada_incorrecta(self, funcion):
        MenuUniversal.imprimir_menu_error()
        opcion_elegida = input(': ')
        match opcion_elegida.strip():
            case '1':
                funcion()
            case '2':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(funcion)

    @staticmethod
    def salir():
        print('¡Adios!👋')


App().main()
from menus.menu_lector import MenuLector
from menus.menu_universal import MenuUniversal


class App:
    def main(self):
        MenuUniversal.imprimir_menu_inicio()
        opcion_elegida = input(': ')
        match opcion_elegida.strip():
            case '1':
                pass
            case '2':
                pass
            case '3':
                self.gestionar_lector()
            case '4':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(self.main)

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
        pass # necesito saber hacer selects

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
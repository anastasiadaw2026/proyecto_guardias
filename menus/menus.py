class Menus:
    class ConstantesMenu:
        UNO = '1'
        DOS = '2'
        TRES = '3'
        CUATRO = '4'
        CINCO = '5'
        SEIS = '6'
        SIETE = '7'
        SEGUIR = 'S'
        ACABAR = 'N'

    @staticmethod
    def imprimir_menu_inicio():
        print(f"¡Bienvenido a la página de gestión de las guardias!\n"
              f"Para empezar indicanos quién eres, introduciendo una de las "
              f"siguientes opciones:\n"
              f"{Menus.ConstantesMenu.UNO}. Administrador.\n"
              f"{Menus.ConstantesMenu.DOS}. Profesor.\n"
              f"{Menus.ConstantesMenu.TRES}. Lector (sin validar).\n"
              f"{Menus.ConstantesMenu.CUATRO}. Salir de la aplicación.")

    @staticmethod
    def imprimir_menu_visualizar_guardias():
        print(f"Elige una de las siguientes opciones:\n"
              f"{Menus.ConstantesMenu.UNO}. Visualizar el parte de guardias "
              f"semanas.\n"
              f"{Menus.ConstantesMenu.DOS}. Elegir otra semana.")

    @staticmethod
    def imprimir_menu_error():
        print(f'La opción introducida no corresponde a ninguna de las posibles.\n'
              f'Elige una de las siguientes opciones:\n'
              f'{Menus.ConstantesMenu.UNO}. Intentarlo de nuevo.\n'
              f'{Menus.ConstantesMenu.DOS}. Salir ')

    @staticmethod
    def imprimir_menu_inicial_prof():
        print(f"Elige una de las siguientes opciones:\n"
              f"{Menus.ConstantesMenu.UNO}. Visualizar el parte de guardias "
              f"semanas\n"
              f"{Menus.ConstantesMenu.DOS}. Dar de baja una guardia.\n"
              f"{Menus.ConstantesMenu.TRES}. Dar de alta una guardia.\n"
              f"{Menus.ConstantesMenu.CUATRO}. Salir.\n")

    @staticmethod
    def imprimir_menu_lector_inicio():
        print(f"Ahora puedes elegir una de las siguientes opciones:\n"
              f"{Menus.ConstantesMenu.UNO}. Visualizar el parte de guardias semanal.\n"
              f"{Menus.ConstantesMenu.DOS}. Salir.")

    @staticmethod
    def imprimir_elegir_semana():
        print(f'Estas son las guardias de esta semana.\n'
              f'Si deseas elegir otra semana pulsa '
              f'{Menus.ConstantesMenu.SEGUIR}, si no pulsa '
              f'{Menus.ConstantesMenu.ACABAR} y '
              f'saldrás de la aplicación.')

    @staticmethod
    def imprimir_menu_inicial_admin():
        print(f"Elige una de las siguientes opciones:\n"
              f"{Menus.ConstantesMenu.UNO}. Cargar la Base de Datos.\n"
              f"{Menus.ConstantesMenu.DOS}. Visualizar el parte de guardias "
              f"semanal.\n"
              f"{Menus.ConstantesMenu.TRES}. Dar de baja una guardia.\n"
              f"{Menus.ConstantesMenu.CUATRO}. Dar de alta una guardia.\n"
              f"{Menus.ConstantesMenu.CINCO}. Ver informe de las guardias.\n"
              f"{Menus.ConstantesMenu.SEIS}. Ver el listado de usuarios.\n"
              f"{Menus.ConstantesMenu.SIETE}. Salir.")


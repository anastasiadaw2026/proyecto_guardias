class MenuUniversal:

    @staticmethod
    def imprimir_menu_inicio():
        print(f"¡Bienvenido a la página de gestión de las guardias!\n"
              f"Para empezar indicanos quién eres, introduciendo una de las "
              f"siguientes opciones:\n"
              f"1. Administrador.\n"
              f"2. Profesor.\n"
              f"3. Lector (sin validar).\n"
              f"4. Salir de la aplicación.")

    @staticmethod
    def imprimir_menu_visualizar_guardias():
        print("Elige una de las siguientes opciones:\n"
              "1. Visualizar el parte de guardias semanas."
              "2. Elegir otra semana.")

    @staticmethod
    def imprimir_menu_error():
        print(f'La opción introducida no corresponde a ninguna de las posibles.\n'
              f'Elige una de las siguientes opciones:\n'
              f'1. Intentarlo de nuevo.\n'
              f'2. Salir ')


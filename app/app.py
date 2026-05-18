from colores import Colores
from recursos_externos.bbdd.base_datos import BaseDatos
from lib.administrador import Administrador
from lib.guardia import Guardia
from lib.profesor import Profesor
from menus.menus import Menus
from datetime import date, timedelta
from claves import claves_admin as ad


class App:
    FINES_SEMANA = (5, 6)
    NUM_DIAS_SEMANA = 7
    fin = False
    SEPARADOR = Colores.ROSA + '·' * 16 + Colores.RESET

    def main(self):
        while not App.fin:
            print(App.SEPARADOR)
            Menus.imprimir_menu_inicio()
            opcion_elegida = input(': ')
            print(App.SEPARADOR)
            match opcion_elegida.strip():
                case Menus.ConstantesMenu.UNO:
                    print(f'Para registrarte y poder acceder a los '
                          f'derechos de Administrador introduce el id y la clave.')
                    id_admin = input('ID: ').strip()
                    clave_admin = input('CLAVE: ').strip()
                    if (Administrador(ad.ID, ad.CLAVE) ==
                            Administrador(id_admin, clave_admin)):
                        print('Autentificación correcta.')
                        print(App.SEPARADOR)
                        self.gestionar_opciones_admin()
                    else:
                        self.gestionar_fallo_autentificacion()
                case Menus.ConstantesMenu.DOS:
                    print(App.SEPARADOR)
                    print('Para registrarte y poder acceder a los derechos de '
                          'Profesor introduce el id y la clave.')
                    id_prof = input('ID: ')
                    clave_prof = input('CLAVE: ')
                    if BaseDatos.autentificar_profesor(id_prof,
                                                               clave_prof):
                        print('Autentificación correcta.')
                        self.gestionar_opciones_profesor(id_prof)
                    else:
                        self.gestionar_fallo_autentificacion()
                case Menus.ConstantesMenu.TRES:
                    self.gestionar_lector()
                case Menus.ConstantesMenu.CUATRO:
                    self.salir()
                case _:
                    self.gestionar_entrada_incorrecta(self.main)

    def gestionar_opciones_profesor(self, id_prof):
        print(App.SEPARADOR)
        Menus.imprimir_menu_inicial_prof()
        opcion = input(': ')
        print(App.SEPARADOR)
        match opcion.lower().strip():
            case Menus.ConstantesMenu.UNO:
                self.visualizar_parte_guardias()
            case Menus.ConstantesMenu.DOS:
                self.dar_de_baja_guardia(id_prof)
                self.acabar_operacion()
            case Menus.ConstantesMenu.TRES:
                self.dar_de_alta_guardia(id_prof)
            case Menus.ConstantesMenu.CUATRO:
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(
                    self.gestionar_opciones_profesor, id_prof)

    def gestionar_opciones_admin(self):
        print(App.SEPARADOR)
        Menus.imprimir_menu_inicial_admin()
        opcion = input(': ')
        print(App.SEPARADOR)
        match opcion.strip().lower():
            case Menus.ConstantesMenu.UNO:
                self.gestionar_backup()
                BaseDatos.vaciar_bbdd()
                BaseDatos.cargar_tablas()
                BaseDatos.guardar_claves_profesores()
                self.acabar_operacion()
            case Menus.ConstantesMenu.DOS:
                self.visualizar_parte_guardias()
            case Menus.ConstantesMenu.TRES:
                self.dar_de_baja_guardia()
                self.acabar_operacion()
            case Menus.ConstantesMenu.CUATRO:
                self.dar_de_alta_guardia()
                self.acabar_operacion()
            case Menus.ConstantesMenu.CINCO:
                self.generar_informe()
            case Menus.ConstantesMenu.SEIS:
                contador = 1
                profesores = BaseDatos.sacar_profesores()
                print(f'Profesores registrados en el sistema:\n'
                      f'{Colores.ROJO}{"ID".ljust(40)}NOMBRE/APELLIDO'
                      f'S{Colores.RESET}')
                for profesor in profesores:
                    print(contador, end='. ')
                    profesor.imprimir_id_nombre_apellidos()
                    contador += 1
                self.acabar_operacion()
            case Menus.ConstantesMenu.SIETE:
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(
                    self.gestionar_opciones_admin)

    def generar_informe(self):
        print('Para ver el informe de la guardias debes introducir '
              'la fecha de inicio y la fecha final.\n'
              'Para la FECHA DE INICIO:')
        fecha_inicio = self.generar_fecha()
        print('Para la FECHA FINAL:')
        fecha_final = self.generar_fecha()
        if fecha_inicio < fecha_final:
            guardias = BaseDatos.seleccionar_guardias_por_fechas(
                fecha_inicio, fecha_final)
            for guardia in guardias:
                print(guardia)
        else:
            print(f'La fecha final es menor que la fecha de inicio, '
                  f'si desea intercambiarlas automáticamente pulse '
                  f'{Menus.ConstantesMenu.SEGUIR}.'
                  f'Si quiere introducir las fechas de nuevo pulse '
                  f'{Menus.ConstantesMenu.ACABAR} y para  salir pulse '
                  f'cualquier otra tecla.')
            opcion = input(': ')
            if opcion.upper().strip() == Menus.ConstantesMenu.SEGUIR:
                guardias = BaseDatos.seleccionar_guardias_por_fechas(
                    fecha_final, fecha_inicio)
                for guardia in guardias:
                    print(guardia)
            elif opcion.upper().strip() == Menus.ConstantesMenu.ACABAR:
                self.generar_informe()
            else:
                self.salir()

    def gestionar_backup(self):
        print(App.SEPARADOR)
        print(f'Antes de cargar una nueva base de datos, desea hacer '
              f'la copia de seguridad de la base de datos en su '
              f'estado actual. Si quiere generar el backup pulse '
              f'{Menus.ConstantesMenu.SEGUIR}, si no pulse '
              f'{Menus.ConstantesMenu.ACABAR}')
        opcion = input(': ')
        print(App.SEPARADOR)
        match opcion.upper().strip():
            case Menus.ConstantesMenu.SEGUIR:
                resultados = BaseDatos.hacer_backup()
                self.comprobar_resultado_backup(resultados)
            case Menus.ConstantesMenu.ACABAR:
                print(f'Si esta seguro introduzca {Menus.ConstantesMenu.SEGUIR}. '
                      f'Si introduce otro carácter volverá al inicio.')
                opcion = input(': ')
                if opcion.upper().strip() != Menus.ConstantesMenu.SEGUIR:
                    self.gestionar_backup()
            case _:
                self.gestionar_entrada_incorrecta(self.gestionar_backup)

    def comprobar_resultado_backup(self, resultados: tuple[bool, str]):
        print(App.SEPARADOR)
        if resultados[0]:
            print(f'La copia de seguridad se guardo correctamente, '
                  f'Si desea consultarla se encuentra en el archivo '
                  f'{resultados[1]}.')
        else:
            print(resultados[1])
            print(f'Si quiere seguir sin copia de seguridad introduzca '
                  f'{Menus.ConstantesMenu.SEGUIR}. Si quiere salir '
                  f'introduzca {Menus.ConstantesMenu.ACABAR}.')
            opcion = input(': ')
            if opcion.upper().strip() == Menus.ConstantesMenu.ACABAR:
                App.salir()
            elif opcion.upper().strip() == Menus.ConstantesMenu.SEGUIR:
                return
            else:
                self.gestionar_entrada_incorrecta(
                    self.comprobar_resultado_backup, resultados)

    def dar_de_alta_guardia(self, *args):
        guardia = Guardia()
        if args:
            profesor = BaseDatos.sacar_prof_por_id(*args)
            guardia.id = Profesor(profesor[0], profesor[1])
        else:
            print(App.SEPARADOR)
            print('Elige el profesor al quien se le designará la guardia. '
                  'Introduce el número correspondiente.')
            profesor = self.elegir_objeto_de_lista(
                BaseDatos.sacar_profesores())
            guardia.id = profesor
        print(App.SEPARADOR)
        print('Ahora elige la fecha de la guardia.')
        fecha = self.generar_fecha()
        guardia.dia = fecha
        print(App.SEPARADOR)
        print('Ahora elige la hora en la que se realizará la guardía.')
        hora = self.elegir_objeto_de_lista(BaseDatos.sacar_horas())
        guardia.hora = hora
        print(App.SEPARADOR)
        print('A continuación elige el curso.')
        curso = self.elegir_objeto_de_lista(BaseDatos.sacar_cursos())
        guardia.curso = curso
        print(App.SEPARADOR)
        print('Además, elige el aula.')
        aula = self.elegir_objeto_de_lista(BaseDatos.sacar_aulas())
        guardia.clase = aula
        print(App.SEPARADOR)
        print(f'Si hay tarea introduce {Menus.ConstantesMenu.SEGUIR}, '
              f'si no introduce cualquier otra letra o dígito.')
        opcion = input(': ')
        if opcion.strip().upper() == Menus.ConstantesMenu.SEGUIR:
            guardia.tarea = Guardia.SI_TAREA
        print(App.SEPARADOR)
        print('Por último si quieres añadir algún fichero introduce su '
              'nombre, si no no introduzcas nada y pulsa ENTER.')
        opcion = input(': ')
        if opcion:
            guardia.ficheros = opcion
        print(App.SEPARADOR)
        print(guardia)
        print(App.SEPARADOR)
        guardia.insertar_guardia()

    def dar_de_baja_guardia(self, *args):
        print(App.SEPARADOR)
        print("Introduce el número de la guardia que quieres dar de baja:")
        if not args:
            guardia = self.elegir_objeto_de_lista(BaseDatos.sacar_las_guardias_existentes())
        else:
            guardia = self.elegir_objeto_de_lista(
                BaseDatos.sacar_guardias_profesor(args))
        guardia.borrar_guardia()

    def elegir_objeto_de_lista(self, lista):
        print(App.SEPARADOR) #todo: ver que hacer si no hay guardias
        if lista:
            for numero, objeto in enumerate(lista):
                print(str(numero + 1) + f'. {'-' * 10}\n' + str(objeto))
        else:
            print('No hay opciones disponibles.')
            print(f'Si desea salir de la aplicación pulse '
                  f'{Menus.ConstantesMenu.ACABAR}. Si quiere volver al menu '
                  f'principal pulse {Menus.ConstantesMenu.SEGUIR}.')
            opcion = input(': ')
            if opcion.upper().strip() == Menus.ConstantesMenu.ACABAR:
                return self.salir()
            elif opcion.upper().strip() == Menus.ConstantesMenu.SEGUIR:
                return self.main()
        try:
            opcion = int(input(': '))
            if 1 <= opcion <= len(lista):
                guardia_elegida = lista[opcion - 1]
                return guardia_elegida
            else:
                self.gestionar_entrada_incorrecta(
                    self.elegir_objeto_de_lista, lista)
        except ValueError:
            self.gestionar_entrada_incorrecta(self.elegir_objeto_de_lista,
                                              lista)

    def gestionar_fallo_autentificacion(self):
        print(App.SEPARADOR)
        print(f'Usuario y/o contraseña incorrectos. Si quieres intentar de '
              f'nuevo introduce {Menus.ConstantesMenu.SEGUIR}, si quieres salir '
              f'introduce {Menus.ConstantesMenu.ACABAR}.')
        opcion = input(': ')
        print(App.SEPARADOR)
        match opcion.strip().upper():
            case Menus.ConstantesMenu.SEGUIR:
                return
            case Menus.ConstantesMenu.ACABAR:
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(self.gestionar_fallo_autentificacion)

    def gestionar_lector(self):
        print(App.SEPARADOR)
        Menus.imprimir_menu_lector_inicio()
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
        guardias = BaseDatos.seleccionar_guardias_por_fechas(
                                       fecha_inicio, fecha_fin)
        print(App.SEPARADOR)
        self.imprimir_guardias(guardias)
        self.cambiar_semana()
        self.acabar_operacion()

    def imprimir_guardias(self, guardias: list[Guardia]):
        if guardias:
            for guardia in guardias:
                print(App.SEPARADOR)
                print(guardia)
        else:
            print('No se encontró ninguna guardía para estas fechas.')

    def cambiar_semana(self):
        print(App.SEPARADOR)
        Menus.imprimir_elegir_semana()
        opcion = input(': ')
        print(App.SEPARADOR)
        match opcion.strip().upper():
            case Menus.ConstantesMenu.SEGUIR:
                print(App.SEPARADOR)
                print(f'Introduce los datos del día a partir de las cual '
                      f'quieres visualizar las guardias. Aparecerán los datos '
                      f'de los siguientes {App.NUM_DIAS_SEMANA} días a '
                      f'partir de la fecha introducida.')
                fecha_inicio = self.generar_fecha()
                fecha_fin = fecha_inicio + timedelta(days = App.NUM_DIAS_SEMANA)
                guardias = BaseDatos.seleccionar_guardias_por_fechas(
                                                   fecha_inicio, fecha_fin)
                print(App.SEPARADOR) #todo
                self.imprimir_guardias(guardias)
            case Menus.ConstantesMenu.ACABAR:
                self.salir()
            case _:
               self.gestionar_entrada_incorrecta(self.cambiar_semana)

    def generar_fecha(self) -> date:
        try:
            dia = int(input('Introduce el día: '))
            mes = int(input('Introduce el mes: '))
            anio = int(input('Introduce el año: '))
            fecha = date(anio, mes, dia)
            if date.weekday(fecha) not in App.FINES_SEMANA:
                return fecha
            else:
                print(App.SEPARADOR)
                print(f'La fecha introducida se corresponde a un día no '
                      f'lectivo. Si desea salir pulsa '
                      f'{Menus.ConstantesMenu.ACABAR}, si quiere '
                      f'intentar poner otra fecha pulse cualquier otra tecla.')
                opcion = input(': ')
                print(App.SEPARADOR)
                if opcion.upper().strip() == Menus.ConstantesMenu.ACABAR:
                    self.salir()
                else:
                    return self.generar_fecha()
        except ValueError:
            return self.gestionar_entrada_incorrecta(self.generar_fecha)

    def gestionar_entrada_incorrecta(self, funcion, *args):
        print(App.SEPARADOR)
        Menus.imprimir_menu_error()
        opcion_elegida = input(': ')
        print(App.SEPARADOR)
        match opcion_elegida.strip():
            case Menus.ConstantesMenu.UNO:
                return funcion(*args)
            case Menus.ConstantesMenu.DOS:
                return self.salir()
            case _:
                return self.gestionar_entrada_incorrecta(funcion, *args)

    def acabar_operacion(self):
        print(App.SEPARADOR)
        print(f'Operación ejecutada correctamente.\n'
              f'Si deseas salir de la app, introduce '
              f'{Menus.ConstantesMenu.ACABAR}. Si deseas '
              f'ejecutar otras operaciones introduce {Menus.ConstantesMenu.SEGUIR}.')
        opcion = input(': ')
        print(App.SEPARADOR)
        match opcion.upper().strip():
            case Menus.ConstantesMenu.ACABAR:
                self.salir()
            case Menus.ConstantesMenu.SEGUIR:
                return
            case _:
                self.gestionar_entrada_incorrecta(self.acabar_operacion)

    @staticmethod
    def salir():
        print(App.SEPARADOR)
        print('¡Adios!👋')
        print(App.SEPARADOR)
        App.fin = True
        raise SystemExit


App().main()
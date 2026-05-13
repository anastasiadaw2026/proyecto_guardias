from bbdd.carga_inicial import CargaInicial
from bbdd.recuperacion_datos import RecuperacionDatos
from lib.administrador import Administrador
from lib.guardia import Guardia
from lib.profesor import Profesor
from menus.menu_admin import MenuAdmin
from menus.menu_lector import MenuLector
from menus.menu_prof import MenuProf
from menus.menu_universal import MenuUniversal
from datetime import date, timedelta
from claves import claves_admin as ad


class App:
    FIN = False
    def main(self):
        while not App.FIN:
            MenuUniversal.imprimir_menu_inicio()
            opcion_elegida = input(': ')
            match opcion_elegida.strip():
                case '1':
                    print('Para registrarte y poder acceder a los derechos de '
                          'Administrador introduce el id y la clave.')
                    id_admin = input('ID: ').strip()
                    clave_admin = input('CLAVE: ').strip()
                    if (Administrador(ad.ID, ad.CLAVE) ==
                            Administrador(id_admin, clave_admin)):
                        print('Autentificación correcta.')
                        self.gestionar_opciones_admin()
                    else:
                        self.gestionar_fallo_autentificacion()
                case '2':
                    print('Para registrarte y poder acceder a los derechos de '
                          'Profesor introduce el id y la clave.')
                    id_prof = input('ID: ')
                    clave_prof = input('CLAVE: ')
                    if RecuperacionDatos().autentificar_profesor(id_prof,
                                                               clave_prof):
                        print('Autentificación correcta.')
                        self.gestionar_opciones_profesor(id_prof)
                    else:
                        self.gestionar_fallo_autentificacion()
                case '3':
                    self.gestionar_lector()
                case '4':
                    self.salir()
                case _:
                    self.gestionar_entrada_incorrecta(self.main)

    def gestionar_opciones_profesor(self, id_prof):
        MenuProf().imprimir_menu_inicial_prof()
        opcion = input(': ')
        match opcion.lower().strip():
            case '1':
                self.visualizar_parte_guardias()
            case '2':
                self.dar_de_baja_guardia(id_prof)
                self.acabar_operacion()
            case '3':
                self.dar_de_alta_guardia(id_prof)
            case '4':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(
                    self.gestionar_opciones_profesor, id_prof)

    def gestionar_opciones_admin(self):
        MenuAdmin().imprimir_menu_inicial_admin()
        opcion = input(': ')
        match opcion.strip().lower():
            case '1':
                self.gestionar_backup()
                CargaInicial().vaciar_bbdd()
                CargaInicial().rellenar_tablas()
                self.acabar_operacion()
            case '2':
                self.visualizar_parte_guardias()
            case '3':
                self.dar_de_baja_guardia()
                self.acabar_operacion()
            case '4':
                self.dar_de_alta_guardia()
                self.acabar_operacion()
            case '5':
                self.generar_informe()
            case '6':
                contador = 1
                profesores = RecuperacionDatos().sacar_profesores()
                print('Profesores registrados en el sistema:\n'
                      'ID                   NOMBRE/APELLIDOS ') #todo
                for profesor in profesores:
                    print(contador, end='. ')
                    profesor.imprimir_id_nombre_apellidos()
                    contador += 1
                self.acabar_operacion()
            case '7':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(
                    self.gestionar_opciones_admin)

    def generar_informe(self):
        print('Para ver el informe de la guardias debes introducir '
              'la fecha de inicio y la fecha final.\n'
              'Para la FECHA DE INICIO:')
        fecha_inicio = self.generar_fecha()
        print('Para la FECHA FINAL:\n')
        fecha_final = self.generar_fecha()
        if fecha_inicio < fecha_final:
            guardias = RecuperacionDatos().seleccionar_guardias_semana(
                fecha_inicio, fecha_final)
            for guardia in guardias:
                print(guardia)
        else:
            print('La fecha final es menor que la fecha de inicio, '
                  'si desea intercambiarlas automáticamente pulse S.'
                  'Si quiere introducir las fechas de nuevo pulse N y para '
                  'salir pulse cualquier otra tecla.')
            opcion = input(': ')
            if opcion.lower().strip() == 's':
                guardias = RecuperacionDatos().seleccionar_guardias_semana(
                    fecha_final, fecha_inicio)
                for guardia in guardias:
                    print(guardia)
            elif opcion.lower().strip() == 'n':
                self.generar_informe()
            else:
                self.salir()

    def gestionar_backup(self):
        print('Antes de cargar una nueva base de datos, desea hacer '
              'la copia de seguridad de la base de datos en su '
              'estado actual. Si quiere generar el backup pulse S, '
              'si no pulse N.')
        opcion = input(': ')
        match opcion.lower().strip():
            case 's':
                CargaInicial().hacer_backup()
            case 'n':
                print('Si esta seguro introduzca S. Si introduce otro '
                      'carácter volverá al inicio.')
                opcion = input(': ')
                if opcion.lower().strip() != 's':
                    self.gestionar_backup()
            case _:
                self.gestionar_entrada_incorrecta(self.gestionar_backup)

    def dar_de_alta_guardia(self, *args):
        guardia = Guardia()
        if len(*args) == 0:
            print('Elige el profesor al quien se le designará la guardia. '
                  'Introduce el número correspondiente.')
            profesor = self.elegir_objeto_de_lista(RecuperacionDatos().sacar_profesores())
            guardia.id = profesor
        else:
            profesor = RecuperacionDatos().sacar_prof_por_id(usuario)
            guardia.id = Profesor(profesor[0], profesor[1])
        print('Ahora elige la fecha de la guardia.')
        fecha = self.generar_fecha()
        guardia.dia = fecha
        print('Ahora elige la hora en la que se realizará la guardía.')
        hora = self.elegir_objeto_de_lista(RecuperacionDatos().sacar_horas())
        guardia.hora = hora
        print('A continuación elige el curso.')
        curso = self.elegir_objeto_de_lista(RecuperacionDatos().sacar_cursos())
        guardia.curso = curso
        print('Además, elige el aula.')
        aula = self.elegir_objeto_de_lista(RecuperacionDatos().sacar_aulas())
        guardia.clase = aula
        print('Si hay tarea introduce S, si no introduce cualquier otra '
              'letra o dígito.')
        opcion = input(': ')
        if opcion.lower().strip() == 's':
            guardia.tarea = Guardia.SI_TAREA
        print('Por último si quieres añadir algún fichero introduce su '
              'nombre, si no no introduzcas nada y pulsa ENTER.')
        opcion = input(': ')
        if opcion:
            guardia.ficheros = opcion
        print(guardia)
        guardia.insertar_guardia()

    def dar_de_baja_guardia(self, *args):
        print("Introduce el número de la guardia que quieres dar de baja:")
        if len(*args) == 0:
            guardia = self.elegir_objeto_de_lista(RecuperacionDatos().sacar_las_guardias_existentes())
        else:
            guardia = self.elegir_objeto_de_lista(
                RecuperacionDatos().sacar_guardias_profesor(*args))
        guardia.borrar_guardia()

    def elegir_objeto_de_lista(self, lista): #todo: hacer la salida bonita
        for numero, objeto in enumerate(lista):
            print(str(numero + 1) + '. ----\n' + str(objeto))
        try:
            opcion = int(input(': '))
            if 1 <= opcion <= len(lista):
                guardia_elegida = lista[opcion - 1]
                return guardia_elegida
            else:
                # en este caso como tiene parámetros se pone chungo pq no
                # puedo solamente usar mi méto_do comodín
                self.gestionar_entrada_incorrecta(
                    self.elegir_objeto_de_lista, lista)
        except ValueError:
            self.gestionar_entrada_incorrecta(self.elegir_objeto_de_lista,
                                              lista)

    def gestionar_fallo_autentificacion(self):
        print('Usuario y/o contraseña incorrectos. Si quieres  intentar de '
              'nuevo introduce S, si quieres salir introduce N.')
        opcion = input(': ')
        match opcion.strip().lower():
            case 's':
                return
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
                      'quieres visualizar las guardias. Aparecerán lso datos '
                      'de los siguientes 7 días a partir de la fecha introducida.')
                fecha_inicio = self.generar_fecha()
                fecha_fin = fecha_inicio + timedelta(days = 7)
                guardias = RecuperacionDatos().seleccionar_guardias_semana(
                                                   fecha_inicio, fecha_fin)
                for guardia in guardias:
                    print(guardia)
            case 'n':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(self.cambiar_semana)

    def generar_fecha(self) -> date:
        try:
            dia = int(input('Introduce el día: '))
            mes = int(input('Introduce el mes: '))
            anio = int(input('Introduce el año: '))
            fecha = date(anio, mes, dia)
            return fecha
        except ValueError:
            self.gestionar_entrada_incorrecta(self.generar_fecha)

    def gestionar_entrada_incorrecta(self, funcion, *args):
        MenuUniversal.imprimir_menu_error()
        opcion_elegida = input(': ')
        match opcion_elegida.strip():
            case '1':
                funcion(*args)
            case '2':
                self.salir()
            case _:
                self.gestionar_entrada_incorrecta(funcion, *args)

    def acabar_operacion(self):
        print('Operación ejecutada correctamente.\n'
              'Si deseas salir de la app, introduce N. Si deseas ejecutar '
              'otras operaciones introduce S.')
        opcion = input(': ')
        match opcion.lower().strip():
            case 'n':
                self.salir()
            case 's':
                return
            case _:
                self.gestionar_entrada_incorrecta(self.acabar_operacion)

    @staticmethod
    def salir():
        print('¡Adios!👋')
        App.FIN = True
        raise SystemExit


App().main()
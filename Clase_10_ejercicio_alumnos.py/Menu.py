import Funciones

titulo = " Menú alumnos Sysacad "
subrayado = len(titulo) * "-"
mensaje_opciones = """
01 - Ingresar alumnos\n
02 - Mostrar todos los alumnos\n
03 - Mostrar alumnos promocionados\n
04 - Mostrar alumnos regularizados\n
05 - Mostrar alumnos desaprobados\n
06 - Buscar alumno por DNI\n
07 - Mostrar totales de cada estado de aprobación\n
08 - Mostrar promedio de nota de todos los alumnos\n
09 - Mostrar promedio de nota de los alumnos masculinos\n
10 - Mostrar el procentaje de alumnos de cada género\n
11 - Mostrar el / los alumnos con mayor nota\n
12 - Mostrar la cantidad de alumnos que superan la nota promedio\n
13 - Salir\n"""
flag_carga = False

while(True):
    print(f"\n{subrayado}")
    print(titulo)
    print(subrayado)
    print(mensaje_opciones)

    opcion = Funciones.pedir_opcion(1, 13)

    match opcion:
        case 1:
            matriz_alumnos = Funciones.cargar_matriz()
            flag_carga = True
        case 2:
            if flag_carga:
                print(subrayado)
                print("Lista completa de alumnos:")
                Funciones.mostrar_matriz(matriz_alumnos)
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 3:
            if flag_carga:
                print(subrayado)
                print("Lista de alumnos promocionados:")
                promocionados = Funciones.buscar_promocionados(matriz_alumnos, 4)
                if promocionados == -1:
                    print("No hay alumnos promocionados")
                else:
                    Funciones.mostrar_matriz(promocionados)
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 4:
            if flag_carga:
                print(subrayado)
                print("Lista de alumnos regularizados:")
                regularizados = Funciones.buscar_regularizados(matriz_alumnos, 4)
                if regularizados == -1:
                    print("No hay alumnos regularizados")
                else:
                    Funciones.mostrar_matriz(regularizados)
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 5:
            if flag_carga:
                print(subrayado)
                print("Lista de alumnos desaprobados:")
                desaprobados = Funciones.buscar_desaprobados(matriz_alumnos, 4)
                if desaprobados == -1:
                    print("No hay alumnos desaprobados")
                else:
                    Funciones.mostrar_matriz(desaprobados)
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 6:
            if flag_carga:
                Funciones.buscar_por_DNI(matriz_alumnos, 2)
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 7:
            if flag_carga:
                print(subrayado)
                print("Totales de cada estado de aprobación:")
                Funciones.imprimir_cantidades(matriz_alumnos, 4)

            else:
                print("Primero debe realizar la carga de los alumnos")
        case 8:
            if flag_carga:
                print(subrayado)
                print(f"El promedio final de todos los alumnos es: {Funciones.calcular_promedio(matriz_alumnos, 4)}")
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 9:
            if flag_carga:
                print(subrayado)
                print(f"El promedio final de todos los alumnos masculinos es: {Funciones.calcular_promedio_masculinos(matriz_alumnos, 4, 3)}")
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 10:
            if flag_carga:
                print(subrayado)
                Funciones.imprimir_porcentaje_generos(matriz_alumnos, 3)
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 11:
            if flag_carga:
                print(subrayado)
                print("Alumnos con la nota más alta:")
                Funciones.imprimir_alumnos_mayor_nota(matriz_alumnos, 4)
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 12:
            if flag_carga:
                print(subrayado)
                print(f"Cantidad de alumnos con nota mayor al promedio: {Funciones.calcular_alumnos_superan_promedio(matriz_alumnos, 4)}")
            else:
                print("Primero debe realizar la carga de los alumnos")
        case 13:
            print("Saliendo...")
            break
    
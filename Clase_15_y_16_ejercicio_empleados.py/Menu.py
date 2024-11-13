import Funciones

titulo = " Menú  de empleados "
subrayado = len(titulo) * "-"
mensaje_opciones = """
01 - Leer información (csv)\n
02 - Leer información (json)\n
03 - Cargar empleados\n
04 - Mostrar empleados\n
05 - Ordenar empleados por sueldo\n
06 - Mostrar empleados de mayor edad\n
07 - Mostrar empleados de mayot antigüedad\n
08 - Mostrar apellidos\n
09 - Mostrar empleados con salario en USD\n
10 - Buscar empleado\n
11 - Eliminar empleado\n
12 - Guardar información (csv)\n
13 - Guardar información (json)\n
14 - Salir\n"""

flag_carga_diccionario = False
flag_carga_csv = False
flag_carga_json = False

lista_empleados = []

while(True):
    print(f"\n{subrayado}")
    print(titulo)
    print(subrayado)
    print(mensaje_opciones)

    opcion = Funciones.pedir_opcion(1, 14)

    match opcion:
        case 1:
            if flag_carga_csv:
                pass
            else:
                print("\nPrimero debe realizar la carga del archivo csv")
        case 2:
            if flag_carga_json:
                pass
            else:
                print("\nPrimero debe realizar la carga del archivo json")
        case 3:
            if Funciones.cargar_empleados(lista_empleados):
                print("\nEmpleado cargado con éxito")
                flag_carga_diccionario = True
            else:
                print("\nOperación cancelada")
        case 4:
            if flag_carga_diccionario:
                print("\n-----------------------------------")
                print("Lista de empleados\n")
                Funciones.mostrar_lista_diccionario(lista_empleados)
                print("-----------------------------------")
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 5:
            if flag_carga_diccionario:
                lista_ordenada = Funciones.ordenar_por_sueldo(lista_empleados)
                print("\n-----------------------------------")
                print("Lista de empleados ordenados por sueldo\n")
                Funciones.mostrar_lista_diccionario(lista_ordenada)
                print("-----------------------------------")
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 6:
            if flag_carga_diccionario:
                lista_ordenada = Funciones.ordenar_por_edad(lista_empleados)
                print("\n-----------------------------------")
                print("Lista de los 5 empleados de mayor edad\n")
                Funciones.mostrar_lista_diccionario_hasta_5(lista_ordenada)
                print("-----------------------------------")
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 7:
            if flag_carga_diccionario:
                lista_ordenada = Funciones.ordenar_por_antiguedad(lista_empleados)
                print("\n-----------------------------------")
                print("Lista de los 5 empleados de mayor antigüedad\n")
                Funciones.mostrar_lista_diccionario_hasta_5(lista_ordenada)
                print("-----------------------------------")
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 8:
            if flag_carga_diccionario:
                lista_ordenada = Funciones.ordenar_apellidos_unicos(lista_empleados)
                print("\n-----------------------------------")
                print("Lista de apellidos\n")
                Funciones.imprimir_lista(lista_ordenada)
                print("-----------------------------------")
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 9:
            if flag_carga_diccionario:
                pass
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 10:
            if flag_carga_diccionario:
                pass
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 11:
            if flag_carga_diccionario:
                pass
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 12:
            if flag_carga_diccionario:
                pass
                flag_carga_csv = True
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 13:
            if flag_carga_diccionario:
                pass
                flag_carga_json = True
            else:
                print("\nPrimero debe realizar la carga de los empleados")
        case 14:
            print("\nSaliendo...")
            break
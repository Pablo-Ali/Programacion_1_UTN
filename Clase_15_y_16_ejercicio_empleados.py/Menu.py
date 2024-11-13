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
                print("Primero debe realizar la carga del archivo csv")
        case 2:
            if flag_carga_json:
                pass
            else:
                print("Primero debe realizar la carga del archivo json")
        case 3:
            flag_carga_diccionario = True
        case 4:
            if flag_carga_diccionario:
                pass
            else:
                print("Primero debe realizar la carga de los empleados")
        case 5:
            if flag_carga_diccionario:
                pass
            else:
                print("Primero debe realizar la carga de los empleados")
        case 6:
            if flag_carga_diccionario:
                pass
            else:
                print("Primero debe realizar la carga de los empleados")
        case 7:
            if flag_carga_diccionario:
                pass
            else:
                print("Primero debe realizar la carga de los empleados")
        case 8:
            if flag_carga_diccionario:
                pass
            else:
                print("Primero debe realizar la carga de los empleados")
        case 9:
            if flag_carga_diccionario:
                pass
            else:
                print("Primero debe realizar la carga de los empleados")
        case 10:
            if flag_carga_diccionario:
                pass
            else:
                print("Primero debe realizar la carga de los empleados")
        case 11:
            if flag_carga_diccionario:
                pass
            else:
                print("Primero debe realizar la carga de los empleados")
        case 12:
            if flag_carga_diccionario:
                pass
                flag_carga_csv = True
            else:
                print("Primero debe realizar la carga de los empleados")
        case 13:
            if flag_carga_diccionario:
                pass
                flag_carga_json = True
            else:
                print("Primero debe realizar la carga de los empleados")
        case 14:
            print("Saliendo...")
            break
import Funciones

titulo = " Menú alumnos Sysacad "
subrayado = len(titulo) * "-"
mensaje_opciones = """
01 - Ingresar alumnos\n
02 - Mostrar todos los alumnos\n
03 - Mostrar alumnos promocionados\n
04 - Mostrar alumnos aprobados\n
05 - Mostrar alumnos desaprobados\n
06 - Buscar alumno por DNI\n
07 - Mostrar totales de cada estado de aprobación\n
08 - Mostrar promedio de nota de todos los alumnos\n
09 - Mostrar promedio de nota de los alumnos masculinos\n
10 - Mostrar el procentaje de alumnos de cada género\n
11 - Mostrar el / los alumnos con mayor nota\n
12 - Mostrar la cantidad de alumnos que superan la nota promedio\n
13 - Salir\n"""

while(True):
    print(subrayado)
    print(titulo)
    print(subrayado)
    print(mensaje_opciones)

    opcion = Funciones.pedir_opcion(1, 13)

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case 12:
            pass
        case 13:
            print("Saliendo...")
            break
    
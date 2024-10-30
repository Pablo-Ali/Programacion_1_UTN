# Ali, Pablo Sharif
# DNI: 37969010
# Legajo: 112468
# Comisión 313

import Funciones_Primer_Parcial_Ali

flag_carga = False
flag_segunda_vuelta = False

while(True):
    print("-----------------------------------------")
    print("Menú\n")

    print("1 - Cargar votos")
    print("2 - Mostrar votos")
    print("3 - Ordenar votos turno mañana")
    print("4 - No te votó nadie")
    print("5 - Turno que más fue a votar")
    print("6 - Ballotage")
    print("7 - Realizar segunda vuelta")
    print("8 - Salir\n")
    
    opcion = Funciones_Primer_Parcial_Ali.pedir_opcion(1,8)

    match opcion:
        case 1:
            matriz_votos = Funciones_Primer_Parcial_Ali.inicializar_matriz(5, 4, -1)
            Funciones_Primer_Parcial_Ali.cargar_votos(matriz_votos)
            flag_carga = True
        case 2:
            if flag_carga:
                Funciones_Primer_Parcial_Ali.mostrar_votos(matriz_votos)
            else:
                print("Primero debe cargar los votos")
        case 3:
            if flag_carga:
                mat_turno_mañana = Funciones_Primer_Parcial_Ali.ordenar_matrices_segun_columna_descendente_con_copia(matriz_votos, 1)
                Funciones_Primer_Parcial_Ali.mostrar_matriz(mat_turno_mañana)
            else:
                print("Primero debe cargar los votos")
        case 4:
            if flag_carga:
                Funciones_Primer_Parcial_Ali.encontrar_listas_menores_5_prociento(matriz_votos)
            else:
                print("Primero debe cargar los votos")
        case 5:
            if flag_carga:
                Funciones_Primer_Parcial_Ali.mostrar_turno_mas_votantes(matriz_votos)
            else:
                print("Primero debe cargar los votos")
        case 6:
            if flag_carga:
                ballotage = Funciones_Primer_Parcial_Ali.verificar_ballotage(matriz_votos)
                if ballotage:
                    print("Habrá segunda vuelta")
                    flag_segunda_vuelta = True
                else:
                    print("No hrabrá segunda vuelta")
            else:
                print("Primero debe cargar los votos")
        case 7:
            if flag_carga and flag_segunda_vuelta:
                Funciones_Primer_Parcial_Ali.realizar_segunda_vuelta(matriz_votos)
            else:
                print("Primero debe cargar los votos")
        case 8:
            print("Saliendo")
            break
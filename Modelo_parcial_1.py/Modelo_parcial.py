# Ali, Pablo Sharif
# Comisión 313

import Funciones_modelo_parcial

flag_carga = False

while(True):
    print("-----------------------------------------")
    print("Menú\n")

    print("1 - Calificar bailarines")
    print("2 - Mostrar notas")
    print("3 - Ordenar bailarines jurado 2")
    print("4 - Triple 7")
    print("5 - Jurado malo")
    print("6 - Top 3")
    print("7 - Verificar ganador")
    print("8 - Salir\n")
    
    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            tabla_bailarines = Funciones_modelo_parcial.cargar_matriz_bailarines()
            Funciones_modelo_parcial.mostrar_matriz(tabla_bailarines)
            flag_carga = True
        case 2:
            if flag_carga:
                Funciones_modelo_parcial.mostrar_notas(tabla_bailarines)
            else:
                print("Primero debe cargar los datos de los bailarines")
        case 3:
            if flag_carga:
                tabla_jurado_2 = Funciones_modelo_parcial.ordenar_matrices_segun_columna_descendente_con_copia(tabla_bailarines, 2)
                Funciones_modelo_parcial.mostrar_matriz(tabla_jurado_2)
            else:
                print("Primero debe cargar los datos de los bailarines")
        case 4:
            if flag_carga:
                Funciones_modelo_parcial.mostrar_triple_7(tabla_bailarines)
            else:
                print("Primero debe cargar los datos de los bailarines")
        case 5:
            if flag_carga:
                Funciones_modelo_parcial.mostrar_aplazo_jurado_malo(tabla_bailarines)
            else:
                print("Primero debe cargar los datos de los bailarines")
        case 6:
            if flag_carga:
                Funciones_modelo_parcial.mostrar_top_3_promedio(tabla_bailarines)
            else:
                print("Primero debe cargar los datos de los bailarines")
        case 7:
            if flag_carga:
                Funciones_modelo_parcial.verificar_ganador(tabla_bailarines)
            else:
                print("Primero debe cargar los datos de los bailarines")
        case 8:
            print("Saliendo")
            break
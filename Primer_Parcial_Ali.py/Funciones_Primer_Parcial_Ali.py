# Ali, Pablo Sharif
# DNI: 37969010
# Legajo: 112468
# Comisión 313

import random

def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any = None) -> list:
    '''
    Función que se engarga de inicializar una matriz según la cantidad 
    de filas y columnas pasadas por parámetro. Por defecto se inicializa con None en cada 
    campo, pero puede modificarse por cualquier valor en el tercer parámetro.
    Retorna la matriz.
    '''
    
    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz : list) -> None:
    '''
    Función que imprime por pantalla la matriz recibida por parámetro
    '''
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def pedir_opcion(min : int, max : int) -> int:
    '''
    Función que recibe por parámetro un mínimo y un máximo y 
    se encarga de validar que el número ingresado se encuentre dentro de ese rango.
    Retorna el número.
    '''
    num = int(input("Ingrese la opción: "))

    while num < min or num > max:
        print(f"Las opciones son del {min} al {max}")
        num = int(input("Ingrese la opción: "))

    return num

def cargar_votos(matriz_votos : list) -> None:
    '''
    Función que recibe una matriz iniciada y la carga con
    los votos de las elecciones del centro de estudiantes.
    '''

    for i in range(len(matriz_votos)):
        while matriz_votos[i][0] < 100 or matriz_votos[i][0] > 999:
            matriz_votos[i][0] = int(input("Ingrese el número de lista (entre 100 y 999): "))
        while matriz_votos[i][1] < 0:
            matriz_votos[i][1] = int(input("Ingrese los votos del turno mañana: "))
        while matriz_votos[i][2] < 0:
            matriz_votos[i][2] = int(input("Ingrese los votos del turno tarde: "))
        while matriz_votos[i][3] < 0:
            matriz_votos[i][3] = int(input("Ingrese los votos del turno noche: "))

def calcular_porcentaje_votos_segun_fila(matriz_votos : list, fila : int) -> float:
    '''
    Función que recibe una matriz con votos y un numero de fila.
    Calcula el porcentaje de votos de la fila respecto al total y lo retorna.
    '''

    total_votos = 0

    for i in range(len(matriz_votos)):
        for j in range(1, len(matriz_votos[i])):
            total_votos += matriz_votos[i][j]

    return ((matriz_votos[fila][1] + matriz_votos[fila][2] + matriz_votos[fila][3]) * 100) / total_votos

def mostrar_votos(matriz_votos : list) -> None:
    '''
    Función que imprime por pantalla los resultados de la votación
    de la matriz pasada por parámetro.
    '''

    for i in range(len(matriz_votos)):
        print(f"LISTA: {matriz_votos[i][0]}")
        print(f"CANTIDAD VOTOS TURNO MAÑANA: {matriz_votos[i][1]}")
        print(f"CANTIDAD VOTOS TURNO TARDE: {matriz_votos[i][2]}")
        print(f"CANTIDAD VOTOS TURNO NOCHE: {matriz_votos[i][3]}")
        print(f"PORCENTAJE DE LOS VOTOS: {calcular_porcentaje_votos_segun_fila(matriz_votos, i)}")

def ordenar_matrices_segun_columna_descendente_con_copia(matriz : list, columna : int) -> list:
    '''
    Función que recibe una matriz y un entero que representa una de sus columnas.
    Retorna una copia de la matriz ordenada de mayor a menor.
    '''
    flag = 1
    matriz_ordenada = matriz.copy()
    
    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if  matriz_ordenada[i][columna] < matriz_ordenada[i + 1][columna]:
                aux = matriz_ordenada[i]
                matriz_ordenada[i] = matriz_ordenada[i + 1]
                matriz_ordenada[i + 1] = aux
                flag = 1

    return matriz_ordenada

def encontrar_listas_menores_5_prociento(matriz_votos : list) -> None:
    '''
    Función que recibe una matriz con votos. Muestra por pantalla a aquellas
    listas que posean menos del 5% de los votos.
    '''

    for i in range(len(matriz_votos)):
        porcentaje = calcular_porcentaje_votos_segun_fila(matriz_votos, i)
        if porcentaje < 5:
            print(f"La lista {matriz_votos[i][0]} fue votada por menos del 5% del padrón")

def calcular_votantes_por_turno(matriz_votos : list) -> list:
    '''
    Función que recibe la matriz de votos y retorna otra matriz con los votantes por turno
    '''

    votantes_mañana = 0
    votantes_tarde = 0
    votantes_noche = 0

    for i in range(len(matriz_votos)):
        votantes_mañana += matriz_votos[i][1]
    for i in range(len(matriz_votos)):
        votantes_tarde += matriz_votos[i][2]
    for i in range(len(matriz_votos)):
        votantes_noche += matriz_votos[i][3]

    matriz_turnos = [
        ["Turno mañana", votantes_mañana],
        ["Turno tarde", votantes_tarde],
        ["Turno noche", votantes_noche]
    ]

    return matriz_turnos


def mostrar_turno_mas_votantes(matriz_votos : list) -> None:
    '''
    Función que recibe una matriz con votos. Calcula qué turno tuvo la mayor cantidad
    de votantes y lo imprime por pantalla. En caso de ser más de uno, lo informa.
    '''

    matriz_turnos = calcular_votantes_por_turno(matriz_votos)

    matriz_ordenada = ordenar_matrices_segun_columna_descendente_con_copia(matriz_turnos, 1)

    if matriz_ordenada[0][1] > matriz_ordenada[1][1]:
        print(f"Turno que más fue a votar: {matriz_ordenada[0][0]}")
    elif matriz_ordenada[0][1] == matriz_ordenada[1][1] and matriz_ordenada[0][1] == matriz_ordenada[2][1]:
        print("Todos los turnos tuvieron la misma cantidad de votantes")
    else:
        print(f"Los turnos con más votantes fueron: {matriz_ordenada[0][0]} y {matriz_ordenada[1][0]}")

def verificar_ballotage(matriz_votos : list) -> bool:
    '''
    Función que recibe una matriz de votos y verifica si habrá ballotage.
    En caso de que ninguna lista llegue a superar el 50%, retorna True,
    caso contrario, False.
    '''

    for i in range(len(matriz_votos)):
        flag_ballotage = True

        porcentaje = calcular_porcentaje_votos_segun_fila(matriz_votos, i)
        if porcentaje > 50:
            flag_ballotage = False

    return flag_ballotage

def realizar_segunda_vuelta(matriz_votos : list) -> None:
    '''
    Función que se encarga de realizar la segunda vuelta de las votaciones.
    Imprime al ganador.
    '''

    matriz_porcentajes = inicializar_matriz(len(matriz_votos), 2)

    for i in range(len(matriz_porcentajes)):
        matriz_porcentajes[i][0] = matriz_votos[i][0]
        matriz_porcentajes[i][1] = calcular_porcentaje_votos_segun_fila(matriz_votos, i)

    matriz_ordenada = ordenar_matrices_segun_columna_descendente_con_copia(matriz_porcentajes, 1)

    primer_candidato = matriz_ordenada[0][0]
    segundo_candidato = matriz_ordenada[1][0]

    turno_mañana = int(input("Ingresar total votantes turno mañana: "))
    turno_tarde = int(input("Ingresar total votantes turno tarde: "))
    turno_noche = int(input("Ingresar total votantes turno noche: "))

    votantes_primer_candidato_mañana = random.randint(0, turno_mañana)
    votantes_primer_candidato_tarde = random.randint(0, turno_tarde)
    votantes_primer_candidato_noche = random.randint(0, turno_noche)

    votantes_segundo_candidato_mañana = turno_mañana - votantes_primer_candidato_mañana
    votantes_segundo_candidato_tarde = turno_tarde - votantes_primer_candidato_tarde
    votantes_segundo_candidato_noche = turno_noche - votantes_primer_candidato_noche

    total_primero = votantes_primer_candidato_mañana + votantes_primer_candidato_tarde + turno_noche
    total_segundo = votantes_segundo_candidato_mañana + votantes_segundo_candidato_tarde + votantes_segundo_candidato_noche

    if total_primero == total_segundo:
        print("Empataron, se retoma la semana siguiente")
    elif total_primero > total_segundo:
        print(f"Ganó la lista {primer_candidato}")
    else:
        print(f"Ganó la lista {segundo_candidato}")
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

def ordenar_matriz_doble_criterio_descendente_con_copia(matriz : list, criterio_1 : int, criterio_2 : int) -> list:
    '''
    Función que recibe una matriz y dos enteros que funcionan como criterios de ordenamiento.
    Retorna una copia de la matriz ordenada según la columna del criterio 1. En caso de haber valores iguales,
    aplica el ordenamiento según la columna del criterio 2.
    '''

    flag = 1
    matriz_ordenada = matriz.copy()

    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if  (matriz_ordenada[i][criterio_1] < matriz_ordenada[i + 1][criterio_1]) or (
                (matriz_ordenada[i][criterio_1] == matriz_ordenada[i + 1][criterio_1]) and 
                (matriz_ordenada[i][criterio_2] < matriz_ordenada[i + 1][criterio_2])):
                
                aux = matriz_ordenada[i]
                matriz_ordenada[i] = matriz_ordenada[i + 1]
                matriz_ordenada[i + 1] = aux
                flag = 1

    return matriz_ordenada

def ingresar_nota() -> int:
    '''
    Función que se encarga de pedir una nota por teclado 
    y verifica que esta sesté entre uno y diez.
    Finalmente, retorna la nota.
    '''

    nota = int(input("Ingrese la nota: "))

    while nota < 1 or nota > 10:
        print("La nota final debe ser del 1 al 10.")
        nota = int(input("Ingrese la nota: "))

    return nota

#------------------------------------hasta acá, funciones que ya tenía hechas-------------------------

def cargar_matriz_bailarines() -> list:
    '''
    Función que carga los datos de los bailarines en una matriz.
    Retorna la matriz.
    '''
    matriz = inicializar_matriz(10, 5)
    
    for i in range (len(matriz)):
        matriz[i][0] = i + 1
        matriz[i][1] = ingresar_nota()
        matriz[i][2] = ingresar_nota()
        matriz[i][3] = ingresar_nota()
        matriz[i][4] = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3

    return matriz


def mostrar_notas(matriz_bailarines : list) -> None:
    '''
    Función que recibe la matriz de bailarines e
    imprime sus notas.
    '''

    for i in range(len(matriz_bailarines)):
        print(f"Nro participante: {i + 1}")
        print(f"Nota jurado 1: {matriz_bailarines[i][1]}")
        print(f"Nota jurado 2: {matriz_bailarines[i][2]}")
        print(f"Nota jurado 3: {matriz_bailarines[i][3]}")
        print(f"Promedio: {matriz_bailarines[i][4]}")

def mostrar_triple_7(matriz_bailarines : list) -> None:
    '''
    Función que recibe una matriz de bailarines e
    imprime aquellos participantes que tengan 7 en
    todas sus notas. En caso de no haber, lo notifica.
    '''

    flag = True

    for i in range(len(matriz_bailarines)):
        if matriz_bailarines[i][1] == 7 and matriz_bailarines[i][2] == 7 and matriz_bailarines[i][3] == 7:
            print(f"El bailarín nro {matriz_bailarines[i][0]} obtuvo triple 7")
            flag = False

    if flag:
        print("No hubo participantes que obtuvieran triple 7")

def mostrar_aplazo_jurado_malo(matriz_bailarines : list) -> None:
    '''
    Función que recibe una matriz de bailarines e
    imprime aquellos participantes aplazados por el jurado 3.
    En caso de no haber, lo notifica.
    '''

    flag = True

    for i in range(len(matriz_bailarines)):
        if matriz_bailarines[i][3] < 4:
            print(f"El bailarín nro {matriz_bailarines[i][0]} aplazó con {matriz_bailarines[i][3]}")
            flag = False

    if flag:
        print("No hubo participantes aplazados por el jurado 3")


def mostrar_top_3_promedio(matriz_bailarines : list) -> None:
    '''
    Función que recibe una matriz de bailarines e
    imprime el top 3 de promedios.
    '''
    matriz_ordenada = ordenar_matrices_segun_columna_descendente_con_copia(matriz_bailarines, 4)

    for i in range(3):
        print(f"Bailarín nro : {matriz_ordenada[i][0]} promedio: {matriz_ordenada[i][4]}")

def verificar_ganador(matriz_bailarines : list) -> None:
    '''
    Función que recibe una matriz de bailarines con promedio e
    imprime al ganador. En caso de empatar los promedios, se dirime según
    el jurado 1. Si vuelven a empatar, se muestran todos los ganadores.
    '''
    promedio_ordenado = ordenar_matriz_doble_criterio_descendente_con_copia(matriz_bailarines, 4, 1)

    promedio_mayor = promedio_ordenado[0][4]
    nota_jurado_1_mayor = promedio_ordenado[0][1]
    for i in range(len(promedio_ordenado)):
        if promedio_ordenado[i][4] == promedio_mayor and promedio_ordenado[i][1] == nota_jurado_1_mayor:
            print(f"Ganador: bailarín nro {promedio_ordenado[i][0]}, con promedio {promedio_ordenado[i][4]} y nota del jurado 1 {promedio_ordenado[i][1]}")
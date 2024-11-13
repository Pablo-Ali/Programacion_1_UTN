#-----Matrices-----

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

def validar_largo(matriz_1 : list, matriz_2 : list) -> bool:
    '''
    Función que recibe dos matrices y compara su tamaño.
    Retorna True si son del mismo tamaño, False en caso contrario.
    '''
    
    filas_m1 = len(matriz_1)
    filas_m2 = len(matriz_2)
    columnas_m1 = len(matriz_1[0])
    columnas_m2 = len(matriz_2[0])

    if filas_m1 == filas_m2 and columnas_m1 == columnas_m2:
        return True

    else:
        return False
    
def validar_largo_multi(matriz_1 : list, matriz_2 : list) -> bool:
    '''
    Función que recibe dos matrices y compara su tamaño.
    Retorna True si pueden multiplicarse en el
    orden ingresado, False en caso contrario.
    '''
    
    filas_m2 = len(matriz_2)
    columnas_m1 = len(matriz_1[0])

    if filas_m2 == columnas_m1:
        return True

    else:
        return False

def calcular_matriz_traspuesta(matriz : list) -> list:
    '''
    Función que recibe una matriz y retorna su traspuesta
    '''

    matriz_r = inicializar_matriz(len(matriz[0]), len(matriz))

    for i in range (len(matriz_r)):
        for j in range (len(matriz_r[i])):
            matriz_r[i][j] = matriz[j][i]
    
    return matriz_r

def calcular_matriz_opuesta(matriz : list) -> list:
    '''
    Función que recibe una matriz y retorna su opuesta.
    '''

    matriz_r = inicializar_matriz(len(matriz), len(matriz[0]))

    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            matriz_r[i][j] = matriz[i][j] * -1
    
    return matriz_r

#-----Carga-----

def ingresar_nota() -> int:
    '''
    Función que se encarga de pedir una nota por teclado 
    y verifica que esta esté entre uno y diez.
    Finalmente, retorna la nota.
    '''

    nota = int(input("Ingrese la nota: "))

    while nota < 1 or nota > 10:
        print("La nota final debe ser del 1 al 10.")
        nota = int(input("Ingrese la nota: "))

    return nota

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


#-----Ordenamiento-----

def ordenar_arreglo_burbuja_ascendente(lista : list) -> None:
    '''
    Función que recibe un arreglo de números y lo ordena de menor 
    a mayor.
    '''
    flag = 1
    
    while flag:
        flag = 0
        for i in range (len(lista) - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag = 1


def ordenar_arreglo_burbuja_con_copia(lista : list) -> list:
    '''
    Función que recibe un arreglo de números y lo ordena de menor 
    a mayor.
    Retorna una copia ordenada sin afectar a la lista original.
    '''
    flag = 1
    lista_ordenada = lista.copy()
    
    while flag:
        flag = 0
        for i in range (len(lista) - 1):
            if lista_ordenada[i] > lista_ordenada[i + 1]:
                aux = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[i + 1]
                lista_ordenada[i + 1] = aux
                flag = 1   

    return lista_ordenada

def ordenar_matrices_segun_columna_ascendente(matriz : list, columna : int) -> None:
    '''
    Función que recibe una matriz y un entero que representa una de sus columnas.
    Ordena esa matriz de menor a mayor.
    '''
    flag = 1
    
    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if  matriz[i][columna] > matriz[i + 1][columna]:
                aux = matriz[i]
                matriz[i] = matriz[i + 1]
                matriz[i + 1] = aux
                flag = 1

def ordenar_matrices_segun_columna_ascendente_con_copia(matriz : list, columna : int) -> list:
    '''
    Función que recibe una matriz y un entero que representa una de sus columnas.
    Ordena esa matriz de menor a mayor.
    Retorna una copia de la matriz ordenada sin afectar a la original.
    '''
    flag = 1
    matriz_ordenada = matriz.copy()
    
    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if  matriz_ordenada[i][columna] > matriz_ordenada[i + 1][columna]:
                aux = matriz_ordenada[i]
                matriz_ordenada[i] = matriz_ordenada[i + 1]
                matriz_ordenada[i + 1] = aux
                flag = 1

    return matriz_ordenada

def ordenar_matriz_doble_criterio_ascendente(matriz : list, criterio_1 : int, criterio_2 : int) -> None:
    '''
    Función que recibe una matriz y dos enteros que funcionan como criterios de ordenamiento.
    Ordena la matriz según la columna del criterio 1. En caso de haber valores iguales,
    aplica el ordenamiento según la columna del criterio 2.
    '''

    flag = 1

    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if  (matriz[i][criterio_1] > matriz[i + 1][criterio_1]) or (
                (matriz[i][criterio_1] == matriz[i + 1][criterio_1]) and 
                (matriz[i][criterio_2] > matriz[i + 1][criterio_2])):
                
                aux = matriz[i]
                matriz[i] = matriz[i + 1]
                matriz[i + 1] = aux
                flag = 1

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

#-----Diccionarios y listas de diccionarios-----

def mostrar_diccionario(diccionario) -> None:
    '''
    '''

    for clave,valor in diccionario.items():
        print(f"{clave.title().replace("-"," ")} : {valor}")

def mostrar_lista_diccionario(lista : list) -> bool:
    '''
    '''

    retorno = False

    for elemento in lista:
        mostrar_diccionario(elemento)
        print("")
        retorno = True
    
    return retorno
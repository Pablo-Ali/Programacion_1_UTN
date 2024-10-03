# Ali, Pablo Sharif
# Comisión 313

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


m_1 = [
    [1, 35],
    [4, -9],
    [-5, 7]
]

m_2 = [

    [72, 6],
    [-8, 5],
    [13, 3]
]

m_3 = [
    [1, 2, 3],
    [4, 5, 6]
]

# 1

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
    
def sumar_matrices(matriz_1 : list, matriz_2 : list) -> list:
    '''
    Función que recibe dos matrices y retorna su suma.
    '''

    matriz = inicializar_matriz(len(matriz_1), len(matriz_1[0]))

    for i in range (len(matriz_1)):
        for j in range (len(matriz_1[i])):
            matriz[i][j] = matriz_1[i][j] + matriz_2[i][j]

    return matriz



mismo_tamaño = validar_largo(m_1, m_2)

if mismo_tamaño:
    matriz_resultado = sumar_matrices(m_1, m_2)
    mostrar_matriz(matriz_resultado)
else:
    matriz_resultado = []
    print(matriz_resultado)


# 2

def multiplicar_matriz_escalar(matriz_1 : list, escalar : int) -> list:
    '''
    Función que recibe una matriz y un escalar y retorna la multiplicación.
    '''

    matriz = inicializar_matriz(len(matriz_1), len(matriz_1[0]))

    for i in range (len(matriz_1)):
        for j in range (len(matriz_1[i])):
            matriz[i][j] = matriz_1[i][j] * escalar
    
    return matriz

matriz_resultado_2 = multiplicar_matriz_escalar(m_1, 10)
mostrar_matriz(matriz_resultado_2)

# 3

def calcular_matriz_opuesta(matriz : list) -> list:
    '''
    Función que recibe una matriz y retorna su opuesta.
    '''

    matriz_r = inicializar_matriz(len(matriz), len(matriz[0]))

    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            matriz_r[i][j] = matriz[i][j] * -1
    
    return matriz_r

matriz_resultado_3 = calcular_matriz_opuesta(m_1)
mostrar_matriz(matriz_resultado_3)

# 4

def calcular_matriz_traspuesta(matriz : list) -> list:
    '''
    Función que recibe una matriz y retorna su traspuesta
    '''

    matriz_r = inicializar_matriz(len(matriz[0]), len(matriz))

    for i in range (len(matriz_r)):
        for j in range (len(matriz_r[i])):
            matriz_r[i][j] = matriz[j][i]
    
    return matriz_r

matriz_resultado_4 = calcular_matriz_traspuesta(m_1)
mostrar_matriz(matriz_resultado_4)

# 5

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


def multiplicar_matrices (matriz_1 : list, matriz_2 : list) -> list:
    '''
    Función que recibe dos matrices y retorna su multiplicación
    '''
    
    matriz_resultado = inicializar_matriz(len(matriz_1), len(matriz_2[0]))

    for i in range(len(matriz_resultado)):
        for j in range(len(matriz_resultado[0])):
            resultado = 0
            for k in range(len(matriz_2)):
                resultado += matriz_1[i][k] * matriz_2[k][j]
            matriz_resultado[i][j] = resultado

    return matriz_resultado

m = [
    [4, 1, -2],
    [1, 2, 6]
]
m2 = [
    [2, 1],
    [2, 1],
    [2, 3]
]

multiplicable = validar_largo_multi(m, m2)
multiplicable_2 = validar_largo_multi(m_1, m_2)

if multiplicable:
    r = multiplicar_matrices(m,m2)
    mostrar_matriz(r)
else:
    r = []
    print(r)

if multiplicable_2:
    r_2 = multiplicar_matrices(m_1, m_2)
    mostrar_matriz(r_2)
else:
    r_2 = []
    print(r_2)

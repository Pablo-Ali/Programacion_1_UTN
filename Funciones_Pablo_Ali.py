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

#-----Ordenamiento-----

def ordenar_arreglo_burbuja(lista : list) -> None:
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

def ordenar_matrices_segun_columna(matriz : list, columna : int) -> None:
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

def ordenar_matrices_segun_columna_con_copia(matriz : list, columna : int) -> list:
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

def ordenar_matriz_doble_criterio(matriz : list, criterio_1 : int, criterio_2 : int) -> None:
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

# Cadenas

def es_alfabetico(cadena : str) -> bool:
    '''
    Función que recibe una cadena de caracteres,
    revisa que sólo posea caracteres alfabéticos.
    Retorna True si es así, False en caso contrario.
    '''

    resultado = True

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])
        if (c_ascii < 65) or (c_ascii > 90 and c_ascii < 97) or (c_ascii > 122):
            resultado = False

    return resultado

def convertir_caracter_mayuscula(cadena : str) -> str | None:
    '''
    Función que recibe un caracter.
    Si es posible, lo convierte a mayúscula.
    Si ya está en mayúscula o es otro tipo de caracter, lo retorna.
    Si hay más de un caracter, retorna None.
    '''

    if len(cadena) > 1:
        return None
    
    if ord(cadena) > 97 and ord(cadena) < 122:
        return chr(ord(cadena) - 32)
    else:
        return cadena

def capitalizar_texto(cadena : str) -> str:
    '''
    Función que convierte la primera letra de la cadena a mayúscula.
    Retorna la nueva cadena.
    '''

    cadena_retorno = ""

    for i in range(len(cadena)):
        if i == 0:
            c_ascii = ord(cadena[i])
            if c_ascii >= 97 and c_ascii <= 122:
                aux = c_ascii - 32
                cadena_retorno += chr(aux)
            else:
                cadena_retorno += cadena[i]
        else:
            cadena_retorno += cadena[i]

    return cadena_retorno

def generar_titulo(cadena : str) -> str:
    '''
    Función que recibe una cadena de caracteres.
    Convierte las letras iniciales de cada palabra a mayúscula.
    Retorna la nueva cadena.
    '''

    cadena_retorno = ""

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])

        if i == 0:
            if c_ascii >= 97 and c_ascii <= 122:
                aux = c_ascii - 32
                cadena_retorno += chr(aux)
            else:
                cadena_retorno += cadena[i]
        else:
            if cadena[i - 1] == " ":
                if c_ascii >= 97 and c_ascii <= 122:
                    aux = c_ascii - 32
                    cadena_retorno += chr(aux)
                else:
                    cadena_retorno += cadena[i]
            else:
                if c_ascii >= 65 and c_ascii <= 90:
                    aux = c_ascii + 32
                    cadena_retorno += chr(aux)
                else:
                    cadena_retorno += cadena[i]
    
    return cadena_retorno

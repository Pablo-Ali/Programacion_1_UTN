# Ali, Pablo Sharif
# Comisión 313

def mostrar_matriz(matriz : list) -> None:
    '''
    Función que imprime por pantalla la matriz recibida por parámetro
    '''
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")


# Ordenamiento de doble criterio

# 1

def ordenar_matriz_doble_criterio_des(matriz : list, criterio_1 : int, criterio_2 : int) -> None:
    '''
    Función que recibe una matriz y dos enteros que funcionan como criterios de ordenamiento.
    Ordena la matriz de forma descendente según la columna del criterio 1.
    En caso de haber valores iguales, aplica el ordenamiento según la columna del criterio 2.
    '''

    flag = 1

    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if  (matriz[i][criterio_1] < matriz[i + 1][criterio_1]) or (
                (matriz[i][criterio_1] == matriz[i + 1][criterio_1]) and 
                (matriz[i][criterio_2] < matriz[i + 1][criterio_2])):
                
                aux = matriz[i]
                matriz[i] = matriz[i + 1]
                matriz[i + 1] = aux
                flag = 1



matriz_productos = [
    ["Jabón", 5, 47],
    ["Detergente", 8, 32],
    ["Suavizante", 8, 37],
    ["Pastilla", 9, 12]
]


ordenar_matriz_doble_criterio_des(matriz_productos, 1, 2)
mostrar_matriz(matriz_productos)

# 2

def ordenar_matriz_doble_criterio_des_as(matriz : list, criterio_1 : int, criterio_2 : int) -> None:
    '''
    Función que recibe una matriz y dos enteros que funcionan como criterios de ordenamiento.
    Ordena la matriz según la columna del criterio 1, que será
    descendente. En caso de haber valores iguales, aplica el ordenamiento según
    la columna del criterio 2, aquí ascendente.
    '''

    flag = 1

    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if  (matriz[i][criterio_1] < matriz[i + 1][criterio_1]) or (
                (matriz[i][criterio_1] == matriz[i + 1][criterio_1]) and 
                (matriz[i][criterio_2] > matriz[i + 1][criterio_2])):
                
                aux = matriz[i]
                matriz[i] = matriz[i + 1]
                matriz[i + 1] = aux
                flag = 1

matriz_productos_2 = [
    ["Jabón", 5, 47],
    ["Detergente", 8, 32],
    ["Suavizante", 8, 37],
    ["Pastilla", 9, 12]
]

print("------")
ordenar_matriz_doble_criterio_des_as(matriz_productos_2, 1, 0)
mostrar_matriz(matriz_productos_2)

# 3

def ordenar_matriz_doble_criterio_eleccion(matriz : list, criterio_1 : int, criterio_2 : int, eleccion : str) -> None:
    '''
    Función que recibe una matriz, dos enteros que funcionan como criterios de ordenamiento y
    un string que determina si el ordenamiento será ascendente o descentente.
    Ordena la matriz según la columna del criterio 1. En caso de haber valores iguales,
    aplica el ordenamiento según la columna del criterio 2.
    '''

    flag = 1

    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if eleccion == "d":
                if  (matriz[i][criterio_1] < matriz[i + 1][criterio_1]) or (
                    (matriz[i][criterio_1] == matriz[i + 1][criterio_1]) and 
                    (matriz[i][criterio_2] < matriz[i + 1][criterio_2])):
                    aux = matriz[i]
                    matriz[i] = matriz[i + 1]
                    matriz[i + 1] = aux
                    flag = 1
            else:
                if  (matriz[i][criterio_1] > matriz[i + 1][criterio_1]) or (
                    (matriz[i][criterio_1] == matriz[i + 1][criterio_1]) and 
                    (matriz[i][criterio_2] > matriz[i + 1][criterio_2])):
                    aux = matriz[i]
                    matriz[i] = matriz[i + 1]
                    matriz[i + 1] = aux
                    flag = 1

matriz_productos_3 = [
    ["Jabón", 5, 47],
    ["Detergente", 8, 32],
    ["Suavizante", 8, 37],
    ["Pastilla", 9, 12]
]

print("------")
ordenar_matriz_doble_criterio_eleccion(matriz_productos_3, 0, 1, "a")
mostrar_matriz(matriz_productos_3)
print("------")
ordenar_matriz_doble_criterio_eleccion(matriz_productos_3, 0, 1, "d")
mostrar_matriz(matriz_productos_3)

# 4

def ordenar_matriz_doble_criterio_eleccion_doble(matriz : list, criterio_1 : int, criterio_2 : int, eleccion_1 : str, eleccion_2 : str) -> None:
    '''
    Función que recibe una matriz, dos enteros que funcionan como criterios de ordenamiento y
    un string que determina si el ordenamiento será ascendente o descentente.
    Ordena la matriz según la columna del criterio 1. En caso de haber valores iguales,
    aplica el ordenamiento según la columna del criterio 2.
    '''

    flag = 1

    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if (eleccion_1 == "d") and (matriz[i][criterio_1] < matriz[i + 1][criterio_1]):  
                aux = matriz[i]
                matriz[i] = matriz[i + 1]
                matriz[i + 1] = aux
                flag = 1
            elif (eleccion_1 == "a") and (matriz[i][criterio_1] > matriz[i + 1][criterio_1]):
                aux = matriz[i]
                matriz[i] = matriz[i + 1]
                matriz[i + 1] = aux
                flag = 1
            elif matriz[i][criterio_1] == matriz[i + 1][criterio_1]:
                if eleccion_2 == "d":
                    if matriz[i][criterio_2] < matriz[i + 1][criterio_2]:
                        aux = matriz[i]
                        matriz[i] = matriz[i + 1]
                        matriz[i + 1] = aux
                        flag = 1
                if eleccion_2 == "a":
                    if matriz[i][criterio_2] > matriz[i + 1][criterio_2]:
                        aux = matriz[i]
                        matriz[i] = matriz[i + 1]
                        matriz[i + 1] = aux
                        flag = 1


matriz_productos_4 = [
    ["Jabón", 5, 47],
    ["Detergente", 8, 32],
    ["Suavizante", 8, 37],
    ["Pastilla", 9, 12]
]

print("------")
ordenar_matriz_doble_criterio_eleccion_doble(matriz_productos_4, 1, 2, "a", "d")
mostrar_matriz(matriz_productos_4)
print("------")
ordenar_matriz_doble_criterio_eleccion_doble(matriz_productos_4, 1, 2, "d", "a")
mostrar_matriz(matriz_productos_4)

# Cadenas

# 5

def contar_vocales(cadena : str) -> int:
    '''
    Función que recibe una cadena de caracteres y retorna la 
    cantidad de vocales presentes.
    '''

    contador = 0

    for letra in cadena:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E'or letra == 'I' or letra == 'O' or letra == 'U':
            contador += 1

    return contador

cadena = "Hola mundo. Esta es una cadena para probar cosas" # 18 voc, 21 cons

print(contar_vocales(cadena))

# 6

def contar_consonantes(cadena : str) -> int:
    '''
    Función que recibe una cadena de caracteres y retorna la 
    cantidad de consonantes presentes.
    '''

    contador = 0

    for letra in cadena:
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u' and letra != 'A' and letra != 'E'and letra != 'I' and letra != 'O' and letra != 'U' and letra != " " and letra != "." and letra != ",":
            contador += 1

    return contador

print(contar_consonantes(cadena))

# 7

def quitar_espacios(cadena : str) -> str:
    '''
    Función que recibe una cadena de caracteres.
    Borra los espacios en blanco y retorna una nueva
    cadena sin estos.
    '''
    cadena_retorno = ""
    for i in range(len(cadena)):
        if cadena[i] != " ":
            cadena_retorno += cadena[i]
    return cadena_retorno

cadena_sin_espacios = quitar_espacios(cadena)
print(cadena_sin_espacios)

# 8

def repetir_cadena(cadena : str, repetidor : int) -> str:
    '''
    Función que recibe una cadena de caracteres y un número entreo.
    Retorna una nueva cadena con la primera repetida por la cantidad 
    de veces ingresada por parámetro.
    '''

    cadena_retorno = ""

    for i in range(repetidor):
        if i == repetidor - 1:
            cadena_retorno += cadena
        else:
            cadena_retorno += (cadena + " ")

    return cadena_retorno

cadena_repetida = repetir_cadena("hola", 5)
print(cadena_repetida)

#verificación rápida de que no generó espacio en blanco al final

contdor  = 0

for letra in cadena_repetida:
    contdor += 1

print(contdor)
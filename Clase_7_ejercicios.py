# Ali, Pablo Sharif
# Comisión 313

# 1

import random


def calcular_promedio(lista_enteros : list) -> float:
    '''
    Función que recibe un lista de números enteros,
    suma sus componentes y luego retorna el promedio.
    '''
    suma = 0
    for i in lista_enteros:
        suma += i
    
    return suma / len(lista_enteros)

lista_enteros = [5, 7, 10]

print(calcular_promedio(lista_enteros))

# 2

def calcular_promedio_positivos(lista_enteros : list) -> float|str:
    '''
    Función que recibe un lista de números enteros.
    Suma sus positivos y luego retorna el promedio.
    En caso de no haber positivos, retorna un string que lo aclara.
    '''
    suma_positivos = 0
    contador_positivos = 0
    for i in lista_enteros:
        if i % 2 == 0:
            suma_positivos += i
            contador_positivos += 1
    
    if suma_positivos > 0:
        return suma_positivos / contador_positivos
    else:
        return "No hay números positivos"
    
print(calcular_promedio_positivos([1, 4, 6, 9, 11]))
print(calcular_promedio_positivos([1, 9, 11]))

# 3

def calcular_producto(lista_enteros : list) -> int:
    '''
    Función que recibe un lista de números enteros 
    y retorna el producto de sus elementos.
    '''
    producto = 1
    for i in lista_enteros:
        producto *= i
    
    return producto

print(calcular_producto([2, 3, 5]))

# 4

def retornar_indice_num_max(lista_enteros : list) -> int:
    '''
    Recibe una lista de enteros y retorna el índice del número mayor.
    '''

    indice_max = 0
    numero_max = 0

    for i in range (len(lista_enteros) - 1):
        if i == 0:
            numero_max = lista_enteros[i]
            indice_max = i
        if lista_enteros[i] > numero_max:
            numero_max = lista_enteros[i]
            indice_max = i
    
    return indice_max

print(retornar_indice_num_max([2, 5, 5, 3, 1]))

# 5

def imprimir_indice_num_max_y_numero(lista_enteros : list):
    '''
    Recibe una lista de enteros e imprime el índice y el número mayor.
    '''
    
    indice_max = 0
    numero_max = 0

    for i in range (len(lista_enteros) - 1):
        if i == 0:
            numero_max = lista_enteros[i]
            indice_max = i
        if lista_enteros[i] > numero_max:
            numero_max = lista_enteros[i]
            indice_max = i
    
    print(f"Índice: {indice_max}\nNúmero: {numero_max}")

imprimir_indice_num_max_y_numero([2, 5, 5, 3, 1])

# 6

def retornar_todos_indices_num_max(lista_enteros : list) -> list:
    '''
    Recibe una lista de enteros y retorna una lista con los índices 
    del número mayor.
    '''

    numero_max = 0
    lista_indices = []

    for i in range (len(lista_enteros) - 1):
        if i == 0:
            numero_max = lista_enteros[i]
        if lista_enteros[i] > numero_max:
            numero_max = lista_enteros[i]

    for i in range (len(lista_enteros) - 1):
        if lista_enteros[i] == numero_max:
            lista_indices.append(i)

    return lista_indices

print(retornar_todos_indices_num_max([2, 5, 5, 3, 1]))

# 7

def imprimir_todos_indices_y_num_max(lista_enteros : list):
    '''
    Recibe una lista de enteros y imprime
    '''

    numero_max = 0
    
    for i in range (len(lista_enteros) - 1):
        if i == 0:
            numero_max = lista_enteros[i]
        if lista_enteros[i] > numero_max:
            numero_max = lista_enteros[i]

    for i in range (len(lista_enteros) - 1):
        if lista_enteros[i] == numero_max:
            print(f"Índice: {i}\nNúmero: {numero_max}")

imprimir_todos_indices_y_num_max([2, 5, 5, 3, 1])

# 8

def crear_lista_sueldos() -> list:
    '''
    Retorna una lista de 10 sueldos aleatorios entre 350000 y 1250000
    '''
    lista_sueldos = []

    for i in range (10):
        lista_sueldos.append(random.randint(350000, 1250000))

    return lista_sueldos

def calcular_cant_superan_promedio(lista_enteros :list) -> int:
    '''
    Recibe una lista de enteros, calcula el promedio y retorna cuantos superan ese número
    '''

    suma = 0
    contador = 0

    for i in lista_enteros:
        suma += i

    promedio = suma / len(lista_enteros)

    for i in lista_enteros:
        if i > promedio:
            contador += 1

    return contador

lista_sueldos = crear_lista_sueldos()

print(calcular_cant_superan_promedio(lista_sueldos))
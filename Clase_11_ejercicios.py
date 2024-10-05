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


# 1 

def ordenar_lista_ascendente(lista : list) -> bool:
    '''
    Función que recibe un arreglo de números y lo ordena de menor 
    a mayor.
    Retorna True si hubo cambios, False si ya estaba ordenado.
    '''

    flag = 1
    ordenada = False
    
    while flag:
        flag = 0
        for i in range (len(lista) - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag = 1
                ordenada = True

    return ordenada

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [3, 1, 5, 2, 4]

print(ordenar_lista_ascendente(lista_1))
print(ordenar_lista_ascendente(lista_2))

# 2 

def ordenar_lista_descendente(lista : list) -> bool:
    '''
    Función que recibe un arreglo de números y lo ordena de menor 
    a mayor.
    Retorna True si hubo cambios, False si ya estaba ordenado.
    '''

    flag = 1
    ordenada = False
    
    while flag:
        flag = 0
        for i in range (len(lista) - 1):
            if lista[i] < lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag = 1
                ordenada = True

    return ordenada

lista_3 = [5, 4, 3, 2, 1]
lista_4 = [3, 1, 5, 2, 4]

print(ordenar_lista_descendente(lista_3))
print(ordenar_lista_descendente(lista_4))

# 3

def ordenar_lista_eleccion(lista : list, criterio : str) -> int:
    '''
    Función que recibe un arreglo de números y un criterio de ordenamiento.
    Ordena el arreglo según el criterio seleccionado y retorna la cantidad de intercambios.
    '''

    flag = 1
    contador = 0
    
    while flag:
        flag = 0
        for i in range (len(lista) - 1):
            if criterio == "a":
                if lista[i] > lista[i + 1]:
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    flag = 1
                    contador += 1
            else:
                if lista[i] < lista[i + 1]:
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    flag = 1
                    contador += 1

    return contador


lista_5 = [3, 1, 5, 2, 4]
lista_6 = [3, 1, 5, 2, 4]

print(ordenar_lista_eleccion(lista_5, "a"))
print(lista_5)
print(ordenar_lista_eleccion(lista_6, "d"))
print(lista_6)

# 4

def ordenar_lista_str_eleccion(lista : list, criterio : str) -> int:
    '''
    Función que recibe un arreglo de strings y un criterio de ordenamiento.
    Ordena el arreglo según el criterio seleccionado y retorna la cantidad de intercambios.
    '''

    flag = 1
    contador = 0
    
    while flag:
        flag = 0
        for i in range (len(lista) - 1):
            if criterio == "a":
                if lista[i] > lista[i + 1]:
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    flag = 1
                    contador += 1
            else:
                if lista[i] < lista[i + 1]:
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    flag = 1
                    contador += 1

    return contador

lista_str_1 = ["Paula", "Pablo", "María", "José"]
lista_str_2 = ["Paula", "Pablo", "María", "José"]

print(ordenar_lista_str_eleccion(lista_str_1, "a"))
print(lista_str_1)
print(ordenar_lista_str_eleccion(lista_str_2, "d"))
print(lista_str_2)

# 5

def ordenar_lista_str_eleccion_por_largo(lista : list, criterio : str) -> int:
    '''
    Función que recibe un arreglo de strings y un criterio de ordenamiento.
    Ordena el arreglo según el criterio seleccionado según el largo
    de los strings y retorna la cantidad de intercambios.
    '''

    flag = 1
    contador = 0
    
    while flag:
        flag = 0
        for i in range (len(lista) - 1):
            if criterio == "a":
                if len(lista[i]) > len(lista[i + 1]):
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    flag = 1
                    contador += 1
            else:
                if len(lista[i]) < len(lista[i + 1]):
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    flag = 1
                    contador += 1

    return contador

lista_str_3 = ["Paula", "Pablo", "Fernanda", "José"]
lista_str_4 = ["Paula", "Pablo", "Fernanda", "José"]

print(ordenar_lista_str_eleccion_por_largo(lista_str_3, "a"))
print(lista_str_3)
print(ordenar_lista_str_eleccion_por_largo(lista_str_4, "d"))
print(lista_str_4)

# 6

def ordenar_matrices_segun_columna_y_eleccion(matriz : list, columna : int, criterio : str) -> int:
    '''
    Función que recibe una matriz, un entero que representa una de sus columnas
    y un criterio de ordenamiento. Ordena según el criterio y retorna la cantidad
    de intercambios.
    '''

    flag = 1
    contador = 0
    
    while flag:
        flag = 0
        for i in range (len(matriz) - 1):
            if criterio == "a":
                if  matriz[i][columna] > matriz[i + 1][columna]:
                    aux = matriz[i]
                    matriz[i] = matriz[i + 1]
                    matriz[i + 1] = aux
                    flag = 1
                    contador += 1
            else:
                if  matriz[i][columna] < matriz[i + 1][columna]:
                    aux = matriz[i]
                    matriz[i] = matriz[i + 1]
                    matriz[i + 1] = aux
                    flag = 1
                    contador += 1
        
    return contador

matriz_1 = [
    ["Carlos", "Camps"],
    ["Pablo", "Ali"],
    ["Mirta", "García"]
]

matriz_2 = [
    ["Carlos", "Camps"],
    ["Pablo", "Ali"],
    ["Mirta", "García"]
]

print(ordenar_matrices_segun_columna_y_eleccion(matriz_1, 1, "a"))
mostrar_matriz(matriz_1)
print(ordenar_matrices_segun_columna_y_eleccion(matriz_2, 1, "d"))
mostrar_matriz(matriz_2)

# 7

# Es exactamente la misma función que en el punto anterior, solo hay que cambiar la columna en el llamado (lo mismo que pasaba con la función de ordenar string)

# 8

print("-------------------------------------------------------------------------------------------")

def ordenar_matriz_ascendente(matriz : list, columna : int) -> list:
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

def ordenar_matriz_descendente(matriz : list, columna : int) -> list:
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
            if  matriz_ordenada[i][columna] < matriz_ordenada[i + 1][columna]:
                aux = matriz_ordenada[i]
                matriz_ordenada[i] = matriz_ordenada[i + 1]
                matriz_ordenada[i + 1] = aux
                flag = 1

    return matriz_ordenada

def mostrar_matriz(matriz : list) -> None:
    '''
    Función que imprime por pantalla la matriz recibida por parámetro
    '''

    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def mostrar_5(matriz : list) -> None:
    '''
    Función que imprime por pantalla los primeros 5 elementos de la matriz.
    '''

    for fil in range(5):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def mostrar_3(matriz : list) -> None:
    '''
    Función que imprime por pantalla los primeros 3 elementos de la matriz.
    '''

    for fil in range(3):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")


tabla = [
    ["Pablo", "Ali", 57, 3, 12],
    ["Carlos", "Camps", 52, 9, 4],
    ["Julian", "Escudero", 68, 2, 4],
    ["Guillermo", "Gallegos", 61, 27, 10],
    ["Santiago", "Esquivel", 40, 1, 2],
    ["Fernando", "González", 7, 3, 2]
]

goleadores = ordenar_matriz_descendente(tabla, 3)
mostrar_matriz(goleadores)
print("------")
asistidores = ordenar_matriz_descendente(tabla, 4)
mostrar_matriz(asistidores)
print("------")
mas_partidos = ordenar_matriz_descendente(tabla, 2)
mostrar_5(mas_partidos)
print("------")
mostrar_3(goleadores)
print("------")
mesnos_asistencias = ordenar_matriz_ascendente(tabla, 4)
mostrar_3(mesnos_asistencias)
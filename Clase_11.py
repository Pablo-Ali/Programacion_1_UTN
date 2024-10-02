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


# -----------------------------------------------------------------------

print("\nUsando la función que crea copia")

lista = [20, -5, 10, 8, 3, 100, -10, 25, 50, 80]

print(f"Lista original {lista}")

lista_ordenada = ordenar_arreglo_burbuja_con_copia(lista)
print("Ordenando")
print(f"Lista original {lista}")
print(f"Copia ordenada {lista_ordenada}")

#----------------------------------------------------------------------------

print("\nUsando la función que altera el original")

lista_2 = [20, -5, 10, 8, 3, 100, -10, 25, 50, 80]

print(f"Lista original {lista_2}")

ordenar_arreglo_burbuja(lista_2)
print("Ordenando")
print(f"Lista original {lista_2}")


#----------------------------------------------------------------------------

print("\nProbando a ordenar una matriz")

mat = [
    ["BBB", 3, "Era el 1"],
    ["CCC", 2, "Era el 2"],
    ["DDD", 4, "Era el 3"],
    ["AAA", 1, "Era el 4"]
]

print(mat)

ordenar_matrices_segun_columna(mat, 0)

print("Orden según indice 0")
print(mat)

ordenar_matrices_segun_columna(mat, 1)

print("Orden según indice 1")
print(mat)
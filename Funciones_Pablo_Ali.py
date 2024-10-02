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

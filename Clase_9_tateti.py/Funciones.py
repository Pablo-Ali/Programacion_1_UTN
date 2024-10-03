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


def lanzar_moneda():
    return random.randint(1, 2)

def pedir_cara():
    moneda = ""
    while moneda != "cara" and moneda != "cruz":
        moneda = input("Elija cara o cruz: ")

    return lanzar_moneda()

def elegir_jugador(matriz):
    
    valido = False

    while valido == False:
    
        opcion = 0
        
        while opcion < 1 or opcion > 10:
            print("1 | 2 | 3")
            print("4 | 5 | 6")
            print("7 | 8 | 9")
            opcion = int(input("¿En qué posición desea colocar la X (1-9)?: "))

        valido = verificar_disponibilidad(matriz, opcion)

        if valido:
            return opcion

def elegir_maquina(matriz):
    valido = False

    while valido == False:
        opcion = random.randint(1, 9)
        valido = verificar_disponibilidad(matriz, opcion)
        if valido:
            return opcion


def verificar_disponibilidad(matriz, opcion):
    match opcion:
        case 1:
            if matriz[0][0] == 0:
                return True
            else:
                return False
        case 2:
            if matriz[0][1] == 0:
                return True
            else:
                return False
        case 3:
            if matriz[0][2] == 0:
                return True
            else:
                return False
        case 4:
            if matriz[1][0] == 0:
                return True
            else:
                return False
        case 5:
            if matriz[1][1] == 0:
                return True
            else:
                return False
        case 6:
            if matriz[1][2] == 0:
                return True
            else:
                return False
        case 7:
            if matriz[2][0] == 0:
                return True
            else:
                return False
        case 8:
            if matriz[2][1] == 0:
                return True
            else:
                return False
        case 9:
            if matriz[2][2] == 0:
                return True
            else:
                return False
            
def cargar_posición_jugador(matriz, opcion):
     match opcion:
        case 1:
            matriz[0][0] = "X"
        case 2:
            matriz[0][1] = "X"
        case 3:
            matriz[0][2] = "X"
        case 4:
            matriz[1][0] = "X"
        case 5:
            matriz[1][1] = "X"
        case 6:
            matriz[1][2] = "X"
        case 7:
            matriz[2][0] = "X"
        case 8:
            matriz[2][1] = "X"
        case 9:
            matriz[2][2] = "X"

def cargar_posición_maquina(matriz, opcion):
    match opcion:
        case 1:
            matriz[0][0] = "O"
        case 2:
            matriz[0][1] = "O"
        case 3:
            matriz[0][2] = "O"
        case 4:
            matriz[1][0] = "O"
        case 5:
            matriz[1][1] = "O"
        case 6:
            matriz[1][2] = "O"
        case 7:
            matriz[2][0] = "O"
        case 8:
            matriz[2][1] = "O"
        case 9:
            matriz[2][2] = "O"

def verificar_ganador():
    pass
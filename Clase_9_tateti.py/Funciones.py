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


def lanzar_moneda() -> int:
    '''
    Función que retorna un número random entre 1 y 2
    '''
    return random.randint(1, 2)

def pedir_cara() -> int:
    '''
    Función que solicita al usuario elegir entre 'cara' o 'cruz',
    Retorna el llamado a la función lanzar_moneda().
    '''

    moneda = ""
    while moneda != "cara" and moneda != "cruz":
        moneda = input("Elija cara o cruz: ")

    return lanzar_moneda()

def elegir_jugador(matriz : list) -> int:
    '''
    Función que recibe una matriz y solicita al jugador elegir un número entre 1 y 9.
    Llama a la función verificar_disponibilidad(matriz, opcion) para
    evaluar si la elección es viable.
    Retorna el número elegido.
    '''
    
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

def elegir_maquina(matriz : list) -> int:
    '''
    Función que recibe una matriz y genera un número random entre 1 y 9.
    Compara la disponibilidad del número con el llamado de
    verificar_disponibilidad(matriz, opcion). En caso de estar disponible
    lo retorna.
    '''
    
    valido = False

    while valido == False:
        opcion = random.randint(1, 9)
        valido = verificar_disponibilidad(matriz, opcion)
        if valido:
            return opcion


def verificar_disponibilidad(matriz : list, opcion : int) -> bool:
    '''
    Función que recibe una matriz y un número.
    Compara el número con una posición de la matriz.
    Si esta posee un '0' (está disponible para la carga),
    retorna True. Si ya está cargada con 'X' u 'O', retorna
    False.
    '''

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
            
def cargar_posición(matriz : list, opcion : int, ficha : str) -> None:
     '''
     Función que recibe una matriz, un número y una ficha.
     Carga el contenido de la ficha en la posición elegida.
     '''

     match opcion:
        case 1:
            matriz[0][0] = ficha
        case 2:
            matriz[0][1] = ficha
        case 3:
            matriz[0][2] = ficha
        case 4:
            matriz[1][0] = ficha
        case 5:
            matriz[1][1] = ficha
        case 6:
            matriz[1][2] = ficha
        case 7:
            matriz[2][0] = ficha
        case 8:
            matriz[2][1] = ficha
        case 9:
            matriz[2][2] = ficha


def verificar_ganador(matriz : list, ficha : str) -> bool:
    '''
    Función que recibe una matriz y una ficha.
    Si hay tres fichas iguales en línea (según reglas del TaTeTi),
    retorna True. Caso contrario, False.
    '''

    if matriz[0][0] == ficha and matriz[0][1] == ficha and matriz[0][2] == ficha:
        return True
    elif matriz[1][0] == ficha and matriz[1][1] == ficha and matriz[1][2] == ficha:
        return True
    elif matriz[2][0] == ficha and matriz[2][1] == ficha and matriz[2][2] == ficha:
        return True
    elif matriz[0][0] == ficha and matriz[1][0] == ficha and matriz[2][0] == ficha:
        return True
    elif matriz[0][1] == ficha and matriz[1][1] == ficha and matriz[2][1] == ficha:
        return True
    elif matriz[0][2] == ficha and matriz[1][2] == ficha and matriz[2][2] == ficha:
        return True
    elif matriz[0][0] == ficha and matriz[1][1] == ficha and matriz[2][2] == ficha:
        return True
    elif matriz[0][2] == ficha and matriz[1][1] == ficha and matriz[2][0] == ficha:
        return True
    else:
        return False
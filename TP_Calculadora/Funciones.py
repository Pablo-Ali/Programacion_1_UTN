# Ali, Pablo Sharif
# Comisión 313

def suma (num1 : int, num2 : int) -> int:
    '''
    Retorna el resultado de la suma de los números ingresados como parámetros
    '''
    return num1 + num2

def resta (num1 : int, num2 : int) -> int:
    '''
    Retorna el resultado de la resta de los números ingresados como parámetros
    '''
    return num1 - num2

def multiplicacion (num1 : int, num2 : int) -> int:
    '''
    Retorna el resultado de la multiplicación de los números ingresados como parámetros
    '''
    return num1 * num2

def division (num1 : int, num2 : int) -> float:
    '''
    Retorna el resultado de la división de los números ingresados como parámetros
    '''
    return num1 / num2

def potencia (num1 : int, num2 : int) -> int:
    '''
    Retorna el resultado de la potencia del primer parámetro elevado al segundo parámetro (que debe ser un entero)
    '''
    resultado = 1

    for i in range (num2):
        resultado *= num1

    return resultado

def resto (num1 : int, num2 : int) -> int:
    '''
    Retorna el resto de la división de los números ingresados como parámetros
    '''
    return num1 % num2

def factorial (num : int) -> int:
    '''
    Retorna el factorial del numero ingresado
    '''
    resultado = 1

    for i in range (1, num + 1):
        resultado *= i

    return resultado

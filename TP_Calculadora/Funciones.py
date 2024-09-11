# Ali, Pablo Sharif
# Comisión 313

def calcular_suma (num1 : int, num2 : int) -> int:
    '''
    Retorna el resultado de la suma de los números ingresados como parámetros
    '''
    return num1 + num2

def calcular_resta (num1 : int, num2 : int) -> int:
    '''
    Retorna el resultado de la resta de los números ingresados como parámetros
    '''
    return num1 - num2

def calcular_multiplicacion (num1 : int, num2 : int) -> int:
    '''
    Retorna el resultado de la multiplicación de los números ingresados como parámetros
    '''
    return num1 * num2

def calcular_division (num1 : int, num2 : int) -> float:
    '''
    Retorna el resultado de la división de los números ingresados como parámetros
    '''
    return num1 / num2

def calcular_potencia (num1 : int, num2 : int) -> int:
    '''
    Retorna el resultado de la potencia del primer parámetro elevado al segundo parámetro (que debe ser un entero)
    '''
    resultado = 1

    for i in range (num2):
        resultado *= num1

    return resultado

def calcular_resto (num1 : int, num2 : int) -> int:
    '''
    Retorna el resto de la división de los números ingresados como parámetros
    '''
    return num1 % num2

def calcular_factorial (num : int) -> int:
    '''
    Retorna el factorial del numero ingresado usando iteración
    '''
    resultado = 1

    for i in range (1, num + 1):
        resultado *= i

    return resultado

def calcular_factorial_recursivo (num : int) -> int:
    '''
    Retorna el factorial del numero ingresado usando recurividad
    '''
    if num > 1:
        resultado = num * calcular_factorial_recursivo(num - 1)
    else:
        resultado = 1
    
    return resultado


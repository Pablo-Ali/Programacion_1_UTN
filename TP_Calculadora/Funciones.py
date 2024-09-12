# Ali, Pablo Sharif
# Comisión 313

def calcular_suma (numero_1 : int, numero_2 : int) -> int:
    '''
    Retorna el resultado de la suma de los números ingresados como parámetros
    '''
    return numero_1 + numero_2

def calcular_resta (numero_1 : int, numero_2 : int) -> int:
    '''
    Retorna el resultado de la resta de los números ingresados como parámetros
    '''
    return numero_1 - numero_2

def calcular_multiplicacion (numero_1 : int, numero_2 : int) -> int:
    '''
    Retorna el resultado de la multiplicación de los números ingresados como parámetros
    '''
    return numero_1 * numero_2

def calcular_division (numero_1 : int, numero_2 : int) -> float | str:
    '''
    Retorna el resultado de la división de los números ingresados como parámetros
    '''
    if numero_2 != 0:
        return numero_1 / numero_2
    else:
        return "No se puede dividir por cero"

def calcular_potencia (numero_1 : int, numero_2 : int) -> int:
    '''
    Retorna el resultado de la potencia del primer parámetro elevado al segundo parámetro (que debe ser un entero)
    '''
    resultado = 1

    for i in range (numero_2):
        resultado *= numero_1

    return resultado

def calcular_resto (numero_1 : int, numero_2 : int) -> int | str:
    '''
    Retorna el resto de la división de los números ingresados como parámetros
    '''
    if numero_2 != 0:
        return numero_1 % numero_2
    else:
        return "No se puede dividir por cero"
    
def calcular_factorial (numero : int) -> int:
    '''
    Retorna el factorial del numero ingresado usando iteración
    '''
    resultado = 1

    for i in range (1, numero + 1):
        resultado *= i

    return resultado

def calcular_factorial_recursivo (numero : int) -> int:
    '''
    Retorna el factorial del numero ingresado usando recurividad
    '''
    if numero > 1:
        resultado = numero * calcular_factorial_recursivo(numero - 1)
    else:
        resultado = 1
    
    return resultado


# Ali, Pablo Sharif
# Comisión 313

# 1

def suma1 (num1 : float, num2 : float) -> float:
    '''
    Retorna el resultado de la suma de los números ingresados como parámetros
    '''
    return num1 + num2

print(f"El resultado es: {suma1(3, 5.5)}")

# 2

def suma2 (num1 : float, num2 : float) -> float:
    '''
    Imprime el resultado de la suma de los números ingresados como parámetros
    '''
    print(f"El resultado es: {num1 + num2}")

suma2(4, 6.6)

# 3

def suma3 () -> float:
    '''
    Solicita al usuario dos números y retorna el resultado de su suma.
    '''
    suma = 0
    for i in range (2):
        num = float(input("Ingrese un número: "))
        suma += num
    return suma

print(f"El resultado es: {suma3()}")

# 4

def suma4 ():
    '''
    Solicita al usuario dos números e imprime el resultado de su suma.
    '''
    resultado = 0
    for i in range (2):
        num = float(input("Ingrese un número: "))
        resultado += num
    print(f"El resultado es: {resultado}")

suma4()
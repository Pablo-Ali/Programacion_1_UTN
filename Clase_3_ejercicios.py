# Ali, Pablo Sharif
# Comisión 313

# 1

def calcular_promedio (acumulador : float, contador : int) -> float:
    '''
    Función que recibe un acumulador y un contador. Divide el acumulador por el contador
    para obtener y retornar el promedio. 
    '''
    if contador == 0:
        print("Error: No se puede dividir por cero")
        return 0
    else:
        return acumulador / contador
    
resultado = calcular_promedio(5, 3)

if resultado != 0:
    print(f"El resultado es: {resultado}")

# 2

def calcular_area_rectangulo(base : float, altura : float) -> float:
    '''
    Calcula el área de un rectángulo a partir de la base y la altura ingresadas por parámetro.
    Retorna el resultado.
    '''
    resultado = base * altura
    return resultado

area = calcular_area_rectangulo(20, 15)
print(f"El área del rectángulo es de: {area}")

# 3

def es_par(num : int) -> bool:
    '''
    La función verifica si el numero ingresado por parámetro es par o no.
    Retorna True en caso de ser par, False en caso de no serlo.
    '''
    if num % 2 == 0:
        return True
    else:
        return False
    
print(f"El número ingresado, ¿es par?: {es_par(15)}")

# 4

def es_primo(num : int) -> bool:
    '''
    La función verifica si el numero ingresado por parámetro es primo o no.
    Retorna True en caso de ser par, False en caso de no serlo.
    '''
    es_primo = True

    for i in range(2, num, 1):
        if num % i == 0:
            es_primo = False
            break

    if es_primo and num > 1:
        return True
    else:
        return False
    
print(f"El número ingresado, ¿es primo?: {es_primo(73)}")

# 5

def hallar_num_max() -> float:
    '''
    La función solicita al usuario ingresar tres números y luego retorna el mayor.
    '''
    num_max = 0
    
    for i in range (3):
        num = float(input("Ingrese un numero: "))
        if i == 0:
            num_max = num
        elif num > num_max:
            num_max = num
    
    return num_max

num_mayor = hallar_num_max()
print(num_mayor)

# 6

def hallar_num_min() -> float:
    '''
    La función solicita al usuario ingresar tres números y luego retorna el menor.
    '''
    num_min = 0
    
    for i in range (3):
        num = float(input("Ingrese un numero: "))
        if i == 0:
            num_min = num
        elif num < num_min:
            num_min = num
    
    return num_min

num_menor = hallar_num_min()
print(num_menor)

# 7

def multiplicar(num1 : float, num2: float) -> float:
    '''
    Retorna el resultado de multiplicar los números pasador por parámetro
    '''
    res = num1 * num2
    return res

print(f"El resutltado de la multiplicación es: {multiplicar(20, 35)}")
# Ali, Pablo Sharif
# Comisión 313

# Recursividad

# 1
def sumar_naturales(num : int) -> int:
    '''
    Retorna la suma de los números naturales anteriores al ingresado
    '''
    if num > 1:
        resultado = num + sumar_naturales(num - 1)
    else:
        resultado = 1
    
    return resultado

print(sumar_naturales(5))

# 2
def calcular_potencia(base:int , exponente:int) -> int:
    '''
    Retorna la potencia de un número ingresado elevado al segundo parámetro
    '''
    if exponente > 1:
        resultado = base * calcular_potencia(base, exponente - 1)
    else:
        resultado = base
    
    return resultado

print(calcular_potencia(3, 5))

# 3
# Salió de casualidad, por probar cosas, no termino de entender por qué funciona
def calcular_fibonacci(num:int) -> int:
    '''
    Retorna la posición de la secuencia de Fibonacci según el número ingresado
    '''
    if num > 1:
        resultado = calcular_fibonacci(num - 1) + calcular_fibonacci(num - 2)
        
    else:
        resultado = 1
    return resultado

print(calcular_fibonacci(7))


# Corroboración punto 3

# a = 0
# b = 1

# for i in range (7):
#     r = a + b
#     a = b
#     b = r
#     print(r)

# Funciones (Avanzado)

# 1
def verificar_dni(dni : str) -> bool:
    caracteres = len(dni)

    if caracteres < 6 or caracteres > 8:
        return False
    else:
        return True

print(verificar_dni("12345"))
print(verificar_dni("1234567"))
print(verificar_dni("123456789"))

# 2
# Solución efectiva, pero poco elegante. Mejorar los retornos para que pueda ser reutilizable en caso de querer admitir cadenas más largas o cortas
def rellenar_dni(dni : str, booleano : bool) -> str:
    if booleano == False:
        return "DNI inválido"
    else:
        caracteres = len(dni)
        if caracteres == 6:
            return f"00{dni}"
        elif caracteres == 7:
            return f"0{dni}"
        else:
            return dni
        
print(rellenar_dni("12345", verificar_dni("12345")))
print(rellenar_dni("123456", verificar_dni("123456")))
print(rellenar_dni("1234567", verificar_dni("1234567")))
print(rellenar_dni("12345678", verificar_dni("12345678")))
print(rellenar_dni("123456789", verificar_dni("123456789")))
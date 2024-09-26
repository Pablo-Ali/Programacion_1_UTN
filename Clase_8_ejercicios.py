# Ali, Pablo Sharif
# Comisión 313

# 1

def contar_str_con_mas_5_char(lista_str : list) -> int:
    '''
    Función que toma una lista de strings y 
    retorna la cantidad de cadenas con más de 5 caracteres
    '''

    contador = 0

    for char in lista_str:
        if len(char) > 5:
            contador += 1
    
    return contador

print(contar_str_con_mas_5_char(["hola", "pentágono", "amarillo", "2", "Pablo"]))

# 2

def retornar_str_con_mas_5_char(lista_str : list) -> list:
    '''
    Función que toma una lista de strings y retorna una nueva 
    lista con los strings que poseen más de 5 caracteres
    '''

    lista_aux = []

    for char in lista_str:
        if len(char) > 5:
            lista_aux.append(char)
    
    return lista_aux

print(retornar_str_con_mas_5_char(["hola", "pentágono", "amarillo", "2", "Pablo"]))

# 3

def ingresar_string(rango : int) -> list:
    '''
    Función que toma un entero y solicita ingresar por 
    teclado esa cantidad de strings, que almacena en una 
    lista y la retorna.
    '''
    
    lista_string = []

    for i in range (rango):
        string = input("Ingrese el string: ")
        lista_string.append(string)
    
    return lista_string

def retornar_nombres_mas_cortos(lista_nombres : list) -> list:
    '''
    Función que recibe una lista de nombres y retorna otra lista 
    con los nombres más cortos
    '''

    min = 0
    lista_aux = []

    for i in range (len(lista_nombres) - 1):
        if i == 0:
            min = len(lista_nombres[0])
        if len(lista_nombres[i]) < min:
            min = len(lista_nombres[i])
        
    for nombre in lista_nombres:
        if len(nombre) == min:
            lista_aux.append(nombre)

    return(lista_aux)

lista_de_nombres = ingresar_string(5)
print(retornar_nombres_mas_cortos(lista_de_nombres))

# 4

def contar_apellidos_repetidos(lista_apellidos_comunes : list) -> None:
    '''
    Función que recibe una lista con apellidos comunes, pide que se ingresen otros 
    apellidos, los almacena en una nueva lista y compara las coincidencias. Imprime los 
    resultados de la comparación.
    '''

    lista_apellidos = ingresar_string(10)
    lista_aux = []



    for i in range (len(lista_apellidos_comunes) - 1):
        for j in range (10):
            if lista_apellidos_comunes[i] == lista_apellidos[j]:
                lista_aux.append(lista_apellidos[j])
    
    for i in range (len(lista_apellidos_comunes) - 1):
        contador  = 0
        for j in range (len(lista_aux) - 1):
            if lista_apellidos_comunes[i] == lista_aux[j]:
                contador += 1
        print(f"{lista_apellidos_comunes[i]} se repite {contador} veces")

contar_apellidos_repetidos(["López", "Gómez", "Fernández", "Pérez", "Martínez"])

# 5

def ingresar_numero(rango : int) -> list:
    '''
    Función que toma un entero y solicita ingresar por 
    teclado esa cantidad de numeros enteros, que almacena en una 
    lista y la retorna.
    '''
    
    lista_numero = []

    for i in range (rango):
        numero = int(input("Ingrese el numero: "))
        lista_numero.append(numero)
    
    return lista_numero



def imprimir_mayores_edad(lista_nombres : list, lista_edades : list) -> None:
    '''
    Función que recibe una lista de nombres y una lista con edades.
    Imprime los nombres de los mayores de edad. En caso de no 
    haberlos, lo notifica
    '''
    flag = True
    
    for i in range (len(lista_nombres)):
        if lista_edades[i] >= 18:
            print(f"{lista_nombres[i]} es mayor de edad")
            flag = False

    if flag:
     print("No hay mayores de edad")

l_nombres = ingresar_string(5)
l_edades = ingresar_numero(5)
imprimir_mayores_edad(l_nombres, l_edades)

# 6

def imprimir_productos_mayores_al_primero(lista_prod: list, lista_precio : list) -> None:
    '''
    Función que recibe una lista de productos y una lista con precios.
    Imprime aqueyos productos cuyo precio supera al primero; en caso de no 
    haberlos, avisa que no hay.
    '''
    precio_primer_prod = lista_precio[0]
    flag = True
    
    for i in range (len(lista_prod)):
        if lista_precio[i] > precio_primer_prod:
            print(lista_prod[i])
            flag = False
    
    if flag:
        print("El primer producto poseía el mayor precio")

l_productos = ingresar_string(5)
l_precios = ingresar_numero(5)
imprimir_productos_mayores_al_primero(l_productos, l_precios)

# 7
#Es más de lo mismo solo que con un par de validaciones más, y no tengo el tiempo como para ponerme a hacerlo en tiempo y fomra. Dudo de que esto sea leído,
#  pero, de ser así, pido disculpas. (Tendría que agregar validaciones de rango a la función que pide números, o crear una nueva para no interferir con la anterior 
# (si estuviesemos con POO, haría sobrecarga de métodos, acá no sé si se puede). Después ya es hacer la función que recorre las listas paralelas y verifica el promedio más alto. 
# Habría que agregarle una verificación para ver si es más de uno (se pueden meter en una lista auxiliar e imprimir todos juntos al final)). 
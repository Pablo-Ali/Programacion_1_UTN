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

def ingresar_nombres(rango : int) -> list:
    '''
    Función que permite ingresar por teclado 
    la cantidad de nombres solicitada por parámetro y retornarlos en una lista.
    '''
    
    lista_nombres = []

    for i in range (rango):
        nombre = input("Ingrese el nombre: ")
        lista_nombres.append(nombre)
    
    return lista_nombres

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

lista_de_nombres = ingresar_nombres(5)
print(retornar_nombres_mas_cortos(lista_de_nombres))

# 4

def contar_apellidos_repetidos(lista_apellidos_comunes : list):
    '''
    Función que recibe una lista con apellidos comunes, pide que se ingresen otros 
    apellidos, los almacena en una nueva lista y compara las coincidencias. Imprime los 
    resultados de la comparación.
    '''

    lista_apellidos = ingresar_nombres(10)
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

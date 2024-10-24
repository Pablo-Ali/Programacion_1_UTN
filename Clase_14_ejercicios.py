# Ali, Pablo Sharif
# Comisión 313

import random

# 1

def pasar_fecha_a_lista(fecha : str) -> list:
    '''
    Función que recibe una fecha en formato DDmmYYYY como
    cadena de caracteres y retorna una lista de enteros con sus
    números. Admite como separadores '-' y '/'.
    '''

    lista_retorno = []

    if fecha[2] == "-":
        lista_aux = fecha.split("-")
    else:
        lista_aux = fecha.split("/")

    for i in range(len(lista_aux)):
        lista_retorno.append(int(lista_aux[i]))
    
    return lista_retorno


fecha_1 = "24-10-2024"
fecha_2 = "55/55/5555"

print(pasar_fecha_a_lista(fecha_1))
print(pasar_fecha_a_lista(fecha_2))
print("--------------------------------------------------------")

# 2

def pasar_lista_a_fecha(lista : list, separador : str) -> str | None:
    '''
    Función que recibe una lista de 3 números enteros y un separador,
    si se cumplen las condiciones, retorna un string. En caso contrario,
    retorna None.
    '''

    lista_aux = []

    for i in range(len(lista)):
        lista_aux.append(str(lista[i]))

    if separador != "-" and separador != "/":
        return None
    elif len(lista) != 3:
        return None
    else:
        return separador.join(lista_aux)

print(pasar_lista_a_fecha([24,10,2024], "-"))
print(pasar_lista_a_fecha([24,10], "-"))
print(pasar_lista_a_fecha([24,10,2024], "#"))
print("--------------------------------------------------------")

# 3

# def reemplazar_vocales(cadena : str) -> str:
#     '''
#     Función que recibe una cadena de texto y reemplaza sus vocales
#     por letras aleatorias. Todo en minúsculas.
#     Retorna la nueva cadena.
#     '''

#     for i in range(len(cadena)):
#         letra = ord(cadena[i])
#         if letra == 97 or letra == 101 or letra == 105 or letra == 111 or letra == 117:
#             letra_aleatoria = random.randint(98,122)
#             cadena.replace(cadena[i], chr(letra_aleatoria))

#     return cadena
    
# print(reemplazar_vocales("hola mundo"))

# 4

def generar_num_legajo() -> int:
    '''
    Función que retorna un número de legajo de 6 dígitos generado 
    aleatoriamente entre 1 y 125000.
    '''

    return str(random.randint(1,125000)).zfill(6)

print(generar_num_legajo())
print("--------------------------------------------------------")

# 5


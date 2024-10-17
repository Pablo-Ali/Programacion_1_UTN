# Ali, Pablo Sharif
# Comisión 313

# 1

def es_alfabetico(cadena : str) -> bool:
    '''
    Función que recibe una cadena de caracteres,
    revisa que sólo posea caracteres alfabéticos.
    Retorna True si es así, False en caso contrario.
    '''

    resultado = True

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])
        if (c_ascii < 65) or (c_ascii > 90 and c_ascii < 97) or (c_ascii > 122):
            resultado = False

    return resultado

cadena_1 = "Pablo"
cadena_2 = "Pablo Ali"
print("---------------------------------------------")

print(es_alfabetico(cadena_1))
print(es_alfabetico(cadena_2))

# 2

def es_entero(cadena : str) -> bool:
    '''
    Función que recibe una cadena,
    revisa que sólo posea caracteres del 0 al 9.
    Retorna True si es así, False en caso contrario.
    '''

    resultado = True

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])
        if c_ascii < 48 or c_ascii > 57:
            resultado = False

    return resultado

cadena_3 = "356"
cadena_4 = "25.3"

print(es_entero(cadena_3))
print(es_entero(cadena_4))
print("---------------------------------------------")

# 3

def es_alfanumerico(cadena : str) -> bool:
    '''
    Función que recibe una cadena de caracteres,
    revisa que sólo posea caracteres alfanuméricos.
    Retorna True si es así, False en caso contrario.
    '''

    resultado = True

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])
        if (c_ascii < 48) or (c_ascii > 57 and c_ascii < 65) or (c_ascii > 90 and c_ascii < 97) or (c_ascii > 122):
            resultado = False

    return resultado

cadena_5 = "Pablo01"

print(es_alfanumerico(cadena_1))
print(es_alfanumerico(cadena_3))
print(es_alfanumerico(cadena_5))
print(es_alfanumerico(cadena_2))
print("---------------------------------------------")

# 4

def es_mayuscula(cadena : str) -> bool:
    '''
    Función que recibe una cadena,
    revisa que sólo posea caracteres en mayúscula.
    Retorna True si es así, False en caso contrario.
    '''

    resultado = True

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])
        if c_ascii < 65 or c_ascii > 90:
            resultado = False

    return resultado

cadena_6 = "PABLO"
cadena_7 = "pablo"

print(es_mayuscula(cadena_6))
print(es_mayuscula(cadena_7))
print("---------------------------------------------")

# 5

def es_minuscula(cadena : str) -> bool:
    '''
    Función que recibe una cadena,
    revisa que sólo posea caracteres en minúscula.
    Retorna True si es así, False en caso contrario.
    '''

    resultado = True

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])
        if c_ascii < 97 or c_ascii > 122:
            resultado = False

    return resultado

print(es_minuscula(cadena_6))
print(es_minuscula(cadena_7))
print("---------------------------------------------")

# 6

def convertir_caracter_mayuscula(cadena : str) -> str | None:
    '''
    Función que recibe un caracter.
    Si es posible, lo convierte a mayúscula.
    Si ya está en mayúscula o es otro tipo de caracter, lo retorna.
    Si hay más de un caracter, retorna None.
    '''

    if len(cadena) > 1:
        return None
    
    if ord(cadena) > 97 and ord(cadena) < 122:
        return chr(ord(cadena) - 32)
    else:
        return cadena
    
cadena_8 = "c"
cadena_9 = "7"

print(convertir_caracter_mayuscula(cadena_8))
print(convertir_caracter_mayuscula(cadena_9))
print(convertir_caracter_mayuscula(cadena_1))
print("---------------------------------------------")

# 7

# lo mismo que lo anteriror pero entre 65 y 90. Se le suma 32.

# 8

def convertir_cadena_mayuscula(cadena : str) -> str | None:
    '''
    Función que recibe una cadena de caractes.
    Convierte los alfabéticos a mayus y deja el resto como está.
    Retorna la nueva cadena.
    '''

    cadena_retorno = ""

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])
        if c_ascii >= 97 and c_ascii <= 122:
            aux = c_ascii - 32
            cadena_retorno += chr(aux)
        else:
            cadena_retorno += cadena[i]

    return cadena_retorno

print(convertir_cadena_mayuscula(cadena_2))
print(convertir_cadena_mayuscula(cadena_5))
print("---------------------------------------------")

# 9

# lo mismo que lo anteriror pero entre 65 y 90. Se le suma 32.

# 10

def capitalizar_texto(cadena : str) -> str:
    '''
    Función que convierte la primera letra de la cadena a mayúscula.
    Retorna la nueva cadena.
    '''

    cadena_retorno = ""

    for i in range(len(cadena)):
        if i == 0:
            c_ascii = ord(cadena[i])
            if c_ascii >= 97 and c_ascii <= 122:
                aux = c_ascii - 32
                cadena_retorno += chr(aux)
            else:
                cadena_retorno += cadena[i]
        else:
            cadena_retorno += cadena[i]

    return cadena_retorno

print(capitalizar_texto("Pablo01"))
print(capitalizar_texto("pablo01"))
print("---------------------------------------------")

# 11

def generar_titulo(cadena : str) -> str:
    '''
    Función que recibe una cadena de caracteres.
    Convierte las letras iniciales de cada palabra a mayúscula.
    Retorna la nueva cadena.
    '''

    cadena_retorno = ""

    for i in range(len(cadena)):
        c_ascii = ord(cadena[i])

        if i == 0:
            if c_ascii >= 97 and c_ascii <= 122:
                aux = c_ascii - 32
                cadena_retorno += chr(aux)
            else:
                cadena_retorno += cadena[i]
        else:
            if cadena[i - 1] == " ":
                if c_ascii >= 97 and c_ascii <= 122:
                    aux = c_ascii - 32
                    cadena_retorno += chr(aux)
                else:
                    cadena_retorno += cadena[i]
            else:
                if c_ascii >= 65 and c_ascii <= 90:
                    aux = c_ascii + 32
                    cadena_retorno += chr(aux)
                else:
                    cadena_retorno += cadena[i]
    
    return cadena_retorno

print(generar_titulo("pablo ali"))
print(generar_titulo("PABLO ALI"))
print(generar_titulo("12 HoLA mUndo"))
print("---------------------------------------------")

# 12

def formatear_nombre_apellido(cadena : str) -> str:
    '''
    Función que recibe una cadena cualquiera.
    Elimina todo aquello que no sean letras y
    le da formato de nombre y apellido.
    Retorna la nueva cadena.
    '''

    cadena_aux = ""
    cadena_retorno = ""

    for i in range(len(cadena)):
        caracter = es_alfabetico(cadena[i])

        if caracter:
            cadena_aux += cadena[i]
        elif cadena[i] == " ":
            cadena_aux += cadena[i]

    for i in range(len(cadena_aux)):
        if cadena_aux[i] != " ":
            cadena_retorno += cadena_aux[i]
        else:
            if i < len(cadena_aux) -1:
                cadena_retorno += cadena_aux[i]

    return generar_titulo(cadena_retorno)

print(formatear_nombre_apellido("123mAriAnO ferNanDEZ 911%@"))
print("---------------------------------------------")

# 13

def suprimir_repetidos_consecutivos(cadena : str) -> str:
    '''
    Función que recibe una cadena de caracteres.
    Elimina los caracteres repetidos consecutivos.
    Retorna la nueva cadena.
    '''

    cadena_retorno = ""

    for i in range(len(cadena) - 1):
        if cadena[i] != cadena[i + 1]:
            cadena_retorno += cadena[i]
        if i == len(cadena) - 2:
            cadena_retorno += cadena[i + 1]
    return cadena_retorno

print(suprimir_repetidos_consecutivos("Hooola"))
print(suprimir_repetidos_consecutivos("essstto  ees unnna     prruebaa"))
print("---------------------------------------------")

# 14

def suprimir_vocales(cadena : str) -> str:
    '''
    Función que recibe una cadena de caracteres.
    Elimina la vocales y retorna la nueva cadena.
    '''

    cadena_retorno = ""

    for caracter in cadena:
        if caracter != 'a' and caracter != 'e' and caracter != 'i' and caracter != 'o' and caracter != 'u' and caracter != 'A' and caracter != 'E' and caracter != 'I' and caracter != 'O' and caracter != 'U':
            cadena_retorno += caracter

    return cadena_retorno

print(suprimir_vocales("Hola"))
print("---------------------------------------------")

# 15

# def contar_subcadena(cadena : str, subcadena : str) -> int:
#     '''
#     Función que recibe una cadena y una subcadena de caracteres.
#     Cuenta la cantidad de veces que la subcadena está presente en la cadena.
#     Retona el resultado.
#     '''

#     pass

    

# print(contar_subcadena("El origen del gen"))    

# no se me ocurrió una solución
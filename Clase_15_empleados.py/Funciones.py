def mostrar_diccionario(diccionario) -> None:
    '''
    '''

    for clave,valor in diccionario.items():
        print(f"{clave.title().replace("-"," ")} : {valor}")

def mostrar_lista_diccionario(lista : list) -> bool:
    '''
    '''

    retorno = False

    for elemento in lista:
        mostrar_diccionario(elemento)
        print("")
        retorno = True
    
    return retorno


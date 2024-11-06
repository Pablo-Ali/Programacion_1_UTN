import os
import json


# Pasaje del archivo csv al sistema

def crear_diccionario_alumnos(lista_valores : list) -> dict:
    mi_alumno = {}
    mi_alumno['nombre'] = lista_valores[0]
    mi_alumno['apellido'] = lista_valores[1]
    mi_alumno['genero'] = lista_valores[2]
    mi_alumno['nota_final'] = int(lista_valores[3])

    return mi_alumno

def leer_csv_alumnos(nombre_archivo : str, lista_alumnos : list) -> bool:
    if os.path.exists(nombre_archivo):
        retorno = True

        with open(nombre_archivo, "r") as archivo:

            archivo.readline() # Falsa lectura -> lee la primera línea, la de la cabecera, para extraerla y que después no lo haga en el for

            for linea in archivo:
                linea_aux = linea.replace("\n", "") # elimino el \n del final
                lista_valores = linea_aux.split(",") # crea una lista separando los elementos por la coma
                mi_alumno = crear_diccionario_alumnos(lista_valores) # metemos los valores de la lista en un diccionario
                lista_alumnos.append(mi_alumno) # agregamos los diccionarios a la lista
    else:
        retorno = False

    return retorno

#hasta acá, debe ser modificado dependiendo del csv, lo que sigue sí ya es genérico

# Pasaje del sistema al archivo csv

def crear_cabecera(diccionario : dict, separador : str) -> str:
    lista_claves = list(diccionario.keys()) # generamos una lista con las claves del diccionario
    cabecera = separador.join(lista_claves) # creamos un string con los elementos de la lista separados por una coma (como debe ser una cabecera)
    return cabecera

def crear_dato_csv(diccionario : dict, separador : str) -> str:
    lista_valores = list(diccionario.values()) # generamos una lista con los valores del diccionario
    for i in range(len(lista_valores)): # convertimos todo a str para poder hacer join
        lista_valores[i] = str(lista_valores[i])
    linea = separador.join(lista_valores) # ecreamos las filas en formato csv

    return linea

def guardar_csv(nombre_archivo : str, lista : list) -> bool:

    if type(lista) == list and len(lista) > 0: # verificamos que sea una lista y que tenga algún elemento
        retorno = True

        cabecera = crear_cabecera(lista[0], ",")

        with open(nombre_archivo, "w") as archivo:
            
            archivo.write(cabecera + "\n") # escribimos la cabecera

            for i in range(len(lista)): # escribimos cada línea de datos
                linea = crear_dato_csv(lista[i], ",")
                if i != len(lista) -1:
                    archivo.write(linea + "\n")
                else:
                    archivo.write(linea) # si es la última línea, no agregamos el salto de línea al final
    else:
        retorno = False

    return retorno


# leer json

def leer_json(nombre_archivo : str) -> list:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            lista = json.load(archivo) # lee el archivo json
        return lista
    else:
        return [] # si el archivo no existe, retorna una lista vacía para que no rompa el programa


# generar json

def generar_json(nombre_archivo : str, lista : list) -> bool:

    if type(lista) == list and len(lista) > 0: # verificamos que sea una lista y que tenga algún elemento
        retorno = True
        with open(nombre_archivo, "w") as archivo:
            json.dump(lista,archivo,indent=4) # escribimos el archivo json con los datos de la lista
    else:
        retorno = False

    return retorno
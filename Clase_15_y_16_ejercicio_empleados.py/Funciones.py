import copy

def imprimir_lista(lista : list) -> None:
    '''
    '''

    for elemento in lista:
        print(elemento)

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

def mostrar_lista_diccionario_hasta_5(lista : list) -> bool:
    '''
    '''

    retorno = False
    contador = 0

    for elemento in lista:
        contador += 1
        if contador > 5:
            break
        mostrar_diccionario(elemento)
        print("")
        retorno = True
    
    return retorno

def cargar_empleados(lista_empleados:list) -> bool:
    '''
    '''
    
    dni = ingresar_DNI()
    apellido = ingresar_apellido()
    nombre = ingresar_nombre()
    edad = ingresar_edad()
    antiguedad = ingresar_antiguedad()
    rol = ingresar_rol()
    sueldo = ingresar_sueldo()
    
    diccionario = {"dni":dni,"apellido":apellido,"nombre":nombre,"edad":edad,"rol":rol,"años-de-antiguedad":antiguedad,"sueldo-mensual-en-pesos":sueldo}
    print("\n-----------------------------------")
    print("Datos a cargar:\n")
    mostrar_diccionario(diccionario)
    print("-----------------------------------")
    
    print("¿Desea guardar los datos?\n1 - Sí\n2 - No")
    opcion = pedir_opcion(1, 2)

    match opcion:
        case 1:
            lista_empleados.append(diccionario)
            retorno = True
        case 2:
            retorno = False
        
    return retorno

def pedir_opcion(min : int, max : int) -> int:
    '''
    Función que recibe por parámetro un mínimo y un máximo y 
    se encarga de validar que el número ingresado se encuentre dentro de ese rango.
    Retorna el número.
    '''
    num = int(input("Ingrese la opción: "))

    while num < min or num > max:
        print(f"Las opciones son del {min} al {max}")
        num = int(input("Ingrese la opción: "))

    return num

def ingresar_DNI() -> str:
    '''
    Función que se encarga de pedir un DNI por teclado 
    y verifica que este tenga siete u ocho dígitos.
    En caso de tener siete, agrega un cero al comienzo.
    Finalmente, retorna el DNI como String para conservar
    el cero del comienzo.
    '''

    dni = input("Ingrese el DNI: ")

    while len(dni) < 7 or len(dni) > 8:
        print("El DNI debe terner siete u ocho dígitos.")
        dni = input("Ingrese el DNI: ")

    return dni.zfill(8)

def ingresar_nombre() -> str:
    '''
    Función que se encarga de pedir un nombre por teclado 
    y verifica que este tenga tres caracteres como mínimo como mínimo y 
    que solo sean alfabéticos.
    Finalmente, retorna el nombre.
    '''

    nombre = input("Ingrese el nombre: ")

    while len(nombre) < 3 or nombre.isalpha() == False:
        print("El nombre debe terner al menos tres caracteres y ser solo alfabéticos.")
        nombre = input("Ingrese el nombre: ")

    return nombre

def ingresar_apellido() -> str:
    '''
    Función que se encarga de pedir un apellido por teclado 
    y verifica que este tenga tres caracteres como mínimo y que
    solo sean alfabéticos.
    Finalmente, retorna el apellido.
    '''

    apellido = input("Ingrese el apellido: ")

    while len(apellido) < 3 or apellido.isalpha() == False:
        print("El apellido debe terner al menos tres caracteres y ser solo alfabéticos.")
        apellido = input("Ingrese el apellido: ")

    return apellido

def ingresar_edad() -> int:
    '''
    '''

    edad = int(input("Ingrese la edad: "))

    while edad < 18 or edad > 65:
        print("La edad debe estar entre 18 y 65 años")
        edad = int(input("Ingrese la edad: "))

    return edad

def ingresar_antiguedad() -> int:
    '''
    '''

    antiguedad = int(input("Ingrese los años de antigüedad: "))

    while antiguedad < 1:
        print("Debe contar con al menos un año de antigüedad")
        antiguedad = int(input("Ingrese los años de antigüedad: "))

    return antiguedad

def ingresar_rol() -> str:
    '''
    '''

    print("Roles:\n1 - Administrativo\n2 - Gerencia\n3 - Atención al cliente\n4 - Limpieza")
    opcion = pedir_opcion(1, 4)
    
    match opcion:
        case 1:
            retorno = "Administrativo"
        case 2:
            retorno = "Gerencia"
        case 3:
            retorno = "Atención al cliente"
        case 4:
            retorno = "Limpieza"
    
    return retorno

def ingresar_sueldo() -> int:
    '''
    '''

    sueldo = int(input("Ingrese el sueldo: "))

    while sueldo < 600000 or sueldo > 30000000:
        print("El sueldo debe estar entre 600.000 y 30.000.000 de pesos")
        sueldo = int(input("Ingrese el sueldo: "))

    return sueldo

def ordenar_por_sueldo(lista_empleados : list[dict]) -> list[dict]:
    '''
    '''

    lista_retorno = copy.deepcopy(lista_empleados)

    lista_retorno.sort(key=lambda x: x['sueldo-mensual-en-pesos'], reverse=True)

    return lista_retorno

def ordenar_por_edad(lista_empleados : list[dict]) -> list[dict]:
    '''
    '''

    lista_retorno = copy.deepcopy(lista_empleados)

    lista_retorno.sort(key=lambda x: x['edad'], reverse=True)

    return lista_retorno

def ordenar_por_antiguedad(lista_empleados : list[dict]) -> list[dict]:
    '''
    '''

    lista_retorno = copy.deepcopy(lista_empleados)

    lista_retorno.sort(key=lambda x: x['"años-de-antiguedad"'], reverse=True)

    return lista_retorno

def ordenar_apellidos_unicos(lista_empleados : list[dict]) -> list:
    '''
    '''

    set_apellidos = set()

    for empleado in lista_empleados:
        apellido = empleado['apellido']
        set_apellidos.add(apellido)

    lista_retorno = list(set_apellidos)

    lista_retorno.sort()
    
    return lista_retorno
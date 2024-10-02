def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any = None) -> list:
    '''
    Función que se engarga de inicializar una matriz según la cantidad 
    de filas y columnas pasadas por parámetro. Por defecto se inicializa con None en cada 
    campo, pero puede modificarse por cualquier valor en el tercer parámetro.
    Retorna la matriz.
    '''
    
    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz : list) -> None:
    '''
    Función que imprime por pantalla la matriz recibida por parámetro
    '''
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def cargar_matriz() -> list:
    '''
    Función que retorna una matriz cargada con los datos de diez alumnos.
    '''
    matriz = inicializar_matriz(1, 5)
    
    for i in range (len(matriz)):
        matriz[i][0] = ingresar_nombre()
        matriz[i][1] = ingresar_apellido()
        matriz[i][2] = ingresar_DNI()
        matriz[i][3] = ingresar_genero()
        matriz[i][4] = ingresar_nota_final()
    
    return matriz


def ingresar_nombre() -> str:
    '''
    Función que se encarga de pedir un nombre por teclado 
    y verifica que este tenga tres caracteres como mínimo.
    Finalmente, retorna el nombre.
    '''

    nombre = input("Ingrese el nombre: ")

    while len(nombre) < 3:
        print("El nombre debe terner al menos tres caracteres.")
        nombre = input("Ingrese el nombre: ")

    return nombre

def ingresar_apellido() -> str:
    '''
    Función que se encarga de pedir un apellido por teclado 
    y verifica que este tenga tres caracteres como mínimo.
    Finalmente, retorna el apellido.
    '''

    apellido = input("Ingrese el apellido: ")

    while len(apellido) < 3:
        print("El apellido debe terner al menos tres caracteres.")
        apellido = input("Ingrese el apellido: ")

    return apellido

def ingresar_DNI() -> int:
    '''
    Función que se encarga de pedir un DNI por teclado 
    y verifica que este tenga seis y ocho dígitos.
    Finalmente, retorna el DNI.
    '''

    dni = input("Ingrese el DNI: ")

    while len(dni) < 6 or len(dni) > 8:
        print("El DNI debe terner entre seis y ocho dígitos.")
        dni = input("Ingrese el DNI: ")

    return int(dni)

def ingresar_genero() -> str:
    '''
    Función que se encarga de pedir y retornar el género.
    Admite masculino, femenino y no binario.
    '''

    genero = input("Ingrese el género (M / F / NB): ").upper()

    while genero != "M" and genero != "F" and genero != "NB":
        print("Debe ingresar 'M' para masculino, 'F' para femenino o 'NB' para no binario")
        genero = input("Ingrese el género (M / F / NB): ")

    return genero


def ingresar_nota_final() -> int:
    '''
    Función que se encarga de pedir una nota por teclado 
    y verifica que esta sesté entre uno y diez.
    Finalmente, retorna la nota.
    '''

    nota = int(input("Ingrese la nota: "))

    while nota < 1 or nota > 10:
        print("La nota final debe ser del 1 al 10.")
        nota = int(input("Ingrese la nota: "))

    return nota

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

def buscar_promocionados (matriz : list, columna : int) -> list | int:
    '''
    Funcion que recibe una matriz y un número de columna.
    Crea y retorna una nueva matriz con los alumnos cuya nota sea 
    superior a 6. 
    En caso de no haber, retorna -1.
    '''
    alumnos_promocionados = []
    flag = False

    for i in range (len(matriz)):
        if matriz[i][columna] >= 6:
            alumnos_promocionados.append(matriz[i])
            flag = True
    
    if flag:
        return alumnos_promocionados
    else:
        return -1

def buscar_regularizados (matriz : list, columna : int) -> list | int:
    '''
    Funcion que recibe una matriz y un número de columna.
    Crea y retorna una nueva matriz con los alumnos cuya nota sea 
    4 o 5. 
    En caso de no haber, retorna -1.
    '''
    alumnos_regularizados = []
    flag = False

    for i in range (len(matriz)):
        if matriz[i][columna] == 4 or matriz[i][columna] == 5:
            alumnos_regularizados.append(matriz[i])
            flag = True
    
    if flag:
        return alumnos_regularizados
    else:
        return -1
    
def buscar_desaprobados (matriz : list, columna : int) -> list | int:
    '''
    Funcion que recibe una matriz y un número de columna.
    Crea y retorna una nueva matriz con los alumnos cuya nota sea 
    menor a 4. 
    En caso de no haber, retorna -1.
    '''
    alumnos_desaprobados = []
    flag = False

    for i in range (len(matriz)):
        if matriz[i][columna] < 4:
            alumnos_desaprobados.append(matriz[i])
            flag = True
    
    if flag:
        return alumnos_desaprobados
    else:
        return -1
    
def buscar_por_DNI(matriz : list, columna : int) -> None:
    '''
    Función que recibe por parámetro una matriz y una columna.
    Pide al usuario un número de DNI y lo compara con la matriz. 
    Si se encuentra, imprime todos los datos, si no, lo informa.
    '''

    dni = ingresar_DNI()
    flag = True

    for i in range (len(matriz)):
        if dni == matriz[i][columna]:
            print(f"Nombre: {matriz[i][0]}")
            print(f"Apellido: {matriz[i][1]}")
            print(f"DNI: {matriz[i][2]}")
            print(f"Género: {matriz[i][3]}")
            print(f"Nota final: {matriz[i][4]}")
            flag = False
    
    if flag:
        print(f"No se encuentra un alumno con el DNI {dni}")

def imprimir_cantidades(matriz : list, columna : int) -> None:
    promocionados = buscar_promocionados(matriz, columna)
    regularizados = buscar_regularizados(matriz, columna)
    desaprobados = buscar_desaprobados(matriz, columna)

    if promocionados == -1:
        print("Promocionados: No hay alumnos promocionados")
    else:
        print(f"Promocionados: {len(promocionados)}")
    if regularizados == -1:
        print("Regularizados: No hay alumnos regularizados")
    else:
        print(f"Regularizados: {len(regularizados)}")
    if desaprobados == -1:
        print("Desaprobados: No hay alumnos desaprobados")
    else:
        print(f"Desaprobados: {len(desaprobados)}")
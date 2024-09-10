# Ali, Pablo Sharif
# Comisión 313

mayor_precio_barbijo = 0
fabricante_barbijo = ""
unidades_barbijo = 0
mas_unidades = 0
fabricante_unidades = ""
total_jabones = 0

for i in range (1):
    while(True):
        tipo = input("Ingrese el tipo (barbijo, jabon o alcohol): ").lower()
        if tipo == "barbijo" or tipo == "jabon" or tipo == "alcohol":
            break
        else:
            print("Debe ingresar un tipo correcto")
    
    while(True):
        precio = float(input("Ingrese el precio (entre 100 y 300): "))
        if precio >= 100 and precio <= 300:
            break
        else:
            print("Ingrese un precio dentro del rango permitido")
    
    while(True):
        cantidad_unidades = int(input("Ingrese la cantidad de unidades (entre 1 y 1000): "))
        if cantidad_unidades > 0 and cantidad_unidades <= 1000:
            break
        else:
            print("Ingrese una cantidad de unidades correcta")
    
    marca = input("Ingrese la marca: ")
    fabricante = input("Ingrese el fabricante: ")

    if tipo == "jabon":
        total_jabones += cantidad_unidades
    elif tipo == "barbijo":
        if precio > mayor_precio_barbijo:
            mayor_precio_barbijo = precio
            fabricante_barbijo = fabricante
            unidades_barbijo = cantidad_unidades
    if cantidad_unidades > mas_unidades:
        mas_unidades = cantidad_unidades
        fabricante_unidades = fabricante

if unidades_barbijo == 0:
    print("No hay barbijos en stock")
else:
    print(f"Hay {unidades_barbijo} de los barbijo de {fabricante_barbijo}, que son los más caros")

print(f"{fabricante_unidades} es el fabricante del ítem con más unidades")

print(f"Hay {total_jabones} jabones en total")

# Ali, Pablo Sharif
# Comisión 313

# 1

for i in range(1, 11, 1):
    print(i)

# 2

for i in range(10, 0, -1):
    print(i)

# 3

num_1 = int(input("Ingresar número 1: "))
num_2 = int(input("Ingresar número 2: "))

if num_1 > num_2:
    for i in range(num_1, num_2 - 1, -1):
        print(i)
elif num_1 < num_2:
    for i in range(num_1, num_2 + 1, 1):
        print(i)
else:
    print(num_1)

# 4

suma = 0
contador = 0

for i in range(5):
    num = int(input("Ingrese un numero. Para salir, ingrese 0: "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"La suma de los números es: {suma}")
    print(f"El promedio es: {promedio}")
else:
    print("Solo se ingresó el nro 0")

# 5

for i in range (2, 101, 2):
    print(i)

# 6

num = int(input("Ingrese un número: "))
es_primo = True

for i in range(2, num, 1):
    if num % i == 0:
        es_primo = False
        break

if es_primo and num > 1:
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un número primo")

# 7

num = int(input("Ingrese un número: "))
contador_primos = 0

for i in range(1, num + 1, 1):
    primo = True
    if i == 1:
        continue
    for j in range (2, i, 1):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)
        contador_primos += 1
            
if contador_primos > 0:
    print(f"Hubo {contador_primos} números primos entre 1 y su número")
else:
    print("No encontramos números primos")

# 8

num = int(input("Ingrese un número: "))

for i in range (1, 11, 1):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

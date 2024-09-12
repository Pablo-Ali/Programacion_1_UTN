# Ali, Pablo Sharif
# Comisión 313

import Funciones

def menu():
    '''
    Menú que permite elegir las opciones para utilizar una calculadora que toma dos números, realiza varias operaciones y muestra los resultados.
    '''
    flag_n1 = False
    flag_n2 = False
    flag_operacion = False
    while(True):
        print("\nMENU CALCULADORA\n1.Ingresar primer operando\n2.Ingresar segundo operando\n3.Calcular todas las operaciones\n4.Informar resultados\n5.Salir\n")
        
        opcion = int(input("Ingrese su opcion: "))
        
        match opcion:
            case 1:
                n1 = int(input("Ingrese el primer número: "))
                flag_n1 = True
            case 2:
                n2 = int(input("Ingrese el segundo número: "))
                flag_n2 = True
            case 3:
                if flag_n1 and flag_n2:
                    r_suma = Funciones.calcular_suma(n1, n2)
                    r_resta = Funciones.calcular_resta(n1, n2)
                    r_mult = Funciones.calcular_multiplicacion(n1, n2)
                    r_pot = Funciones.calcular_potencia(n1, n2)
                    r_fac_1 = Funciones.calcular_factorial(n1) # con for
                    r_fac_2 = Funciones.calcular_factorial_recursivo(n2) # con recursividad
                    if n2 != 0:
                        r_div = Funciones.calcular_division(n1, n2)
                        r_mod = Funciones.calcular_resto(n1, n2)

                    print("Operaciones calculadas con éxito")
                    flag_operacion = True
                else:
                    print("Debe ingresar ambos números")
            case 4:
                if flag_operacion:
                    print(f"El resultado de la suma de {n1} + {n2} es: {r_suma}")
                    print(f"El resultado de la resta de {n1} - {n2} es: {r_resta}")
                    if n2 == 0:
                        print("Error: no se puede dividir por cero")
                    else:
                        print(f"El resultado de la división de {n1} / {n2} es: {r_div}")
                    print(f"El resultado de la multiplicación de {n1} * {n2} es: {r_mult}")
                    print(f"El resultado de la potencia de {n1} elevado a {n2} es: {r_pot}")
                    if n2 == 0:
                        print("Error: no se puede dividir por cero")
                    else:
                        print(f"El resto de la división de {n1} / {n2} es: {r_mod}")
                    print(f"El factorial de {n1} es: {r_fac_1}")
                    print(f"El factorial de {n2} es: {r_fac_2}")
                else:
                    print("Primero debe realizar las operaciones para ver sus resultados")
            case 5:
                print("Hasta luego")
                break
            case _:
                print("Debe ingresar una opción correcta")

menu()
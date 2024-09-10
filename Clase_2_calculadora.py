# Ali, Pablo Sharif
# Comisión 313

while(True):
    operador = input("Ingrese una operación ('+', '-', '*', '/'). Para salir, ingrese 'salir': ").lower()
    if(operador == "salir"):
        print("¡Hasta luego!")
        break
    elif operador == '+' or operador == '-' or operador == '*' or operador == '/':
        num_1 = int(input("Ingrese el primer número: "))
        num_2 = int(input("Ingrese el segundo número: "))
        if operador != '/' or (operador == '/' and num_2 != 0):
            match operador:
                case '+':
                    resultado = num_1 + num_2
                case '-':
                    resultado = num_1 - num_2
                case '*':
                    resultado = num_1 * num_2
                case '/':
                    resultado = num_1 / num_2
            print(f"El resultado es: {resultado}")
        else:
            print("No se puede dividir por cero")    
    else:
        print("Ingrese un operador correcto")
        
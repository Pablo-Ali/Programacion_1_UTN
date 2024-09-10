# Ali, Pablo Sharif
# Comisión 313
# Versión corregida para que tenga For

operador = ""
num_1 = 0
num_2 = 0

while(True):
    operador = input("Ingrese una operación ('+', '-', '*', '/'): ")
    
    if operador == '+' or operador == '-' or operador == '*' or operador == '/':
        break
    
    else:
        print("Ingrese un operador correcto")
        
for i in range(2):
    num = int(input("Ingrese un numero: "))
    if i == 0:
        num_1 = num
    else:
        num_2 = num      

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
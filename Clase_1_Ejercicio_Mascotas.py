contador_consigna_1 = 0
contador_gatos = 0
flag_problemas_digestivos = False
contador_perro_digestivo = 0
contador_gato_digestivo = 0
contador_loro_digestivo = 0
flag_perro_mayor_gato = False
flag_perro_igual_gato = False
flag_loro_igual_gato = False
flag_loro_igual_perro = False
flag_iguales = False
flag_loro_mayor = False
flag_perro_mayor = False
flag_gato_mayor = False
flag_perro_gato_mayor = False
edad_mayor = 0
suma_edad_gatos = 0
tipo_edad_mayor = ""
vacuna_si = 0
vacuna_no = 0

for i in range(20):
    while(True):
        edad = int(input("Ingrese la edad de la mascota: "))
        if edad >= 1 and edad <= 25:
            break
        else:
            print("Ingrese una edad correcta")

    while(True):
        tipo = input("Ingrese la especie de la mascota. Solo atendemos gatos, perros y loros: ").lower()
        if tipo == "gato" or  tipo == "perro" or  tipo == "loro":
            if tipo == "gato":
                contador_gatos += 1
                suma_edad_gatos += edad
            break
        else:
            print("Ingrese una especie admitida (gatos, perros y loros)")

    while(True):
        peso = float(input("Ingrese el peso de la mascota: "))
        if peso > 0:
            break
        else:
            print("Ingrese un peso correcto")
    
    while(True):
        diagnostico = input("Ingrese el problema. Solo atendemos problemas digestivos, parasitos o infecciones: ").lower()
        if diagnostico == "problemas digestivos" or diagnostico == "parasitos" or diagnostico == "infecciones":
            break
        else:
            print("Ingrese un diagnóstico admitido (problemas digestivos, parasitos o infecciones)")
    
    while(True):
        vacuna = input("Ingrese si la mascota posee la vacuna antirrabica s/n: ").lower()
        if vacuna == 's':
            vacuna_si += 1
            break
        elif vacuna == 'n':
            vacuna_no += 1
            break
        else:
            print("Ingrese una respuesta válida (s/n)")
    
    if vacuna == 'n' and edad >=4 and edad <= 12 and (diagnostico == "parasitos" or diagnostico == "infecciones"):
        contador_consigna_1 += 1
    if diagnostico == "problemas digestivos":
        flag_problemas_digestivos = True
        match tipo:
            case "perro":
                contador_perro_digestivo += 1
            case "gato":
                contador_gato_digestivo += 1
            case "loro":
                contador_loro_digestivo += 1
    
    if vacuna == 's':
        if edad > edad_mayor:
            edad_mayor = edad
            tipo_edad_mayor = tipo
    

if flag_problemas_digestivos:
    if contador_perro_digestivo > contador_gato_digestivo:
        flag_perro_mayor_gato = True
    elif contador_perro_digestivo == contador_gato_digestivo:
        flag_perro_igual_gato = True

    if flag_perro_mayor_gato:
        if contador_loro_digestivo > contador_perro_digestivo:
            flag_loro_mayor = True
        elif contador_loro_digestivo == contador_perro_digestivo:
            flag_loro_igual_perro = True
        else:
            flag_perro_mayor = True
    elif flag_perro_igual_gato:
        if contador_perro_digestivo > contador_loro_digestivo:
            flag_perro_gato_mayor = True
        elif contador_loro_digestivo == contador_perro_digestivo:
            flag_iguales = True
        else:
            flag_loro_mayor = True
    else:
        if contador_gato_digestivo > contador_loro_digestivo:
            flag_gato_mayor = True
        elif contador_gato_digestivo == contador_loro_digestivo:
            flag_loro_igual_gato = True
        else:
            flag_loro_mayor = True

porcentaje_vacunados = vacuna_si * 100 / 20
porcentaje_no_vacunados = vacuna_no * 100 / 20

promedio_edad_gatos = suma_edad_gatos / contador_gatos

print(f"Atendimos {contador_consigna_1} mascotas sin la vacuna antirrábica, de entre 4 y 12 años que padecían infecciones o parásitos")

if flag_problemas_digestivos == False:
    print("No hubo mascotas con problemas digestivos")
elif flag_iguales:
    print("Tuvimos la misma cantidad de perros, gatos y loros con problemas digestivos")
elif flag_perro_gato_mayor:
    print("Los tipos de mascotas más ingresados por problemas digestivos fueron el perro y el gato")
elif flag_loro_igual_gato:
    print("Los tipos de mascotas más ingresados por problemas digestivos fueron el loro y el gato")
elif flag_loro_igual_perro:
    print("Los tipos de mascotas más ingresados por problemas digestivos fueron el perro y el loro")
elif flag_gato_mayor == True:
    print("El tipo de mascota más ingresada por problemas digestivos fue el gato")
elif flag_perro_mayor == True:
    print("El tipo de mascota más ingresada por problemas digestivos fue el perro")
else:
    print("El tipo de mascota más ingresada por problemas digestivos fue el loro")

print(f"De las mascotas vacunadas, el mayor fue un {tipo_edad_mayor} de {edad_mayor} años")

print(f"El porcentaje de mascotas vacunadas para la rabia es de: {porcentaje_vacunados}, mientras que el de no vacunados es de: {porcentaje_no_vacunados}")

print(f"El promedio de edad de los gatos atendidos es de: {promedio_edad_gatos} años")
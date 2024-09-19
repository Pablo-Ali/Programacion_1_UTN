from Funciones import *

def ejecutar_menu():
    cantidad_victorias_jugador = 0
    cantidad_victorias_maquina = 0
    contador_pieda_papel_tijera = 0
    puntaje_maximo_adivina_numero = 0
    puntaje_maximo_mayor_menor = 0
    puntaje_final_adivina_numero = 0
    puntaje_final_mayor_menor = 0
    
    while(True):
        print("SALA DE JUEGOS\n1.Jugar al Piedra Papel o Tijera\n2.Jugar al Adivina el Número\n3.Jugar al Mayor/Menor\n4.Mostrar Rankings\n5.Salir")
        
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-5\nSu opcion:",1,5)
        
        if opcion == 1:
            ganador = jugar_piedra_papel_tijera()
            contador_pieda_papel_tijera += 1
            print(f"El ganador es: {ganador}")
            match ganador:
                case "Jugador":
                    cantidad_victorias_jugador += 1
                case "Maquina":
                    cantidad_victorias_maquina += 1
        elif opcion == 2:
            puntaje_final_adivina_numero = jugar_adivina_numero()
            mostrar_mensaje_final(puntaje_final_adivina_numero)
            if puntaje_maximo_adivina_numero == 0:
                puntaje_maximo_adivina_numero = puntaje_final_adivina_numero
            else:
                resultado = calcular_maximo(puntaje_final_adivina_numero, puntaje_maximo_adivina_numero)
                if resultado != -1:
                    puntaje_maximo_adivina_numero = resultado
        elif opcion == 3:
            puntaje_final_mayor_menor = jugar_mayor_menor()
            if puntaje_maximo_mayor_menor == 0:
                puntaje_maximo_mayor_menor = puntaje_final_mayor_menor
            else:
                resultado = calcular_maximo(puntaje_final_mayor_menor, puntaje_maximo_mayor_menor)
                if resultado != -1:
                    puntaje_maximo_mayor_menor = resultado
            print(f"Su puntaje final es: {puntaje_final_mayor_menor}")
        elif opcion == 4:
            print(f"En el juego de Piedra, Papel y Tijera, el jugador ha ganado el {calcular_porcentaje(cantidad_victorias_jugador, contador_pieda_papel_tijera)} % de las veces")
            print(f"En el juego de Piedra, Papel y Tijera, la máquina ha ganado el {calcular_porcentaje(cantidad_victorias_maquina, contador_pieda_papel_tijera)} % de las veces")
            print(f"Su puntaje máximo en Adivina el Número es: {puntaje_maximo_adivina_numero}")
            print(f"Su puntaje máximo en Mayor / Menor es: {puntaje_maximo_mayor_menor}")
        elif opcion == 5:
            print("Saliendo...")
            break
        limpiar_consola()
    
ejecutar_menu()

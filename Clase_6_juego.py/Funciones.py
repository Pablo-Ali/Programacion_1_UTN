import random
import os

#Constantes -> para fecilitar el uso de eso números.

PIEDRA = 1
PAPEL = 2
TIJERA = 3

MAYOR = 1
MENOR = 2

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('clear')

#PEDIR DATOS
def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    while True:
        numero = int(input(mensaje))

        if numero >= minimo and numero <= maximo:
            return numero
        else:
            print(mensaje_error)
    

#RANKINGS
def calcular_maximo(numero_uno:int,numero_dos:int) -> int:
    if numero_uno == numero_dos:
        return -1
    elif numero_uno > numero_dos:
        return numero_uno
    else:
        return numero_dos

def calcular_porcentaje(cantidad_victorias:int,cantidad_partidas:int)->float:
    return (cantidad_victorias / cantidad_partidas) * 100

#JUEGOS EN GENERAL
def generar_respuesta_maquina(minimo:int,maximo:int) -> int:
    return random.randint(minimo, maximo)

#PIEDRA PAPEL O TIJERA
def verificar_ganador_ronda(respuesta_jugador:int,respuesta_maquina:int) -> str:

    if respuesta_jugador == respuesta_maquina:
        return "Empate"
    elif (respuesta_jugador == 1 and respuesta_maquina == 3) or (respuesta_jugador == 2 and respuesta_maquina == 1) or (respuesta_jugador == 3 and respuesta_maquina == 2):
        return "Jugador"
    else:
        return "Maquina"

def verificar_ganador_partida(aciertos_jugador:int,aciertos_maquina:int) -> str:
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    else:
        return "Maquina"


def verificar_estado_partida(aciertos_jugador:int,aciertos_maquina:int,ronda_actual:int) -> bool:
    if ronda_actual >= 3 and (aciertos_jugador != aciertos_maquina):
        return False
    elif ronda_actual == 2 and (aciertos_jugador == 2 or aciertos_maquina == 2):
        return False
    else:
        return True

def obtener_elemento(respuesta:int) -> str:
    match respuesta:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"

def jugar_piedra_papel_tijera() -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    contador_rondas = 0
    
    print("Bienvenido a la partida de Piedra Papel o Tijera")

    while verificar_estado_partida(aciertos_jugador,aciertos_maquina,contador_rondas):
        contador_rondas +=1
        print(f"Ronda: {contador_rondas}")
        
        respuesta_jugador = pedir_numero("Elija un número entre 1 y 3: ", "Error: el número debe ser entre 1 y 3", 1, 3)
        respuesta_maquina = generar_respuesta_maquina(1, 3)
        print(f"Usted ha elegido: {obtener_elemento(respuesta_jugador)}, la máquina ha elegido: {obtener_elemento(respuesta_maquina)}")
        ganador_ronda = verificar_ganador_ronda(respuesta_jugador, respuesta_maquina)
        print(f"Ganador de la ronda: {ganador_ronda}")
        if ganador_ronda == "Jugador":
            aciertos_jugador += 1
        elif ganador_ronda == "Maquina":
            aciertos_maquina += 1
                        
        #NO BORRAR
        limpiar_consola()
        
    #Pista: Debo saber quien gano la partida
    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
            
    return ganador
        
        
#ADIVINA EL NUMERO

def mostrar_mensaje_final(puntaje_final:int)->None:
    if puntaje_final == 0:
        print("Se ve que no eres bueno adivinando, más suerta la próxima")
    elif puntaje_final >= 1 and puntaje_final <= 3:
        print("Buen trabajo adivinando")
    elif puntaje_final >= 4 and puntaje_final <= 5:
        print("Excelente, eres muy bueno adivinando")
    else:
        "Wow, usted es psíquico"

def jugar_adivina_numero() -> int:
    contador_intentos = 3
    puntaje_final = 0
    
    while(contador_intentos != 0):
        #Pista debo reutilizar funciones anteriores que use en el de piedra papel tijera no hacer todo de cero.
        numero_maquina = generar_respuesta_maquina(1, 9)
        numero_jugador = pedir_numero("Elija un número entre 1 y 9: ", "Error: el número debe ser entre 1 y 9", 1, 9)
        if numero_maquina == numero_jugador:
            puntaje_final += 1
        else:
            print(f"Respuesta incorrecta. El número era: {numero_maquina}")
            contador_intentos -= 1
        print(f"Intentos restantes: {contador_intentos}")
        #NO BORRAR
        limpiar_consola()
    
    return puntaje_final


#MAYOR MENOR

def verificar_cartas(carta:int, carta_posterior:int,eleccion_jugador:int) -> str:    
    match eleccion_jugador:
        case 1:
            if carta_posterior == carta:
                return "Iguales"
            elif carta_posterior > carta:
                return "Ganó"
            else:
                return "Perdió"
        case 2:
            if carta_posterior == carta:
                return "Iguales"
            elif carta_posterior < carta:
                return "Ganó"
            else:
                return "Perdió"

        
def jugar_mayor_menor():
    puntuaje_final = 0 
    
    carta_random = generar_respuesta_maquina(1, 12)
    while(True):
        print(f"Carta: {carta_random}")
        respuesta_jugador = pedir_numero("Elija si la siguiente carta será mayor (1) o menor (2): ", "Error, debe elegir 1 o 2 para mayor o menor", 1, 2)
        carta_posterior = generar_respuesta_maquina(1, 12)
        resultado = verificar_cartas(carta_random, carta_posterior, respuesta_jugador)
        print(resultado)
        match resultado:
            case "Ganó":
                puntuaje_final += 1
                carta_random = carta_posterior
            case "Perdió":
                break
        #NO BORRAR
        limpiar_consola()
    
    return puntuaje_final

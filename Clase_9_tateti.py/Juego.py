import Funciones

tateti = Funciones.inicializar_matriz(3,3,0)


print("Bienvenidos a TaTeTi")
print("Para empezar, lanzaremos una moneda para decidir quién comienza")
moneda = Funciones.pedir_cara()

if moneda == 1:
    print("Comienza el Jugador")

    while(True):
        opcion = Funciones.elegir_jugador(tateti)
        Funciones.cargar_posición(tateti, opcion, "X")
        print("Elección del Jugador: ")
        Funciones.mostrar_matriz(tateti)
        print("-----")

        if Funciones.verificar_ganador(tateti, "X"):
            print("¡Felicidades, ganaste la partida!")
            break

        print("Elección de la Máquina:")
        opcion = Funciones.elegir_maquina(tateti)
        Funciones.cargar_posición(tateti, opcion, "O")
        Funciones.mostrar_matriz(tateti)
        print("-----")
        
        if Funciones.verificar_ganador(tateti, "O"):
            print("Ganó la Máquina.")
            break
else:
    print("Comienza la Máquina")

    while(True):
        opcion = Funciones.elegir_maquina(tateti)
        Funciones.cargar_posición(tateti, opcion, "O")
        print("Elección del Jugador: ")
        Funciones.mostrar_matriz(tateti)
        print("-----")

        if Funciones.verificar_ganador(tateti, "O"):
            print("Ganó la Máquina.")
            break

        print("Elección de la Máquina:")
        opcion = Funciones.elegir_jugador(tateti)
        Funciones.cargar_posición(tateti, opcion, "X")
        Funciones.mostrar_matriz(tateti)
        print("-----")
        
        if Funciones.verificar_ganador(tateti, "X"):
            print("¡Felicidades, ganaste la partida!")
            break

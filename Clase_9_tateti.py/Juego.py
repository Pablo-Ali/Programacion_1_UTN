import Funciones

tateti = Funciones.inicializar_matriz(3,3,0)


print("Bienvenidos a Ta Te Ti")
print("Para empezar, lanzaremos una moneda para decidir quién comienza")
moneda = Funciones.pedir_cara()

if moneda == 1:
    print("Comienza el Jugador")

    while(True):
        opcion = Funciones.elegir_jugador(tateti)
        Funciones.cargar_posición_jugador(tateti, opcion)
        print("Elección del Jugador: ")
        Funciones.mostrar_matriz(tateti)
        print("-----")

        #Verificar ganador

        print("Elección de la Máquina:")
        opcion = Funciones.elegir_maquina(tateti)
        Funciones.cargar_posición_maquina(tateti, opcion)
        Funciones.mostrar_matriz(tateti)
        print("-----")
        
        break





else:
    print("Comienza la Máquina")

    while(True):
        opcion = Funciones.elegir_maquina(tateti)
        Funciones.cargar_posición_maquina(tateti, opcion)
        print("Elección del Jugador: ")
        Funciones.mostrar_matriz(tateti)
        print("-----")

        #Verificar ganador

        print("Elección de la Máquina:")
        opcion = Funciones.elegir_jugador(tateti)
        Funciones.cargar_posición_jugador(tateti, opcion)
        Funciones.mostrar_matriz(tateti)
        print("-----")
        
        break

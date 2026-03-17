from utils_Ariela import crea_tablero, crea_barcos, jugar_auto,jugar_manual

def main():
    print("=== Bienvenido a Hundir la Flota ===")
    tamano = int(input("Ingrese el ancho del tablero de juego (debe ser un número entero y positivo): "))

    if type(tamano) != int or tamano < 0:
        print("El número ingresado es incorrecto")

    else: 
        # Creao tableros para cada jugador
        tablero_OR = crea_tablero(tamano)        
        tablero_JU = crea_tablero(tamano)

        # Creo tableros para visualizar los ataques
        tablero_OR2 = crea_tablero(tamano)
        tablero_JU2 = crea_tablero(tamano)
    
    # Coloco barcos en el tablero para el jugador y el ordenador en forma aleatoria
    tableroJUb = crea_barcos(tablero_JU)
    #print("\nTablero del jugador:")
    #print(tableroJUb)

    tableroORb=crea_barcos(tablero_OR)
    #print("\nTablero del ordenador:")
    #print(tableroORb)


    forma_juego = input("Desea ver el juego en forma automática o desea jugar ingresando las coordenadas?, ingrese 'A' para verlo en forma automática, o 'M' para jugar en forma manual:")
    
    
    # OPCIÓN 1 - Juego eligiendo las coordenadas en forma automática
    if forma_juego == 'A':
        print("\nTablero del jugador:")
        print(tableroJUb)
        print("\nTablero del ordenador:")
        print(tableroORb) 
        jugar_auto(tableroORb,tableroJUb,tablero_OR2,tablero_JU2,300)

    else:

    # OPCIÓN 2 - Juego eligiendo las coordenadas en forma manual
        print("\nTablero del jugador:")
        print(tableroJUb)
        print("\nTablero del ordenador:")    ##OCULTAR!!
        print(tableroORb)


        jugar_manual(tableroORb,tableroJUb,tablero_OR2,tablero_JU2,10)

if __name__ == "__main__":
    main()
import numpy as np
import random

## FUNCIÓN PARA CREAR TABLERO
def crea_tablero(tamano):

    tablero = np.full((tamano,tamano)," ")

    if not tamano:
        tablero = np.full((10,10)," ")
  
    return tablero

# FUNCIÓN PARA COLOCAR LOS BARCOS

## PARTE 1 : VERIFICA SI ES POSIBLE COLOCAR EL BARCO


def coloca_barco_plus(tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas:
            #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            #print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        
        tablero_temp[pieza] = "O"    #Aquí coloca la pieza

    # Esta función retorna FALSE si el barco no se puede colocar
    return tablero_temp


## PARTE 2: ELIGE UNA COORDENADA Y ORIENTACIÓN ALEATORIA PARA UBICAR EL BARCO, DENTRO DE LOS LÍMITES DEL TABLERO
def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        # Construimos el hipotetico barco
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))  #pieza original random
        #print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        #print("Con orientacion", orientacion)
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        
        
        tablero_temp = coloca_barco_plus(tablero, barco)  #AQUI LLAMA A COLOCA BARCO

        
        if type(tablero_temp) == np.ndarray:   # Si la función coloca barco_plus devuelve un array si está todo OK, o sea si no devolvió FALSE
            
            return tablero_temp
        #print("Tengo que intentar colocar otro barco")

     
# FUNCIÓN PARA COLOCAR LOS BARCOS DENTRO DEL TABLERO

# Se crean 6 barcos en total (3 barcos de eslora 2, 2 de eslora 3 y 1 eslora 4)


def crea_barcos(tablero):

    esloras = [4, 3, 3, 2, 2, 2]

    for i in esloras:
        tablero = crea_barco_aleatorio(tablero, eslora= i, num_intentos=100)  #Se va sobreescribiendo el tablero con el anterior

    return tablero



# FUNCIÓN PARA RECIBIR DISPARO Y MODIFICAR EL TABLERO

def recibir_disparo(tablero, coordenada):
    acierto = 0
    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        print("Tocado")
        acierto = 1 
    elif tablero[coordenada] == "X":
        print("Agonia, deja de perder el tiempo, dispara a otro sitio")
    else:
        tablero[coordenada] = "-"
        print("Agua")
    return tablero,acierto

# FUNCIÓN PARA JUGAR EN FORMA AUTOMÁTICA  

def jugar_auto(tableroOR,tableroJU,tableroOR2,tableroJU2,turnos):

    num_max_filas = tableroOR.shape[0]
    num_max_columnas = tableroOR.shape[1]

    turnos_ORI = turnos

    vueltas = turnos
    turnos_jug = turnos
    turnos_ord = turnos

    while vueltas > 0:            # Cantidad de turnos alternados entre jugador y ordenador

        while turnos_jug > 0:     # Empieza el jugador, hasta que se le acaben los turnos 

            # Elige una coordenada en forma aleatoria
            print("Turno del jugador 1")
            disparo = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))  
            print(disparo)

            # Llamo a la función de disparo y compruebo si he acertado 
            tableroOR,acierto = recibir_disparo(tableroOR, disparo)

            if acierto == 1:
                print("Has acertado, puedes jugar nuevamente")
                tableroOR2[disparo] = "X" #Marco una X en el tablero que yo veo del ordenador
                print(tableroOR2)

                turnos_jug = turnos_jug-1   #Si he acertado le quito un turno y sigo jugando 

                # Verifico que aún queden barcos
                indices = np.where(tableroOR == "O") # Con where busco la ubicacion
                
                if indices[0].size == 0:
                    print("El jugador 1 ha ganado, eliminados todos los barcos")
                    turnos_jug = 0
                    return
        
            else:
                turnos_jug = 0        #Si no he acertado el ordenador se le acaban los turnos
                #print("turnos jug",turnos_jug)

        
        # Juega el ordenador
        while turnos_ord > 0:
            # Elijo una coordenada en forma aleatoria
            print("Turno del ordenador")
            disparo = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))  
            print(disparo)
            # Disparo y compruebo si he acertado 
            tableroJU,acierto = recibir_disparo(tableroJU, disparo)

            if acierto == 1:
                print("El ordenador ha acertado, puede jugar nuevamente")
                tableroJU2[disparo] = "X"  #Marco una X en el tablero que yo veo del ordenador
                print(tableroJU2)
                
                turnos_ord = turnos_ord-1

                # Verifico que aún queden barcos
                indices = np.where(tableroJU == "O") # Con where busco la ubicacion
                if indices[0].size == 0:
                    print("El ordenador ha ganado, eliminados todos los barcos")
                    turnos_ord = 0
                    return
        
            else:
                turnos_ord = 0   #Si no ha acertado el ordenador se le acaban los turnos
                
        #print(vueltas)
        vueltas = vueltas -1

        #Reinicio los turnos de los jugadores para la siguiente vuelta
        turnos_ord = turnos_ORI
        turnos_jug = turnos_ORI


def jugar_manual(tableroOR,tableroJU,tableroOR2,tableroJU2,turnos):

    num_max_filas = tableroOR.shape[0]
    num_max_columnas = tableroOR.shape[1]

    turnos_ORI = turnos

    vueltas = turnos
    turnos_jug = turnos
    turnos_ord = turnos

    while vueltas > 0:            # Cantidad de turnos alternados entre jugador y ordenador

        while turnos_jug > 0:

            # Empieza el jugador 
            # Elijo una coordenada en forma random
            print("Turno del jugador 1")
            disparo_us = input(f"Ingresa la coordenada a disparar. Debe ser un número mayor que cero, separado por comas de formato (fila,columna) y las dimensiones deben ser menores a {num_max_filas} x {num_max_columnas} ")
            
            fila, columna = disparo_us.split(",")   # separa por coma el valor ingresado
         
            fila = int(fila)-1
            columna = int(columna) -1
            
            if fila < 0 or columna < 0:
                print("No se pueden ingresar números negativos")        
            
            if fila >= num_max_filas or columna >= num_max_columnas:
                print("La coordenada debe estar dentro del tablero")

            disparo = (fila, columna)                      
                    
            # Disparo y compruebo si he acertado 
            tableroOR,acierto = recibir_disparo(tableroOR, disparo)

            if acierto == 1:

                print("Has acertado, puedes jugar nuevamente")
                tableroOR2[disparo] = "X"  #Marco una X en el tablero que yo veo del ordenador
                print(tableroOR2)
                turnos_jug = turnos_jug-1

                # Verifico que aún queden barcos
                indices = np.where(tableroOR == "O") # Con where busco la ubicacion
                
                if indices[0].size == 0:
                    print("El jugador 1 ha ganado, eliminados todos los barcos")
                    turnos_jug = 0
                    return
        
            else:
                turnos_jug = 0
                #print("turnos jug",turnos_jug)

        
        # Juega el ordenador
        while turnos_ord > 0:

            print("Turno del ordenador")
            # Elijo una coordenada en forma random
            disparo = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))  
            print(disparo)
            # Disparo y compruebo si he acertado 
            tableroJU,acierto = recibir_disparo(tableroJU, disparo)

            if acierto == 1:
                print("El ordenador ha acertado, puede jugar nuevamente")
                tableroJU2[disparo] = "X" #Marco una X en el tablero que ve del jugador
                print(tableroJU2)
                turnos_ord = turnos_ord-1

                # Verifico que aún queden barcos
                indices = np.where(tableroJU == "O") # Con where busco la ubicacion
                if indices[0].size == 0:
                    print("El ordenador ha ganado, eliminados todos los barcos")
                    turnos_ord = 0
                    return
        
            else:
                turnos_ord = 0
                #print("turnos ord",turnos_ord)


        #print(vueltas)
        vueltas = vueltas -1

        #Reinicio los turnos de los jugadores
        turnos_ord = turnos_ORI
        turnos_jug = turnos_ORI
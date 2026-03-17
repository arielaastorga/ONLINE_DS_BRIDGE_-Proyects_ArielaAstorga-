# Hundir la Flota (Battleship) en Python 

Este proyecto implementa el clásico juego **Hundir la Flota (Battleship)** en Python. 
Permite jugar en **modo manual**, ingresando coordenadas, o en **modo automático**, donde las coordenadas se generan aleatoriamente.


 --- ## Tabla de Contenidos 
 -  [Descripción](#descripción) 
 - [Instalación](#instalación) - [Uso](#uso) 
 - [Funciones Principales](#funciones-principales) 
 - [Ejemplo de Juego](#ejemplo-de-juego) - [Autor](#autor) 
 - [Licencia](#licencia) 
 
  
## Descripción 
El juego consiste en un tablero cuadrado donde se colocan barcos de diferentes tamaños: - 3 barcos de eslora 2 - 2 barcos de eslora 3 - 1 barco de eslora 4 El jugador y el ordenador disparan por turnos tratando de hundir todos los barcos del adversario. Se pueden visualizar los ataques realizados con: - "X" → acierto - "-" → agua El jugador manual ingresa las coordenadas de los disparos, mientras que en modo automático el ordenador juega ambos bandos aleatoriamente. --- ## Instalación 1. Clonar el repositorio o descargar los archivos. 2. Instalar las dependencias necesarias (solo **numpy**, incluido en Python estándar):
bash
pip install numpy

## Uso
Ejecuta el programa principal:

python main.py

Se pedirá:

Tamaño del tablero (ejemplo: 10 para un tablero 10x10)

Modo de juego:

"M" → Manual (ingresas las coordenadas)

"A" → Automático (el ordenador juega ambos bandos aleatoriamente)

En modo manual, ingresa coordenadas en el formato (fila,columna) empezando en 1, separadas por coma:


## Funciones Principales

Creación y gestión del tablero

* crea_tablero(tamano)
    Crea un tablero vacío de tamaño tamano x tamano.
    Retorna un array de numpy lleno de espacios " ".

* coloca_barco_plus(tablero, barco)
    Verifica si un barco se puede colocar:
    Comprueba que no se salga del tablero
    No se superponga con otros barcos
    Retorna el tablero actualizado con el barco o False si no es posible.

* crea_barco_aleatorio(tablero, eslora=4)
    Coloca un barco de longitud eslora aleatoriamente en el tablero.
    Usa coloca_barco_plus para verificar la colocación.

* crea_barcos(tablero)
    Coloca todos los barcos dentro del tablero según la lista de esloras [4, 3, 3, 2, 2, 2].

Funciones de juego

* recibir_disparo(tablero, coordenada)
    Marca un disparo en el tablero:
    "O" → "X" si acierta un barco  
    "X" → indica que ya disparaste allí
    " " → "-" agua
Retorna el tablero actualizado y una variable acierto (1 si acertó, 0 si no).

* jugar_manual(tableroOR, tableroJU, tableroOR2, tableroJU2, turnos)
    Permite jugar manualmente.
    tableroOR → tablero del ordenador
    tableroJU → tablero del jugador
    tableroOR2 → tablero de visualización de daños sobre el ordenador
    tableroJU2 → tablero de visualización de daños sobre el jugador
    turnos → número máximo de turnos
    jugar_auto(tableroOR, tableroJU, tableroOR2, tableroJU2, turnos)
    Simula el juego automáticamente, eligiendo coordenadas de disparo aleatorias.
    Controla turnos, aciertos y fin del juego.

## Ejemplo de Juego

import numpy as np
from utils import crea_tablero, crea_barcos, jugar_manual, jugar_auto

# Crear tableros
tablero_jugador = crea_tablero(5)
tablero_ordenador = crea_tablero(5)

# Colocar barcos
tablero_jugador = crea_barcos(tablero_jugador)
tablero_ordenador = crea_barcos(tablero_ordenador)

# Tableros de visualización de ataques
tablero_jugador_vis = crea_tablero(5)
tablero_ordenador_vis = crea_tablero(5)

# Jugar manual
jugar_manual(tablero_ordenador, tablero_jugador,
             tablero_ordenador_vis, tablero_jugador_vis, 3)

# Jugar automático
jugar_auto(tablero_ordenador, tablero_jugador,
           tablero_ordenador_vis, tablero_jugador_vis, 3)


## Autor

Ariela Astorga


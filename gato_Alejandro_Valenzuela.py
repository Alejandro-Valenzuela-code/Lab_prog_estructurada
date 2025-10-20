print("Juega al gato ")  # Mensaje inicial en pantalla

x = "___"  # Cadena que representa una casilla vacía

a1 = x  # Casilla fila A, columna 1 (inicialmente vacía)
a2 = x  # Casilla fila A, columna 2 (inicialmente vacía)
a3 = x  # Casilla fila A, columna 3 (inicialmente vacía)
b1 = x  # Casilla fila B, columna 1 (inicialmente vacía)
b2 = x  # Casilla fila B, columna 2 (inicialmente vacía)
b3 = x  # Casilla fila B, columna 3 (inicialmente vacía)
c1 = x  # Casilla fila C, columna 1 (inicialmente vacía)
c2 = x  # Casilla fila C, columna 2 (inicialmente vacía)
c3 = x  # Casilla fila C, columna 3 (inicialmente vacía)

import random  # Importa el módulo random para generar jugadas aleatorias de la computadora

inicio = random.randint(0, 1)  # Decide al azar quién empieza (0 = jugador, 1 = computadora)
turnos = 9  # Número total de jugadas posibles (9 casillas)
ganador = 0  # Bandera de victoria (0 = nadie ha ganado aún)

while turnos != 0 and ganador == 0:  # Bucle principal: corre mientras queden turnos y no haya ganador
    if inicio == 0:  # Si es el turno del jugador
        print("Turno del jugador, tu símbolo es X")  # Anuncia turno del jugador
        ocupado = 1  # Controla que el jugador elija una casilla válida/libre
        while ocupado == 1:  # Repite hasta que elija una casilla libre
            print(f"{a1}|{a2}|{a3}\n{b1}|{b2}|{b3}\n{c1}|{c2}|{c3}")  # Muestra el tablero actual
            print("Ingresa una casilla del 1 al 9")  # Indica el rango válido
            casilla = input("Ingresa una casilla: ")  # Lee la casilla elegida por el jugador (texto)

            if casilla == "1" and a1 == x:  # Si eligió 1 y está libre
                a1 = " X "  # Coloca una X en a1
                ocupado = 0  # Sale del bucle interno (jugada válida)
            elif casilla == "2" and a2 == x:  # Si eligió 2 y está libre
                a2 = " X "  # Coloca una X en a2
                ocupado = 0  # Jugada válida
            elif casilla == "3" and a3 == x:  # Si eligió 3 y está libre
                a3 = " X "  # Coloca una X en a3
                ocupado = 0  # Jugada válida
            elif casilla == "4" and b1 == x:  # Si eligió 4 y está libre
                b1 = " X "  # Coloca una X en b1
                ocupado = 0  # Jugada válida
            elif casilla == "5" and b2 == x:  # Si eligió 5 y está libre
                b2 = " X "  # Coloca una X en b2
                ocupado = 0  # Jugada válida
            elif casilla == "6" and b3 == x:  # Si eligió 6 y está libre
                b3 = " X "  # Coloca una X en b3
                ocupado = 0  # Jugada válida
            elif casilla == "7" and c1 == x:  # Si eligió 7 y está libre
                c1 = " X "  # Coloca una X en c1
                ocupado = 0  # Jugada válida
            elif casilla == "8" and c2 == x:  # Si eligió 8 y está libre
                c2 = " X "  # Coloca una X en c2
                ocupado = 0  # Jugada válida
            elif casilla == "9" and c3 == x:  # Si eligió 9 y está libre
                c3 = " X "  # Coloca una X en c3
                ocupado = 0  # Jugada válida
            else:
                print("Esa casilla está ocupada o no existe")  # Mensaje de error si casilla no válida/ocupada

        inicio = 1  # Cambia el turno a la computadora
        turnos = turnos - 1  # Consume un turno (ya jugó el jugador)
        print(f"Quedan {turnos} turnos restantes (fue tu turno)")  # Muestra turnos restantes
    else:  # Si es el turno de la computadora
        print("Turno de la computadora")  # Anuncia turno de la computadora
        ocupado = 1  # Control para elegir una casilla libre
        while ocupado == 1:  # Repite hasta que encuentre una casilla libre
            casilla = str(random.randint(1, 9))  # La computadora elige una casilla aleatoria (como texto)

            if casilla == "1" and a1 == x:  # Si 1 está libre
                a1 = " O "  # Coloca una O en a1
                ocupado = 0  # Jugada válida
            elif casilla == "2" and a2 == x:  # Si 2 está libre
                a2 = " O "  # Coloca una O en a2
                ocupado = 0  # Jugada válida
            elif casilla == "3" and a3 == x:  # Si 3 está libre
                a3 = " O "  # Coloca una O en a3
                ocupado = 0  # Jugada válida
            elif casilla == "4" and b1 == x:  # Si 4 está libre
                b1 = " O "  # Coloca una O en b1
                ocupado = 0  # Jugada válida
            elif casilla == "5" and b2 == x:  # Si 5 está libre
                b2 = " O "  # Coloca una O en b2
                ocupado = 0  # Jugada válida
            elif casilla == "6" and b3 == x:  # Si 6 está libre
                b3 = " O "  # Coloca una O en b3
                ocupado = 0  # Jugada válida
            elif casilla == "7" and c1 == x:  # Si 7 está libre
                c1 = " O "  # Coloca una O en c1
                ocupado = 0  # Jugada válida
            elif casilla == "8" and c2 == x:  # Si 8 está libre
                c2 = " O "  # Coloca una O en c2
                ocupado = 0  # Jugada válida
            elif casilla == "9" and c3 == x:  # Si 9 está libre
                c3 = " O "  # Coloca una O en c3
                ocupado = 0  # Jugada válida
            else:
                ocupado = 1  # Si la casilla estaba ocupada, vuelve a intentar

        turnos -= 1  # Consume un turno (ya jugó la computadora)
        inicio = 0  # Cambia el turno al jugador
        print(f"Quedan {turnos} turnos restantes (fue turno de la computadora)")  # Muestra turnos restantes

    if (  # Bloque que verifica si hubo un ganador tras la última jugada
        a1 == a2 and a2 == a3 and a1 != "___"  # Fila A completa por el mismo símbolo
        or b1 == b2 and b2 == b3 and b1 != "___"  # Fila B completa
        or c1 == c2 and c2 == c3 and c1 != "___"  # Fila C completa
        or a1 == b1 and b1 == c1 and a1 != "___"  # Columna 1 completa
        or a2 == b2 and b2 == c2 and a2 != "___"  # Columna 2 completa
        or a3 == b3 and b3 == c3 and a3 != "___"  # Columna 3 completa
        or a1 == b2 and b2 == c3 and a1 != "___"  # Diagonal principal completa
        or a3 == b2 and b2 == c1 and a3 != "___"  # Diagonal secundaria completa
    ):
        ganador = 1  # Marca que hay ganador
        print(f"{a1}|{a2}|{a3}\n{b1}|{b2}|{b3}\n{c1}|{c2}|{c3}")  # Muestra el tablero final
        if inicio == 1:  # Si inicio es 1 aquí, significa que el último turno fue del jugador
            print("¡Ganaste!")  # Mensaje de victoria para el jugador
        else:  # Si no, el último turno fue de la computadora
            print("Perdiste")  # Mensaje de derrota
        break  # Sale del bucle principal porque el juego terminó

if ganador == 0:  # Si se acabaron los turnos sin ganador
    print(f"{a1}|{a2}|{a3}\n{b1}|{b2}|{b3}\n{c1}|{c2}|{c3}")  # Muestra el tablero final
    print("Empate")  # Informa empate

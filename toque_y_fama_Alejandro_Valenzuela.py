import random

print("Juguemos toque y fama")

# Generar número secreto con 4 dígitos distintos
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)

# Asegurar que los 4 sean distintos
while len({a, b, c, d}) < 4: #se asegura que los cuatros digitos sean distintos 
    a, b, c, d = [random.randint(0, 9) for _ in range(4)]


# --- Función para pedir y separar dígitos ---
def pedir_numero():
    """Pide un número y devuelve sus dígitos separados."""
    while True: #inicia un bucle hasta que el usuario ingrese un numero valido 
        try:
            n = int(input("Ingresa un número de 4 dígitos: ")) #Pide un al usuario un numero entero 
            if not 0 <= n <= 9999:  #Verifica que el numero este en el rango permitido 
                print("Debe ser un número entre 0000 y 9999.") 
                continue #si no lo esta, vuelve a pedir 

            # Separar los cuatro digitos 
            z = n % 10    #ultimo digito (unidades)
            y = (n // 10) % 10  #Tercer digito (decimas)
            x = (n // 100) % 10  #Segundo digito (centenas)
            w = (n // 1000)  # Primer digito (miles)
            
            # Verifica que los cuatro digitos sean distintos 
            if len({w, x, y, z}) < 4:
                print("Los dígitos deben ser distintos. Intenta de nuevo.")
                continue #vuelve a pedir el numero si hay repetidos 
#si todo esta bien, devuelve el numero completo y los digitos separados 
            return n, w, x, y, z
        except ValueError: #si se ingresa un caracter que no sea un numero 
            print("Debes ingresar un número válido.")


def escribe(w, x, y, z):
    """Muestra los dígitos ingresados."""
    print(f"Tu número ingresado es: {w, x, y, z}") #(f)sirve para colocar funciones en el print 


# --- Variables iniciales del juego ---
intentos = 5  #Cantidad de intentos disponibles 
fama = 0      #Contador de digitos correctos y en la posicion correcta 
toque = 0     #Contador de digitos correctos pero en otra posicion 

# --- Bucle principal ---
while intentos > 0:     #mientras queden intentos 
    intentos -= 1     #se resta uno en cada ronda 
    fama = toque = 0  # reiniciar contadores
#Se pide un numero al jugador y separa en digitos 
    n, w, x, y, z = pedir_numero()
    escribe(w, x, y, z) #se muestra el numero ingresado 

    # Se guarda el numero secreto y el del jugador en listas 
    secreto = [a, b, c, d]
    jugador = [w, x, y, z]
# Recorre los 4 digitos para comparar uno por uno 
    for i in range(4):
        if jugador[i] == secreto[i]:
            fama += 1
        elif jugador[i] in secreto:
            toque += 1

    # Mostrar el resultado del intento actual   
    print(f"Tienes {toque} número/s correcto/s en posición equivocada "
          f"y {fama} número/s correcto/s en la posición exacta.\n")

    if fama == 4: #si adivino los 4 digitos, termina el juego 
        break  # salió del bucle porque ganó
    else: #si no acerto le muestra los intentos restantes 
        print(f"Te quedan {intentos} intento/s restante/s.\n")

# --- Resultado final ---
if fama == 4: #si tiene 4 famas gana el juego 
    print("¡Felicidades, ganaste!")
else:  #si se le acaban los intentos perdio 
    print("Perdiste...")
#muestra el numero secreto al final del juego 
print(f"El número era: {a, b, c, d}")

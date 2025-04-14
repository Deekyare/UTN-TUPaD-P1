""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. """

import random
# Generamos un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

# Inicializamos el contador de intentos
intentos = 0

# Inicializamos la variable número en -1, no puede ser 0.
numeroIngresado = -1

# Mientras el número ingresado no sea igual al número aleatorio

while numeroIngresado != numero_aleatorio:
    # Solicitamos al usuario que ingrese un número
    numeroIngresado = int(input("Adivina el número (entre 0 y 9): "))
    
    # Incrementamos el contador de intentos
    intentos += 1
    
    # Comprobamos si el número ingresado es menor o mayor que el número aleatorio
    if numeroIngresado < numero_aleatorio:
        print("El número es mayor.")
    elif numeroIngresado > numero_aleatorio:
        print("El número es menor.")
        
# Mostramos el resultado                    
print(f"¡Felicidades! El número era {numero_aleatorio}. Y lo divinaste en {intentos} intentos.")

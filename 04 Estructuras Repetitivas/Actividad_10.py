""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

# Pedimos el número al usuario
numero = int(input("Ingrese un número entero: "))

# Guardamos el número original para el mensaje final
numero_original = numero

# Inicializamos el número invertido
invertido = 0

while numero > 0:
    # Extraemos el último dígito
    digito = numero % 10
    # Añadimos el dígito al número invertido
    invertido = invertido * 10 + digito
    # Eliminamos el último dígito del número original
    numero //= 10

# Mostramos el resultado
print(f"El número {numero_original} con sus dígitos invertidos es: {invertido}")

				
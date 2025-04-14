""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. """

#Inicializamos las variable número1 y numero2 con un dato ingresado por el usuario.
acumulador = 0

# Solicitamos el primer número
numero = int(input("Ingrese el primer número: "))

while numero != 0:
    acumulador += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))

# Mostramos el total acumulado
print(f"El total acumulado es: {acumulador}")
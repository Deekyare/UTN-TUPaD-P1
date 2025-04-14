""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. """

#Inicializamos la variable número con un dato ingresado por el usuario.
numero = input("Ingrese un número entero: ")

#Inicializamos la variable contador en 0
contador = 0

#Recorremos la variable numero (contiene un número) y en cada posición (donde se encuentra cada digito),
#sumamos 1 a la variable contador. De esta forma iremos contando los digitos del número.

for i in numero:
    contador += 1
print(f"El número ingresado tiene: {contador} digitos")

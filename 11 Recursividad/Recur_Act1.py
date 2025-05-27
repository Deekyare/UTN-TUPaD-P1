'''Crea una función recursiva que calcule el factorial de un número.
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los
números enteros entre 1 y el número que indique el usuario'''

# Factorial ejemplo: 4! = 4*3*2*1

# Le solicita al usuario un número para calcular el factorial
n = int(input("Introduce un número entero positivo: "))

# Definimos la función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Mostramos el resultado del factorial
print(f"El factorial de {n} es: {factorial(n)}")
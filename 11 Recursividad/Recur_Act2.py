'''Crea una función recursiva que calcule el valor de la serie de Fibonacci
en la posición indicada. Posteriormente, muestra la serie completa hasta 
la posición que el usuario especifique.'''

# Fibonacci ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

# Solicitar al usuario un número para calcular la serie de Fibonacci
posicion = int(input("Introduce un número entero positivo: "))

# Definimos la función recursiva para calcular el valor de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
    
print(f"El valor de Fibonacci en la posición {posicion} es: {fibonacci(posicion)}")
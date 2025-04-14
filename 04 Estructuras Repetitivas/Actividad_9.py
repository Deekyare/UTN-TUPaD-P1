""" 9)Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
(Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
"""

# Definimos la cantidad de números a ingresar (cambiar a 100 para el caso completo)
cantidad_numeros = 10 

# Inicializamos la suma para calcular la media
suma = 0

# Pedimos los números en un bucle
for i in range(cantidad_numeros):
    # Pedimos el número y lo convertimos a entero
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

# Calculamos la media
media = suma / cantidad_numeros

# Mostramos el resultado
print(f"La media de los {cantidad_numeros} números ingresados es: {media}")
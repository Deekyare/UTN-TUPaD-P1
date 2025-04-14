""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros.
Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos
y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado
para procesar 100 números con un solo cambio). """

# Definimos la cantidad de números a ingresar (cambiar a 100 para el caso completo)
cantidad_numeros = 10  # Usamos 10 para pruebas, cambiar a 100 para el caso real

# Inicializamos los contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Pedimos los números en un bucle
for i in range(cantidad_numeros):
    # Pedimos el número y lo convertimos a entero
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    # Contamos pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contamos positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    # Si numero es 0, no se cuenta ni como positivo ni como negativo

# Mostramos los resultados
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

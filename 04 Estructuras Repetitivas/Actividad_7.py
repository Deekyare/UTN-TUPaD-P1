""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo
indicado por el usuario.  """

# Inicializamos la variable suma
suma = 0

# Pedimos el número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Validamos que el número sea positivo
if numero >= 0:
    
    # Recorremos los números desde 0 hasta numero (inclusive)
    for i in range(numero + 1):
        suma += i
    # Mostramos el resultado
    print(f"La suma de los números comprendidos entre 0 y {numero} es: {suma}")
else:
    print("Error: Por favor ingrese un número entero positivo.")
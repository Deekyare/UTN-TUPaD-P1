""" Crear una función llamada operaciones_basicas(a, b)
    que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
    restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara. """

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    #Hay que realizar una estructura especial para la division. En caso de que el valor de "b" sea 0
    #None representa la ausencia de un valor.
    division = None
    if b != 0:
        division = a / b
    # Creamos y devolvemos una tupla con los resultados
    return (suma, resta, multiplicacion, division)

# Llamamos a la función y la tupla de resultados se guarda en la variable 'resultados'
resultados = operaciones_basicas(5, 2)

# "resultados" ahora es una tupla: (7, 3, 10, 2.5)

# Podemos acceder a los elementos de la tupla utilizando su índice (como en una lista)
print(f"La suma es: {resultados[0]}")  # Imprime: La suma es: 7
print(f"La resta es: {resultados[1]}") # Imprime: La resta es: 3
print(f"La multiplicación es: {resultados[2]}") # Imprime: La multiplicación es: 10
print(f"La división es: {resultados[3]}") # Imprime: La división es: 2.5

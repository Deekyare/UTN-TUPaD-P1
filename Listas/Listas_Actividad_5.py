""" 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza."""

# La variable números, contiene una lista de números.
numeros = [8, 15, 3, 22, 7]
# El método remove elimina un valor de la lista que elijamos.
# Con "max" eliminamos el valor mayor, de la ya mencionada lista. 22 en este caso.
numeros.remove(max(numeros))
#Imprime la lista luego del cambio.
print(numeros)


""" Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla
    los dos primeros."""
#Lista vacía donde se iran guardando los números en cada iteración
numeros = []
#Bucle for que recorre números en un rango del 10 al 30 (incluído).
for i in range (10,31,5):
    #Agrega el valor actual a la variable números
    numeros.append(i)
#Imprime la lista completa
print(numeros)
#Imprime los dos primeros números 
print(f"Primer valor: {numeros[0]}, Segundo valor: {numeros[1]}")

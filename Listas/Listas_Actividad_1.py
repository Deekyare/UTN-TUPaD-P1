""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. """

#Bucle for que recorre un rango del 1 al 101 sin incluirlo.
for i in range (1,101):
    #Estructura if para tomar solo los números múltiplos de 4
    if i % 4 == 0:
        #Guardamos los multiplos de 4 en la variable lista
        lista = i
        #Imprimimos la lista
        print(lista)

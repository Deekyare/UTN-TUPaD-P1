""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. """


for i in range (1,101):
    if i % 4 == 0:
        lista = i
        print(lista)

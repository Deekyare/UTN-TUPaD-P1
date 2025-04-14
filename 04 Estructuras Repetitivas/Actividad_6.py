""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100,
en orden decreciente."""

#Utilizamos una estructura for con una función "range", que comienza en 100 y termina en 0 sin incluirlo.
#A su vez colocamos el parametro -2, lo cual indica que en cada vuelta realizará un salto de dos números hacia atras.
for i in range(100, 0, -2):
    #Imprimimos i, para mostar los números del 0 al 101 de 2 en 2
    print(i)
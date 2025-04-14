""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos),
en orden creciente, mostrando un número por línea. """

#Utilizamos una estructura for con una función "range", que comienza en 0 y termina en 101 sin incluirlo.
#A su vez colocamos el parametro 2, lo cual indica que en cada vuelta realizará un salto de dos números.
for i in range(0, 101, 2):
    #Imprimimos i, para mostar los números del 0 al 101 de 2 en 2
    print(i)
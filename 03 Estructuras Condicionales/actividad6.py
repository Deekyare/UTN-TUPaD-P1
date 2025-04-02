# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar
#    si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

import random
from statistics import mode, median, mean

print("\nActividad 6\n")
# Lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(20)]

# Calcular la moda, la mediana y la media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Sesgo
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo o a la derecha"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo o a la izquierda"
else:
    sesgo = "Sin sesgo"

# Imprimir los resultados
print("Lista de números aleatorios:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)
print("Sesgo:", sesgo)
""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. """

# 1) Crear una lista vacía
multiplos_de_4 = []

# Bucle for que recorre un rango del 1 al 101 (para incluir el 100).
for i in range(1, 101):
    # Estructura if para tomar solo los números múltiplos de 4
    if i % 4 == 0:
        # 2) Agregamos el múltiplo de 4 a la lista
        multiplos_de_4.append(i)

# 3) Imprimimos la lista completa
print(multiplos_de_4)
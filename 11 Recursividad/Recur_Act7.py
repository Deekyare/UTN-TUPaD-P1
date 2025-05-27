'''Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo
y devuelva el total de bloques que necesita para construir toda la pirámide.

'''

bloques_base = int(input("Ingrese la cantidad de bloques en la base: "))

def contar_bloques (bloques_base):
    if bloques_base == 0:
        return 0
    elif bloques_base == 1:
        return 1
    else:
        return bloques_base + (contar_bloques(bloques_base-1))
    
print(f"Se necesitan {contar_bloques(bloques_base)} bloques en total para construir una torre con una base de {bloques_base}.")
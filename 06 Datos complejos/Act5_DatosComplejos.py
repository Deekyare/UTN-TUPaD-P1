""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra. """

frase = input("Ingrese una frase: ")

# Convertimos la frase en una lista de palabras
palabras = frase.lower().split()

# Palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Contar la frecuencia de cada palabra
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("Frecuencia de palabras:")
for palabra, cantidad in frecuencia.items():
    print(f"{palabra}: {cantidad}")
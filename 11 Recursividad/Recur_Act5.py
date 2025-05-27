'''Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes,
y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().'''

# reconocer 

palabra = input("Ingrese un número entero positivo: ")

def es_palindromo(palabra):
    # Caso Base 1: Si la palabra tiene 0 o 1 caracteres, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Caso Base 2: Si el primer y último caracter no coinciden, no es un palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    # Paso Recursivo: Comprobamos el resto de la palabra
    else:
        # Quitamos el primer y el último caracter y llamamos a la función con la subcadena
        return es_palindromo(palabra[1:-1])

print(f"{palabra} ¿Es palíndroma? {es_palindromo(palabra)} ")
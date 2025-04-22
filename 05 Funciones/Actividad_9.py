""" Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius
    y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado
    usando la función. """

# Variable para guardar el dato ingresado por el usuario.
celsius = float(input("Ingrese la temperatura actual en grados celsius: "))

#Función que realiza el calculo de conversión
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) +32
    return fahrenheit

# Llamar a la función y mostrar el resultado de la conversión.
en_fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados celsius equivalen a {en_fahrenheit} fahrenheit")


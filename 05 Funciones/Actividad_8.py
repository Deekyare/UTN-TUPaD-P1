""" Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
    y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
    para mostrar el resultado con dos decimales. """

# Variables para guardar los datos ingresado por el usuario.
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Llamar a la función y mostrar el resultado con dos decimales.
resultado_imc = calcular_imc(peso, altura)
print(f"Según los datos ingresados, su IMC es de: {resultado_imc:.2f}")


""" Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio
    de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función. """

# Variables para guardar los datos ingresado por el usuario.
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

#Función para calcular el promedio de los números ingresados
def calcular_promedio(numero1, numero2, numero3):
    promedio = (numero1+numero2+numero3)/3
    return promedio

# Llamar a la función y mostrar el resultado de los promedios.
resultado = calcular_promedio(numero1, numero2, numero3)
print(f"El promedio entre los numeros {numero1}, {numero2}, {numero3} es: {resultado:.2f}")


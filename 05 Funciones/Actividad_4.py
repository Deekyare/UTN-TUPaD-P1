""" Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
    calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
    Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. """

import math

# Obteniendo el valor de Pi a traves de la importación math
pi = math.pi

#Variable que guardará los datos ingresados por el usuario
radio = float(input("\nIngrese el radio del círculo: "))

#Esta función imprime el área de un círculo'  
def calcular_area_circulo(radio):
    area = pi * radio ** 2
    print(f"\nEl área del círculo es: {area}!")
    
    
#Esta función imprime el perímetro de un circulo!'      
def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    print(f"\nEl perímetro del círculo es: {perimetro}")
    

#Llamar a las funciones
calcular_perimetro_circulo(radio)
calcular_area_circulo(radio)




""" Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros
    e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
    Pedir los datos al usuario y llamar a esta función con los valores ingresados. """

#Variables que guardaran los datos ingresados por el usuario
nombre = input("\nIngrese su nombre: ")
apellido = input("\nIngrese su apellido: ")
edad = input("\nIngrese su edad: ")
residencia = input("\nIngrese su residencia: ")

#Esta función imprime un mensaje con los datos ingresados!'
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"\nSoy {nombre} {apellido}, tengo {edad} y vivo en {residencia}!")

#Llamar a la función
informacion_personal(nombre, apellido, edad, residencia)

""" 
Otra forma:

    def informacion_personal():
    nombre = input("\nIngrese su nombre: ")
    apellido = input("\nIngrese su apellido: ")
    edad = input("\nIngrese su edad: ")
    residencia = input("\nIngrese su residencia: ")
    print(f"\nSoy {nombre} {apellido}, tengo {edad} y vivo en {residencia}!")

informacion_personal() """
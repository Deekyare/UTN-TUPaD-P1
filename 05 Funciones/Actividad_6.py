""" Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla 
    de multiplicar de ese número del 1 al 10.
    Pedir al usuario el número y llamar a la función. """
    
# Variable para guardar el número ingresado por el usuario.
numero = int(input("Ingrese un número: "))

#Función para mostrar la tabla de multiplicar de un número ingresado por el usuario.
def tabla_multiplicar(numero):
    print (f"La tabla del {numero} es: \n")
    #Bucle for para iterar un número del 1 al 11 sin incluirlo, multiplicándolo en cada vuelta.
    for i in range(1,11):
        #Mostrar la tabla
        print (f"{numero} * {i} = {numero * i}")

#Llamar a la función
tabla_multiplicar(numero)
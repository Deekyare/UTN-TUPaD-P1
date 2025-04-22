""" Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
    Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
    Llamar a esta función desde el programa principal solicitando el nombre al usuario. """

#Esta función imprime el mensaje 'Hola + nombre!'    
def saludar_usuario():
    nombre = input("\nIngrese su nombre: ")  # Pide el nombre al usuario
    print(f"\nHola {nombre}!")
    
#Llamar a la función
saludar_usuario()
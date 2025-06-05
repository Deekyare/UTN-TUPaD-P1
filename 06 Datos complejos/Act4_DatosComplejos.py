""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe. """

# Crear el diccionario vacío
contactos = {}

# Cargar hasta 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número del contacto {i+1}: ")
    contactos[nombre] = numero
    print("Contacto agregado.")

# Consultar un contacto
consulta = input("Ingrese el nombre del contacto que desea buscar: ")
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("Contacto no encontrado.")
    



# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

print("\nActividad 4\n")
# Ingreso de datos
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("\nUsted es un niño/a.")
elif edad >= 12 and edad < 18:
    print("\nUsted es un adolescente.")
elif edad >= 18 and edad < 30:
    print ("\nUsted es un adulto/a joven.")
else:
    print ("\n Usted es un adulto/a.")

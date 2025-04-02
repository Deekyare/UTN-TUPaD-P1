# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

print("\nActividad 8\n")

# Ingreso de dato
nombre = input("Ingrese su nombre: \n")
print("¿Como desea ver su  nombre?\n")
print("_ Si quiere su nombre en mayúsculas, precione: 1.\n_ Si quiere su nombre en minúsculas, precione: 2.\n_ Si quiere su nombre con la primera letra mayúscula, precione: 3.\n")
# Ingreso de opcion
opcion = int(input ("Ingrese una opcion: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Elija una opcion valida")
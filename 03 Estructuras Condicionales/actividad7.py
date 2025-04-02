# 7) Escribir un programa que solicite una frase o palabra al usuario.
#    Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla;
#    en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

print("\nActividad 7\n")

# Ingreso de dato
palabra = input("Ingrese una palabra: ")

if palabra[-1] in ('aeiouAEIOU'):
    print(f"{palabra}"+ "!")
else:
    print(palabra)

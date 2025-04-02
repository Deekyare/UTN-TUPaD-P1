# 10) Utilizando la información aportada en la tabla sobre las estaciones del año:

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

print("\nActividad 10\n")

# Ingreso de datos
hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ").lower()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    if hemisferio == 'n':
        print("Usted se encuentra en invierno")
    else:
        print("Usted se encuentra en verano")
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    if hemisferio == 'n':
        print("Usted se encuentra en primavera")
    else:
        print("Usted se encuentra en otoño")
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    if hemisferio == 'n':
        print("Usted se encuentra en verano")
    else:
        print("Usted se encuentra en invierno")
else:
    print("Algun dato es invalido.")
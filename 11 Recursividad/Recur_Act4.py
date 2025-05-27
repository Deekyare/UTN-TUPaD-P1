'''Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva 
su representación en binario como una cadena de texto.'''

#Ejemplo de calculo. Convertir 13 a binario: 13 / 2 = 6 (residuo 1), 6 / 2 = 3 (residuo 0), 3 / 2 = 1 (residuo 1), 1 / 2 = 0 (residuo 1)
#10  Debería ser "1010"
#0 Debería ser "0"
#25 Debería ser "11001"
#128 Debería ser "10000000"

#Le pedimos al usuario un número para realizar el calculo
numero_decimal = int(input("Ingrese un número entero positivo: "))


def decimal_a_binario(numero_decimal):
    if numero_decimal == 0:
        return "0"
    elif numero_decimal == 1:
        return "1"
    else:
        # Guardamos en la variable residuo el resto de la division.
        residuo = numero_decimal % 2
        # Guardamos en la variable cociente, el resultado de la division.
        cociente = numero_decimal // 2
        # Concatenamos los valores de ambas variables, que formarán el número binario.
        # Debemos transformar el numero a str, ya que de lo contrario sumaría ambas variables, y no es lo buscado.
        return decimal_a_binario(cociente) + str(residuo)
#Imprimimos el resultado obtenido
print(f"El número decimal {numero_decimal} en binario es equivalente a {decimal_a_binario(numero_decimal)}")

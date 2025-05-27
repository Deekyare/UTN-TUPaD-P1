'''Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva
la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión. Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4) suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)'''

#Le pedimos al usuario un número para realizar el calculo
numero = int(input("Ingrese un número entero positivo: "))

def suma_digitos (numero):
    #Caso base
    if numero == 0:
        return 0
    # Obtenemos el último dígito.
    ultimo_digito = numero % 10  # Por ejemplo, si numero=123, ultimo_digito=3
    
    # Obtenemos el resto del número (sin el último dígito).
    # Por ejemplo, numero=123, ya sacamos el 3, numeros_restantes=12
    numeros_restantes = numero // 10 
    
    # Sumamos el último dígito a la suma de los dígitos del resto del número.
    return ultimo_digito + suma_digitos(numeros_restantes)
    
print(f"La de los digitos ingresados es {suma_digitos(numero)}")
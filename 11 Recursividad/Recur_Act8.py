"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
y un dígito (entre 0 y 9), 
y devuelva cuántas veces aparece ese dígito dentro del número.
Ejemplos: contar_digito(12233421, 2) → 3 contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0 """

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un digito a buscar: "))
contador = 0

def contar_digito(numero, digito_buscado):
    # Condición Base
    if numero == 0:
        return 0
    
    #Obtener el último dígito del número actual.
    ultimo_digito = numero % 10
    
    # Verificar si el último dígito es el que estamos buscando.
    # Si lo es, sumamos 1 
    conteo_actual = 0
    if ultimo_digito == digito_buscado:
        conteo_actual = 1
    
    resto_del_numero = numero // 10
    return conteo_actual + contar_digito(resto_del_numero, digito_buscado)

print(f"Hay {contar_digito(numero, digito)},'{digito}'en el número {numero}") 

'''
Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). 
Prueba esta función en un algoritmo general.'''

numero = int(input("Introduce un número entero positivo: "))
exponente = int(input("Introduce un número para el exponente: "))

# formula: numero ** exponente = n*n(m-1)
#Un número elevado a la potencia 0 es 1

# Definimos la función recursiva para calcular la potencia
def potencia(num_base, exponente):
    if exponente == 0:
        return 1
    else:
        return num_base * potencia(num_base, exponente - 1)
    


# Mostramos el resultado de la potencia   
print(f"La potencia es: {potencia(numero, exponente)}")
    
              
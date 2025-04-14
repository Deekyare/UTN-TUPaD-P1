""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. """


#Inicializamos las variable número1 y numero2 con un dato ingresado por el usuario.
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
#La variable numeros, irá guardando en cada iteración cada numéro entre los ingresados
numeros = 0
#Con un for recorreremos los números entre numero y numero y los iremos sumando en cada vuelta
for i in range(numero1+1, numero2):
    numeros += i
    print(i)
    
#Mostramos el resultado
print(f"La suma de los números comprendidos entre los dos valores ingresados, excluyendolos es: {suma}")

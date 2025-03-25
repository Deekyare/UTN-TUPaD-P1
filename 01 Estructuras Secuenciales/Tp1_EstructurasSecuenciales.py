# Actividades: Estructuras secuenciales.
# Alumna: Giardini Silvia


# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print('-----------Actividad 1 - Mensaje -----------')

print('Hola mundo!')

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
#    Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.
#    Consejo: esto será más sencillo si utilizas print(f...) para realizar la impresión por pantalla.

print('-----------Actividad 2 - Saludo -----------')

nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}')


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla
#     una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
#     el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
#    Consejo: esto será más sencillo si utilizas print(f...) para realizar la impresión por pantalla.

print('-----------Actividad 3 - Datos -----------')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
residencia = input('Ingrese su lugar de residencia: ')
print(f'Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}.')


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

print('-----------Actividad 4 - Área y Perímetro -----------')

radio = int(input('Ingrese el radio de un circulo: '))
pi = 3.14
area = pi*(radio ** 2 )
perimetro = 2 * pi * radio
print(f'Un circulo con un radio de {radio} cm, tiene un area de {area} cm y un perimetro de {perimetro: .2f} cm.')


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

print('-----------Actividad 5 - De segundos a horas -----------')

segundos = float(input('Ingrese la cantidad de segundos a calcular: ')) 
horas = segundos / 3600  
print(f'{segundos} segundos equivalen a {horas} horas.')


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

print('-----------Actividad 6 - Tablas de multiplicar -----------')

num = int(input('Ingrese un número: ')) 

for i in range(1,11):
    resultado = num * i
    print(f'{num} * {i} = {resultado}')


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos,
#  dividirlos, multiplicarlos y restarlos.

print('-----------Actividad 7 - Cálculos -----------')
num1 = int(input('Ingrese el primer número distinto de 0: ')) 
num2 = int(input('Ingrese el segundo número distinto de 0: ')) 
if num1 == 0 or num2 == 0:
    print("Ningún número puede ser 0.")
else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2 
    division = num1 / num2
    print(f'Los resultados de los cálculos con {num1} y {num2} son: suma {suma}, resta {resta}, multiplicación {multiplicacion}, división {division}')

 
# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
#  Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

print('-----------Actividad 8 - IMC -----------')
altura = float(input('Ingrese su altura en cm: ')) 
peso = float(input('Ingrese su peso en kilos: ')) 
if altura <= 0 or peso <= 0:
    print("La altura y el peso deben ser mayores que 0.")
else:
    imc = peso / (altura ** 2)
    print(f'Su Índice de Masa Corporal es {imc: .2f}')


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados
#  Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎h𝑟𝑒𝑛h𝑒𝑖𝑡 = 95 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

print('-----------Actividad 9 - Temperatura -----------')
celsius = float(input('Ingrese la temperatura en grados Celcius: ')) 
 
fahrenheit = (9/5) * celsius + 32
print(f'{celsius} grados Celsius, equivalen a {fahrenheit} grados farenheit')


# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print('-----------Actividad 10 - Promedio -----------')
num1 = float(input('Ingrese el primer número: ')) 
num2 = float(input('Ingrese el segundo número: ')) 
num3 = float(input('Ingrese el tercer número: ')) 
 
promedio = (num1+num2+num3)/3
print(f'El promedio entre los tres números es: {promedio:.2f}')
print('---------------------------------')
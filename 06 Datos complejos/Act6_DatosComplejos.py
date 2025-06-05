""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno. """

# Solicitamos nombre del alumno
alumno = input("Ingrese el nombre del alumno 1: ")
# Creamos una lista vacia, donde se guardaran las notas ingresadas
notaAlum1 = []
# Con un bucle for, vamos guardando nota a nota en la lista anterior
for _ in range (3):
    nota = int(input("Ingresa una nota: "))
    notaAlum1.append(nota)
# Transformamos la lista en una tupla
alum1tupla = tuple(notaAlum1)
# Mostramos por pantalla la tupla para corroborar su creación
print(alum1tupla)

alumno2 = input("Ingrese el nombre del alumno 2: ")
notaAlum2 = []
for _ in range (3):
    nota = int(input("Ingresa una nota: "))
    notaAlum2.append(nota)
alum2tupla = tuple(notaAlum2)
print(alum2tupla)

alumno3 = input("Ingrese el nombre del alumno 3: ")
notaAlum3 = []
for _ in range (3):
    nota = int(input("Ingresa una nota: "))
    notaAlum3.append(nota)
alum3tupla = tuple(notaAlum3)
print(alum3tupla)

#Promedios

print ("--- Promedios ---")
#Sum(tupla) suma los elementos dento de la tupla, luego los dividimos en 3
print(f"El promedio del alumno 1 '{alumno}' es: {(sum(alum1tupla)/3)}")
print(f"El promedio del alumno 2 '{alumno2}' es: {(sum(alum2tupla)/3)}")
print(f"El promedio del alumno 3 '{alumno3}' es: {(sum(alum3tupla)/3)}")
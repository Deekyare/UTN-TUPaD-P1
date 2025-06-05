""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800 """

# Creamos el diccionario con los datos proporcionados
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregamos al diccionario anterior los siguientes elementos
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Imprimimos por pantalla el resultado
print(precios_frutas)

# Actualización de valores
print("-- Precios actualizado --")
precios_frutas['Banana'] = 1300
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
# Imprimimos por pantalla el resultado
print(precios_frutas)

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado
en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. """
# Lista de frutas sin precios. Solo se mostrará la clave, sin el valor.
lista_frutas = (list(precios_frutas.keys()))
print(" -- Lista de frutas -- ")
print(lista_frutas)


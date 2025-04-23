""" Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
    Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar
    cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"] """

#Inicialización de la variable "animales" con una lista.
animales = ["perro", "gato", "conejo", "pez"]

#Imprimimos la lista original
print(animales)

#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”
animales[2] = "loro"
animales[3] = "oso"

#Reemplazo usando indexing
# animales[-2] = "loro"
# Segunda forma
# animales[-1] = "oso"

#Imprimimos la lista con los núevos valores en el último y antepeúltimo lugar
print(animales)

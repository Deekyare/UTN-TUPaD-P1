""" Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
    y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado 
    usando esta función. """
    
# Variable para guardar los segundos ingresados por el usuario
segundos = int(input("Ingrese la cantidad de segundos a convertir: "))

#Función para saber cuantas horas hay en determinados segundos
def segundos_a_horas(segundos):
    #El número de segundos en una hora 3600. Usamos // para tener la parte entera del resultado
    horas = segundos // 3600
    input(f"\n{segundos} segundos equivalen a: {horas} hora/s")
    
#Llamar a la funcione
segundos_a_horas(segundos)
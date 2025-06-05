""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
 • Las capitales sean las claves.
• Los países sean los valores.
 """
 
 # Dic: Países:claves, capitales:valores
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'España': 'Madrid',
    'Francia': 'París',
    'Alemania': 'Berlín',
    'Italia': 'Roma',
  
}

print("--- Diccionario (País: Capital) ---")
print(paises_capitales)

# Construimos el nuevo diccionario
capitales_paises = {}

# Recorremos el diccionario original
# item() nos da tuplas (clave, valor) del diccionario original
for pais, capital in paises_capitales.items():
    # Asignamos la capital como nueva clave y el país como nuevo valor
    capitales_paises[capital] = pais

print("\n--- Nuevo Diccionario (Capital: País) ---")
print(capitales_paises)
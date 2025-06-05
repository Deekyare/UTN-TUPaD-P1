"""  8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
 • Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. """

# Diccionario
tecnologia = {'celulares': 1200, 'televisores': 100, 'chromecast': 30, 'laptops': 1000}

print("--- Menu ---")

# Inicializamos la opción para que el bucle comience
opcion = ""

# Usamos un bucle while True para que el menú se muestre hasta que el usuario elija salir
while True:
    print("\n--- Menú ---")
    print("1- Ver stock de un producto")
    print("2- Agregar stock a un producto existente")
    print("3- Agregar un nuevo producto")
    print("4- Salir")

    # Pedimos al usuario que ingrese una opción
    opcion = input("Ingrese una opción (1-4): ")

    # Según cada opción
    if opcion == '1':
        print("\n--- Productos Disponibles ---")
        # Mostrar las claves (nombres de productos) para que el usuario sepa qué puede consultar
        for producto in tecnologia.keys():
            print(f"- {producto}")

        consulta = input("Ingrese el nombre del producto que desea consultar: ").lower() # Convertir a minúsculas para coincidir

        if consulta in tecnologia:
            print(f"El stock de '{consulta}' es: {tecnologia[consulta]} unidades.")
        else:
            print(f"Lo siento, el producto '{consulta}' no se encuentra en el inventario.")

    elif opcion == '2':
        print("\n--- Agregar Stock ---")
        # Mostrar productos existentes para ayudar al usuario
        print("Productos actuales:", list(tecnologia.keys()))
        producto_a_modificar = input("Ingrese el nombre del producto al que desea agregar stock: ").lower()

        if producto_a_modificar in tecnologia:
            try:
                cantidad = int(input(f"Ingrese la cantidad a agregar a '{producto_a_modificar}': "))
                if cantidad > 0:
                    tecnologia[producto_a_modificar] += cantidad
                    print(f"Se agregaron {cantidad} unidades a '{producto_a_modificar}'. Nuevo stock: {tecnologia[producto_a_modificar]}.")
                else:
                    print("La cantidad a agregar debe ser un número positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")
        else:
            print(f"El producto '{producto_a_modificar}' no existe. Use la opción 3 para agregarlo como nuevo.")

    elif opcion == '3':
        print("\n--- Agregar Nuevo Producto ---")
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ").lower()

        if nuevo_producto in tecnologia:
            print(f"El producto '{nuevo_producto}' ya existe. Use la opción 2 para agregar stock.")
        else:
            try:
                stock_inicial = int(input(f"Ingrese el stock inicial para '{nuevo_producto}': "))
                if stock_inicial >= 0: # El stock inicial puede ser 0
                    tecnologia[nuevo_producto] = stock_inicial
                    print(f"El producto '{nuevo_producto}' fue agregado con un stock inicial de {stock_inicial} unidades.")
                else:
                    print("El stock inicial no puede ser negativo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para el stock.")

    elif opcion == '4':
        print("Saliendo del programa.")
        break # Salimos del bucle while

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
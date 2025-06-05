""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
     Permití consultar qué actividad hay en cierto día y hora.
"""
# Inicializamos nuestra agenda vacía
agenda = {}

# Agregamos algunos eventos de ejemplo, ahora usando nombres de días
# Las claves son tuplas (nombre_del_dia, hora) y los valores son los eventos
agenda[("lunes", 9)] = "Clse de matemáticas"
agenda[("lunes", 14)] = "Presentación de Tp"
agenda[("martes", 10)] = "Clase de Python"
agenda[("miércoles", 18)] = "Hora de descanso"


print("--- Mi Agenda ---")
print("Eventos actuales en la agenda:")
# Iteramos para mostrar los eventos, con el día en formato de texto
for (dia_str, hora), evento in agenda.items():
    print(f"{dia_str.capitalize()}, {hora:02d}:00 hs -> {evento}") # .capitalize() para que el día se vea bien

# --- Funcionalidad para consultar una actividad ---
print("\n--- Consultar Actividad ---")

while True:
    try:
        # Pedimos el día como una cadena de texto y la convertimos a minúsculas
        dia_consulta_str = input("Ingrese el día que desea consultar (ej. lunes, martes): ").lower()
        
        hora_consulta = int(input("Ingrese la hora que desea consultar (formato 24hs, sin minutos): "))

        # Creamos la tupla clave para la consulta, ahora con el nombre del día
        clave_consulta = (dia_consulta_str, hora_consulta)

        # Verificamos si la clave (día_str, hora) existe en nuestra agenda
        if clave_consulta in agenda:
            # Si existe, mostramos el evento asociado
            print(f"\nEl {dia_consulta_str.capitalize()}, a las {hora_consulta:02d}:00 hs, la actividad es: '{agenda[clave_consulta]}'")
        else:
            # Si no existe, no hay actividad programada para ese momento
            print(f"\nNo hay actividad programada para el {dia_consulta_str.capitalize()}, a las {hora_consulta:02d}:00 hs.")

        continuar = input("\n¿Desea consultar otra actividad? (s/n): ").lower()
        if continuar != 's':
            break # Salimos del bucle si el usuario no quiere continuar

    except ValueError:
        print("Entrada inválida. Por favor, asegúrese de ingresar el día como texto y la hora como un número entero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
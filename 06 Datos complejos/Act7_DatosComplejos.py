""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:

• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""
  
parcial1 = {10,7,6,8}
parcial2 = {5,7,9,10}

# Estudiantes que aprobaron ambos parciales. Interseccion
aprobados_ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", aprobados_ambos)

# Estudiantes que aprobaron solo uno de los dos. Diferencia simétrica
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# Lista total de estudiantes que aprobaron al menos un parcial (sin repetir). Unión
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)
        
    

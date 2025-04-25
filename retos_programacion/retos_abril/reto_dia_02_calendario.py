# Tu misión es simple, soldado: crear un calendario que muestre todos los meses del año y sus semanas de forma clara y organizada.
# Nada de efectos especiales ni complicaciones innecesarias, solo un buen código que haga el trabajo. Crea un programa que:
# Itere los meses del año
# Itere las semanas del mes

# PISTA: Bucle for anidado.

# --Ejemplo:
# Enero
# Semana 1
# Semana 2
# Semana 3
# …

meses_anio = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
    "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] # definimos los meses del año
dias_mes = 0
dias_anio = 2 # el día del año empieza en 2 porque 2025 comienza en miércoles
dias_semana = 2 # al igual que el año, la primera semana comienza en miércoles
num_semana = 0

print("\n** Calendario 2025 **") # imprimimos el año
for i in range(12): # bucle que recorre los 12 meses

    if i == 1: # definimos los días para febrero (28 porque 2025 no es bisiesto)
        dias_mes = 28
    elif i == 3 or i == 5 or i == 8 or i == 10: # para los meses de 30 días
        dias_mes = 30
    else: # para el resto que son los de 31 días
        dias_mes = 31

    print("\n", meses_anio[i]) # imprimimos el nombre del mes

    for j in range(dias_semana, 0, -1): # imprimimos guiones "-" para los días de la semana que no son de este mes
        print("-".ljust(4), end="")

    for k in range(1, dias_mes+1): # bucle que recorre los días de cada mes
        print(f"{k}".ljust(4), end="") # imprimimos el número del día
        dias_anio += 1

        if dias_anio % 7 == 0: # cada 7 días imprimimos la semana y un salto de línea
            num_semana += 1
            print(f"Semana {num_semana}")
    
    dias_semana = dias_anio % 7 # recalculamos el número de días de la semana que hay recorridos ya antes de empezar el nuevo mes
    print("") # separación entre los meses
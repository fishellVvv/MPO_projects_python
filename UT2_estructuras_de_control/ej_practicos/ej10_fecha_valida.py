# Ejercicio 10

# Escribe un programa que pida día, mes y año.
# Comprueba si la fecha introducida es válida.
# Recuerda que, en los años bisiestos, febrero tiene 29 días.
# Puedes usar el algoritmo del ejercicio 6 para determinar si un año es bisiesto.

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes (entre 1 y 12): "))
año = int(input("Introduce el año: "))

if mes in [1, 3, 5, 7, 8, 10, 12] and 1 <= dia <= 31:
    print(f"la fecha {dia}/{mes}/{año} es válida.")
elif mes in [4, 6, 9, 11] and 1 <= dia <= 30:
    print(f"la fecha {dia}/{mes}/{año} es válida.")
elif mes == 2 and 1 <= dia <= 28:
    print(f"la fecha {dia}/{mes}/{año} es válida.")
elif mes == 2 and dia == 29:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"la fecha {dia}/{mes}/{año} es válida.")
    else:
        print(f"la fecha {dia}/{mes}/{año} no es válida.")
else:
    print(f"la fecha {dia}/{mes}/{año} no es válida.")
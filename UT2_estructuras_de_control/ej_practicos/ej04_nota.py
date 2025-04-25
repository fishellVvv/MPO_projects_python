# Ejercicio 4

# Escribe un programa que pida una nota (0-10) y muestre:
# "Suspenso" si es menor de 5
# "Aprobado" si es entre 5 y 6
# "Notable" si es entre 7 y 8
# "Sobresaliente" si es 9 o 10

nota = float(input("Introduce una nota (0-10): "))

if nota < 5:
    print("Suspenso")
elif 5 <= nota < 7:
    print("Aprobado")
elif 7 <= nota < 9:
    print("Notable")
elif 9 <= nota <= 10:
    print("Sobresaliente")
else:
    print("Nota no válida. Debe estar entre 0 y 10.")
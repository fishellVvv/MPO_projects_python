# Ejercicio 2 - Contador de números pares

# Escribe un programa que pida al usuario un número entero positivo y cuente
#   cuántos números pares hay desde 0 hasta ese número (incluido).
# El programa debe imprimir el resultado.

numero = int(input("Introduce un número entero positivo: "))
pares = 0
for i in range(0, numero+1, 2):
    pares += 1
print("Hay", pares, "pares desde 0 hasta", numero, "(contando 0)")
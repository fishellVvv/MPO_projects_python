# Ejercicio 13

# Escribe un programa que pida al usuario un número entero positivo e imprima la tabla de multiplicar de ese número (del 1 al 10).

numero = int(input("Escribe un numero entero: "))
for i in range(1, 11):
    print(f"{numero} x {1} = {numero * i}")
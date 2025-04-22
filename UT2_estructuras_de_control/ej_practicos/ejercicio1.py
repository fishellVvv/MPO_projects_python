# Ejercicio 1

# Escribe un programa que pida al usuario un número entero y determine si es par o impar.
# El programa debe imprimir un mensaje indicando el resultado.

num = int(input("Introduce un número entero: "))

if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
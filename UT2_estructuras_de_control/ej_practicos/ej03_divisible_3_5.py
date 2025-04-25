# Ejercicio 3

# Escribe un programa que pida al usuario un número entero y determine si es divisible por 3 y 5.
# El programa debe imprimir un mensaje indicando el resultado.

num = int(input("Introduce un número entero: "))

if num % 3 == 0 and num % 5 == 0:
    print("El número es divisible por 3 y 5.")
else:
    print("El número no es divisible por 3 y 5.")
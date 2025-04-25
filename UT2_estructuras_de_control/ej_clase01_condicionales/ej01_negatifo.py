# Ejercicio 1 - Siempre negatifo, nunca positifo

# Escribe un programa que pida al usuario un número entero y determine si es positivo o negativo.
# El programa debe imprimir un mensaje indicando el resultado.

num = int(input("Introduce un número entero: "))

if num >= 0:
    print("El número es positivo.")
else:
    print("El número es negativo.")
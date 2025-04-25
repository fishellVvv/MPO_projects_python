# Ejercicio 4 - Factorial

# Escribe un programa que pida al usuario un número entero positivo y calcule su factorial.
# El programa debe imprimir el resultado.
# El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.

numero = int(input("Escribe un numero entero positivo: "))
factorial = 1
for i in range(numero, 1, -1):
    factorial *= i
print ("El factorial de", numero, "es", factorial)
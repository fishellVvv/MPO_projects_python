# Ejercicio 15

# Escribe un programa que pida al usuario un número entero positivo 
#   y calcules la suma de la potencia de 3 de cada número desde 1 hasta el número introducido.
# El programa debe imprimir el resultado.

# Para que se entienda mejor, si el usuario introduce 3, el programa debe calcular:
# 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36

numero = int(input("Escribe un número entero positivo: "))
potencia3 = 0
for i in range(1, numero+1):
    potencia3 += i ** 3
print(f"La suma de la potencia de 3 de cada número desde 1 hasta {numero} es: {potencia3}")
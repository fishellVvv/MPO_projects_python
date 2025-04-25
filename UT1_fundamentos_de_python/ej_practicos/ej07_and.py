# Ejercicio 7

# Escribe un programa que pida al usuario tres números enteros e imprima True si todos ellos son mayores que cero, False en caso contrario.

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
num3 = int(input("Introduce el tercer número entero: "))

print(num1 > 0 and num2 > 0 and num3 > 0)
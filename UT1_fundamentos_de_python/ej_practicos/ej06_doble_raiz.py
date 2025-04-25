# Ejercicio 6

# Escribe un programa que pida al usuario un número entero e imprima:
# Su doble
# Su triple
# Su mitad
# Su cuadrado
# Su raíz cuadrada

import math

num = int(input("Introduce un número entero: "))
print(f"Su doble es: {num * 2}")
print(f"Su triple es: {num * 3}")
print(f"Su mitad es: {num / 2}")
print(f"Su cuadrado es: {num ** 2}")
print(f"Su raíz cuadrada es: {math.sqrt(num)}")
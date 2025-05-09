'''
Ejercicio 10 - Akinator numérico

Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número.
El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido.
El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto.
'''

import random
num_secreto = random.randint(1, 100)

num_usuario = int(input("Adivina el número (1, 100):\n"))
intentos = 1

while num_usuario != num_secreto:
    if num_usuario > num_secreto:
        print("te has pasado, es menor...")
    else:
        print("te has quedado corto, es mayor...")
    num_usuario = int(input())
    intentos += 1

print(f"¡Correcto!, lo has adivinado en {intentos} intentos.")
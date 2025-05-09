'''
Ejercicio 20

Escribe un programa que dado una serie de números introducidos por el usuario,
    hasta que introduzca un -1, cuente cuántos de estos números son pares y cuántos son impares.
El programa debe imprimir el número de pares e impares introducidos, menos el -1.
'''

num = int(input("Introduce numeros enteros (-1 para terminar):\n"))
pares = 0
impares = 0

while num != -1:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    num = int(input())

if pares == 0 and impares == 0:
    print("No has introducido ningún número.")
else:
    print(f"Has introducido {pares} pares y {impares} impares.")
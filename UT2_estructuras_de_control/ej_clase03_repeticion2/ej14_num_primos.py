'''
Ejercicio 14 - Números primos

Escribe un programa que pida al usuario un número entero positivo y determine si es primo o no.
Un número primo es aquel que solo es divisible por 1 y por sí mismo.
El programa debe imprimir el resultado.
'''

num = int(input("Introduce un numero entero positivo: "))
primo = True

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
else:
    primo = False

if num >= 0:
    if primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
else:
    print("El numero debe ser positivo")
'''
Ejercicio 16 - Números perfectos

Escribe un programa que pida al usuario un número entero positivo y determine si es un número perfecto o no.
Un número perfecto es aquel que es igual a la suma de sus divsuma_div propios (excluyendo el propio número).
Por ejemplo, 6 es un número perfecto porque sus divsuma_div son 1, 2 y 3, y 1 + 2 + 3 = 6.
'''

num = int(input("Introduce un numero entero positivo: "))

if num <= 0:
    print("El número debe ser positivo.")
else:
    suma_div = 0

    for i in range(1, (num // 2) + 1):
            if num % i == 0:
                suma_div += i
                
    if suma_div == num:
        print(f"{num} es un número perfecto.")
    else:
        print(f"{num} no es un número perfecto.")
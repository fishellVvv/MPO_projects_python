'''
Ejercicio 17 - Conversión binaria

Escribe un programa que pida al usuario un número entero positivo y lo convierta a su representación binaria.
El programa debe imprimir el resultado en forma de cadena de caracteres.
'''

num = int(input("Introduce un número entero positivo: "))

if num < 0:
    print("El número debe ser entero positivo.")
elif num == 0:
    print("0")
else:
    binario = ""
    num_2 = num
    while num_2 > 0:
        binario = str(num_2 % 2) + binario
        num_2 //= 2

    print(binario)
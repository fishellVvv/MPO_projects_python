'''
Ejercicio 13 - Número de cifras

Escribe un programa que pida al usuario una serie de números enteros positivos
    hasta la introducción de un valor -1 para cada número debe contar cuántas cifras tiene.
El programa debe imprimir la longitud de cada número.
No podéis usar la función len() para contar las cifras ni convertir el número a cadena.
'''

numero = int(input("Introduce un numero entero positivo (-1 para terminar)\nn: "))

while numero >= 0:
    digitos = 1
    num_calculo = numero

    while num_calculo >= 10:
        num_calculo //= 10
        digitos += 1

    numero = int(input(f"El número {numero} tiene {digitos} cifras\nn: "))

if numero < -1:
    print("Error, el número debe ser positivo.")
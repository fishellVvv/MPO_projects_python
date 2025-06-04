'''
Ejercicio 1 - Sumar elementos de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas
    y calcule la suma de todos los elementos de la lista.
El programa debe imprimir el resultado.
'''

lista_numeros = input("Introduce una lista de números enteros separados por comas:\n").split(",")
resultado = 0

for num in lista_numeros:
    resultado += int(num)

print(f"Resultado suma: {resultado}")
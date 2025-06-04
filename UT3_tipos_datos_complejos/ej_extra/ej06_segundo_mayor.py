'''
Ejercicio 6 - Encontrar el segundo valor más grande en una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas.
El programa debe encontrar el segundo valor más grande en la lista y luego imprimirlo.
Si no hay un segundo valor más grande, el programa debe imprimir un mensaje indicando que no se encontró.
Se asegura que la lista no contiene duplicados.
'''

lista_numeros = input("Introduce una lista de números enteros separados por comas:\n").split(",")
lista_numeros = [int(num) for num in lista_numeros]
lista_numeros.sort()

if len(lista_numeros) < 2:
    print("No se encontró un segundo valor más grande.")
else:
    print("El segundo valor más grande es:", lista_numeros[-2])
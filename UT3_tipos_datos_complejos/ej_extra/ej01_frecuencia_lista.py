'''
Ejercicio 1 - Contar la frecuencia de un número en una lista

Escribe un programa que pida al usuario una lista de números enteros separados por espacios y un número entero.
El programa debe contar cuántas veces aparece el número en la lista y luego imprimir el resultado.
'''

lista_numeros = input("Introduce una lista de números enteros separados por espacios:\n").split()
lista_numeros = [int(num) for num in lista_numeros]
numero = int(input("Introduce un número entero: "))

contador = lista_numeros.count(numero)

print(f"El número {numero} aparece {contador} veces en la lista.")
'''
Ejercicio 3 - Filtrar elementos de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas y 
    filtre los números pares de la lista.
El programa debe imprimir la lista de números pares.
'''

lista_numeros = input("Introduce una lista de números enteros separados por espacios:\n").split()
lista_numeros = [int(num) for num in lista_numeros]
numeros_pares = []

for num in lista_numeros:
    if num % 2 == 0 : numeros_pares.append(num)

print(f"Los números pares de tu lista son: {numeros_pares}")
'''
Ejercicio 8 - Eliminar elementos duplicados de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas.
El programa debe eliminar los elementos duplicados de la lista y luego imprimir la lista resultante.
'''

lista_numeros = input("Introduce una lista de números enteros separados por comas:\n").split(",")
lista_numeros = [int(num) for num in lista_numeros]
lista_sin_duplicados = []

for num in lista_numeros:
    if num not in lista_sin_duplicados:
        lista_sin_duplicados.append(num)

print(f"La lista sin duplicados es: {lista_sin_duplicados}")
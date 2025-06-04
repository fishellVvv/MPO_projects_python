'''
Ejercicio 7 - Eliminar elementos duplicados consecutivos de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas.
El programa debe eliminar los elementos duplicados consecutivos de la lista y luego imprimir la lista resultante.
'''

lista_numeros = input("Introduce una lista de números enteros separados por comas:\n").split(",")
lista_numeros = [int(num) for num in lista_numeros]
lista_sin_duplicados = []

for i in range(len(lista_numeros)):
    if i == 0 or lista_numeros[i] != lista_numeros[i-1]:
        lista_sin_duplicados.append(lista_numeros[i])

print(f"La lista sin duplicados es: {lista_sin_duplicados}")
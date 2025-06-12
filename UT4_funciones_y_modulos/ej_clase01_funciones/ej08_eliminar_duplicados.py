'''
Ejercicio 8 - Eliminar elementos duplicados de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas.
El programa debe definir una función que reciba la lista, elimine los elementos duplicados
    y luego imprima la lista resultante.
'''

def eliminar_duplicados(lista_num):
    """DevulDevuelve una lista sin duplicados"""
    lista_ordenada = sorted(lista_num)
    lista_unicos = []
    for i in range(len(lista_ordenada)):
        if lista_ordenada[i] != lista_ordenada[i-1]:
            lista_unicos.append(lista_ordenada[i])
    return lista_unicos

print("Eliminar elementos duplicados de una lista.")
lista_numeros = input("Introduce una lista de números enteros separados por comas: ").split(",")
lista_numeros = [int(num) for num in lista_numeros]

print(f"La lista sin duplicados es {eliminar_duplicados(lista_numeros)}.")

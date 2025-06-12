'''
Ejercicio 6 - Encontrar el máximo y mínimo de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas.
El programa debe definir una función que reciba la lista, encuentre el máximo y el mínimo de la lista
    y luego imprima ambos resultados.
'''

def encontrar_min_max(lista_num):
    """Devuelve los valores minimo y máximo de un lista de numeros enteros"""
    minimo = sorted(lista_num)[0]
    maximo = sorted(lista_num)[-1]
    return minimo, maximo

print("Encontrar el máximo y mínimo de una lista.")
lista_numeros = input("Introduce una lista de números enteros separados por comas: ").split(",")
lista_numeros = [int(num) for num in lista_numeros]

minimo, maximo = encontrar_min_max(lista_numeros)
print(f"El valor mínimo es {minimo} y el máximo es {maximo}.")

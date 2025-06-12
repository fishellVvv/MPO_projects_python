'''
Ejercicio 7 - Incrementar cada elemento de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas y un número entero.
El programa debe definir una función que reciba la lista y el número, incremente cada elemento de la lista por
    el número dado y luego imprima la lista resultante.
'''

def incrementar_elementos_lista(lista_num, num):
    """Devuelve una lista incrementada en cada elemento por el número dado"""
    for i in range(len(lista_num)):
        lista_num[i] += num
    return lista_num

print("Incrementar cada elemento de una lista.")
lista_numeros = input("Introduce una lista de números enteros separados por comas: ").split(",")
lista_numeros = [int(num) for num in lista_numeros]
numero = int(input("Introduce un numero entero: "))

print(f"La lista incrementada en {numero} es {incrementar_elementos_lista(lista_numeros, numero)}.")

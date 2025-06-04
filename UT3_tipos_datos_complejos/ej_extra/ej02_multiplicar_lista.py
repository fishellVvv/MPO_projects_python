'''
Ejercicio 2 - Multiplicar todos los elementos de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por espacios y un número entero.
El programa debe multiplicar todos los elementos de la lista por el número dado y luego imprimir la lista resultante.
'''

lista_numeros = input("Introduce una lista de números enteros separados por espacios:\n").split()
lista_numeros = [int(num) for num in lista_numeros]
numero = int(input("Introduce un número entero: "))

for i in range(len(lista_numeros)):
    lista_numeros[i] *= numero

print(f"Tu lista multiplicada por {numero} es:\n{lista_numeros}")
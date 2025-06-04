'''
Ejercicio 5 - Eliminar todos los elementos de una lista que sean mayores a un número dado

Escribe un programa que pida al usuario una lista de números enteros separados por comas y un número entero.
El programa debe eliminar todos los elementos de la lista que sean mayores al número dado y luego imprimir la lista resultante.
'''

lista_numeros = input("Introduce una lista de números enteros separados por comas:\n").split(",")
lista_numeros = [int(num) for num in lista_numeros]
numero = int(input("Introduce un número entero: "))

for num in lista_numeros:
    if numero < num : lista_numeros.remove(num)

print(f"Los números menores o iguales a {numero} son: {lista_numeros}")
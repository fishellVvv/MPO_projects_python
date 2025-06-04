'''
Ejercicio 5 - Invertir una lista

Escribe un programa que pida al usuario una lista de números enteros 
    separados por espacios y la invierta. 
El programa debe imprimir la lista invertida.
'''

lista_numeros = input("Introduce una lista de números enteros separados por espacios:\n").split()
# lista_numeros.reverse()
lista_reversa = []

for i in range(len(lista_numeros)):
    lista_reversa.append(lista_numeros.pop())

print(f"Lista invertida: {lista_reversa}")
'''
Ejercicio 3 - Mayor y menor elemento de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas 
    y encuentre el mayor y el menor elemento de la lista.
El programa debe imprimir ambos resultados.
'''

lista_numeros = input("Introduce una lista de números enteros separados por comas:\n").split(",")
# lista_numeros = [int(num) for num in lista_numeros]
# print(f"Valor mínimo: {min(lista_numeros)}\nValor máximo: {max(lista_numeros)}")
minimo = float('inf')
maximo = float('-inf')

for num in lista_numeros:
    if (int(num) < minimo): minimo = int(num)
    if (int(num) > maximo): maximo = int(num)

print(f"Valor mínimo: {minimo}\nValor máximo: {maximo}")
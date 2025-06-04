'''
Ejercicio 4 - Sumar dos listas de diferente longitud

Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos de ambas listas.
Si las listas no tienen la misma longitud, el programa debe sumar los elementos de la lista más corta con los elementos 
    correspondientes de la lista más larga y el resto de los elementos de la lista más larga deben ser sumados a cero.
El programa debe imprimir la lista resultante.
'''

lista_numeros1 = input("Introduce una lista de números enteros separados por comas:\n").split(",")
lista_numeros1 = [int(num) for num in lista_numeros1]
lista_numeros2 = input("Introduce otra lista de números enteros separados por comas:\n").split(",")
lista_numeros2 = [int(num) for num in lista_numeros2]
suma_listas = []

max_long = max(len(lista_numeros1), len(lista_numeros2))

for i in range(max_long):
    num1 = lista_numeros1[i] if i < len(lista_numeros1) else 0
    num2 = lista_numeros2[i] if i < len(lista_numeros2) else 0
    suma_listas.append(num1 + num2)

print(f"La suma de tus listas es: {suma_listas}")
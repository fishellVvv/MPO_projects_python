'''
Ejercicio 4 - Sumar dos listas de igual longitud

Escribe un programa que pida al usuario dos listas de números enteros separados por comas 
    y sume los elementos de ambas listas.
El programa debe imprimir la lista resultante.
Si las listas no tienen la misma longitud, el programa debe imprimir un mensaje de error.
'''

lista_numeros1 = input("Introduce una lista de números enteros separados por comas:\n").split(",")
lista_numeros2 = input("Introduce otra lista de números enteros separados por comas:\n").split(",")

if len(lista_numeros1) != len(lista_numeros2):
    print("La longitud de las listas no es la misma")
else:
    lista_suma = []
    for i in range(len(lista_numeros1)):
        lista_suma.append(int(lista_numeros1[i]) + int(lista_numeros2[i]))

    print(f"Resultado de la suma: {lista_suma}")
'''
Ejercicio 4 - Tupla de números

Escribe un programa que pida al usuario una lista de números enteros separados por comas y almacene estos números en una tupla.
Luego, el programa debe calcular y mostrar la suma, el promedio, el número máximo y el número mínimo de la tupla.
'''

numeros = input("Introduce una lista de números separados por comas:\n").split(",")
numeros = [int(num) for num in numeros]
tupla = tuple(numeros)

# print(f"La suma de los números es {sum(tupla)}, el promedio es {sum(tupla)/len(tupla)}, el número máximo es {max(tupla)} y el número mínimo es {min(tupla)}.")

suma = 0
promedio = 0.0
maximo = float('-inf')
minimo = float('inf')

for num in tupla:
    suma += num
    if num > maximo : maximo = num
    if num < minimo : minimo = num
promedio = suma / len(tupla)

print(f"La suma de los números es {suma}, el promedio es {promedio}, el número máximo es {maximo} y el número mínimo es {minimo}.")
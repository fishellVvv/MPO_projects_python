'''
Ejercicio 2 - Contar palabras en un texto

Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece cada palabra en el texto. 
El programa debe imprimir un diccionario donde las claves son las palabras y los valores son sus respectivas frecuencias. 
Ignora la puntuación y considera las palabras en minúsculas.
'''

lista_palabras = input("Introduce un texto: ").lower().split()
diccionario_palabras = {}

for palabra in lista_palabras:
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] += 1
    else:
        diccionario_palabras[palabra] = 1

print(diccionario_palabras)
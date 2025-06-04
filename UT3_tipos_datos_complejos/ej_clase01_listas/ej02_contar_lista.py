'''
Ejercicio 2 - Contar elementos de una lista

Escribe un programa que pida al usuario una lista de palabras separadas por comas
    y cuente cuántas palabras hay en la lista.
El programa debe imprimir el resultado.
'''

# Solución en una linea.
# print("Número de palabras: ", len(input("Introduce una lista de palabras separadas por comas:\n").split(",")))

lista_palabras = input("Introduce una lista de palabras separadas por comas:\n").split(",")
resultado = 0

for palabra in lista_palabras:
    resultado += 1

print(f"Número de palabras: {resultado}")
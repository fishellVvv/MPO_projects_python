'''
Ejercicio 23

Escribe un programa que vaya recibiendo cadenas de texto hasta que el usuario introduzca "fin".
El programa debe contar cuántas vocales se han introducido e imprimir el resultado.
Las vocales son: a, e, i, o, u (tanto mayúsculas como minúsculas).
El programa debe imprimir el número total de vocales introducidas sin contar la palabra "fin".
'''

texto = input("Escribe el texto a analizar (fin para finalizar):\n").lower()
vocales = 0

while texto != "fin":
    for car in texto:
        if car in "aeiou":
            vocales += 1
    texto = input().lower()

print(f"\nNúmero total de vocales: {vocales}")
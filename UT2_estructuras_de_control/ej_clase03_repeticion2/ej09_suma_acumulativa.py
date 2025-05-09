'''
Ejercicio 9 - Suma acumulativa

Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números.
El programa debe seguir pidiendo números hasta que el usuario ingrese un 0.
Al final, imprime la suma total.
'''

suma_num = 0

numero = int(input("Intorduce numeros enteros (0 para terminr): "))

while numero != 0:
    suma_num += numero
    numero = int(input("Intorduce numeros enteros (0 para terminr): "))

print(f"La suma de tus números es {suma_num}")
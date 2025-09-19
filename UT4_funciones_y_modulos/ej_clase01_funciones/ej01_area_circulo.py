'''
Ejercicio 1 - Calcular el área de un círculo

Escribe un programa que pida al usuario el radio de un círculo y calcule su área.
El programa debe definir una función que reciba el valor del radio, realice el cálculo del área y luego imprima el resultado.
'''

import math

def calcular_area_circulo(r):
    """Devuelve el área de un circulo de radio r"""
    area = math.pi * r * r
    return area

print("Calculadora de áreas de círculos.")
radio = float(input("Introduce el rádio de tu círculo: "))
print(f"El area del círculo de radio {radio} es {calcular_area_circulo(radio):.2f}")

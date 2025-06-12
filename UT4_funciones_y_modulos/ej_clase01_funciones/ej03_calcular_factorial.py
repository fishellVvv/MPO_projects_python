'''
Ejercicio 3 - Calcular el factorial de un número

Escribe un programa que pida al usuario un número entero y calcule su factorial.
El programa debe definir una función que reciba el número, realice el cálculo del factorial y luego imprima el resultado.
'''

def calcular_factorial(num):
    """Devuelve el factorial de un número"""
    factorial = 1
    for i in range(num, 1, -1):
        factorial *= i
    return factorial

print("Calcula el factorial.")
numero = int(input("Introduce un número entero positivo: "))
print(f"El factorial de {numero} es {calcular_factorial(numero)}")

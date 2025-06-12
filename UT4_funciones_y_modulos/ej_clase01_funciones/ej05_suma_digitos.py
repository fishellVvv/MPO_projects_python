'''
Ejercicio 5 - Calcular la suma de dígitos de un número

Escribe un programa que pida al usuario un número entero y calcule la suma de sus dígitos.
El programa debe definir una función que reciba el número, realice el cálculo de la suma de los dígitos
    y luego imprima el resultado.
'''

def suma_digitos(num):
    """Devuelve la suma de los dígitos de un número"""
    suma = 0
    while (num > 0):
        suma += num % 10
        num //= 10
    return suma

print("Suma de dígitos.")
numero = int(input("Introduce un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es {suma_digitos(numero)}")

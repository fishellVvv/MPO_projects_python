'''
Ejercicio 4 - Verificar si un número es primo

Escribe un programa que pida al usuario un número entero y verifique si es primo.
El programa debe definir una función que reciba el número, realice la verificación
    y luego imprima si el número es primo o no.
'''

def verificar_primo(num):
    """debuelve un booleano que indica si un numero es primo"""
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
    else:
        return False
    return True

print("Verificador de primos.")
numero = int(input("Introduce un número entero positivo: "))

if numero >= 0:
    if verificar_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
else:
    print("El numero debe ser positivo")

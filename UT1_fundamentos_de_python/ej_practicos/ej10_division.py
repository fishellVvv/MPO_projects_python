# Ejercicio 10

# Escribe un programa que, dados dos números enteros, imprima su división decimal, si división entera y su resto. El segundo número no puede ser cero.

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

if num2 == 0:
    print("El segundo número no puede ser cero.")
else:
    print(f"División decimal: {num1 / num2}")
    print(f"División entera: {num1 // num2}")
    print(f"Resto: {num1 % num2}")
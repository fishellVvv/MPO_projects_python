# Ejercicio 2

# Escribe un programa en Python que pida al usuario dos números y luego imprima la suma, resta, multiplicación y división de ambos números.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
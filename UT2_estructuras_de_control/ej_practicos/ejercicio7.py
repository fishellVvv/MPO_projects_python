# Ejercicio 7

# Escribe un programa que pida dos números y un operador (+, -, *, /) y muestre el resultado de la operación.

num1 = float(input("Intruduce un número: "))
operador = input("Intruduce un operador (+, -, *, /): ")
num2 = float(input("Intruduce otro número: "))

resultado = None

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        mensaje = "Error: División por cero."
else:
    mensaje = "Error: Operador no válido. Debe ser +, -, * o /."

if resultado is not None:
    mensaje = f"El resultado de {num1} {operador} {num2} es: {resultado}."
    
print(mensaje)
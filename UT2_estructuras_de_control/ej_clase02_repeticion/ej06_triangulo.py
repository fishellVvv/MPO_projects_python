# Ejercicio 6 - Triángulo de asteriscos

# Escribe un programa que pida al usuario un número entero positivo y dibuje un triángulo de asteriscos con la altura especificada.
# Por ejemplo, si el usuario ingresa 5, el triángulo debe verse así:
# *
# **
# ***
# ****
# *****

altura = int(input("Define la altura del triangulo: "))
for i in range(altura+1):
    print ("*" * i)
# Ejercicio 4 - Divisibilidad por 3 y 5

# Escribe un programa que pida al usuario un número entero y determine si es múltiplo de 3 o de 5.
# El programa debe imprimir un mensaje indicando el resultado.
# Si el número es múltiplo de ambos, debe imprimir "Múltiplo de 3 y 5".
# Si no es múltiplo de ninguno, debe imprimir "No es múltiplo de 3 ni de 5".

num = int(input("Introduce un número: "))

if num % 3 == 0 and num % 5 == 0:
    print("El número es divisible por 3 y 5")
elif num % 3 == 0:
    print("El número es divisible por 3")
elif num % 5 == 0:
    print("El número es divisible por 5")
else:
    print("El número no es divisible por 3 ni por 5")
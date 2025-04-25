# Ejercicio 7 - Tabla de multiplicar

# Escribe un programa que pida al usuario un número entero positivo y muestre la tabla de multiplicar de ese número.
# Por ejemplo, si el usuario ingresa 3, el programa debe imprimir:
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

numero = int(input("Escribe un numero entero: "))
for i in range(1, 11):
    print (numero, "x", i, "=", numero * i)
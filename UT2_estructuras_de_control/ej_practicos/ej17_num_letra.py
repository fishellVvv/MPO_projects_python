# Ejercicio 17

# Escribe un programa que reciba un número entero positivo y una letra.
# El programa debe imprimir la letra tantas veces como el número introducido.

numero = int(input("Escribe un numero entero positivo: "))
letra = input("Escribe una letra: ")
for i in range(numero+1):
    print(letra, end="")
print()
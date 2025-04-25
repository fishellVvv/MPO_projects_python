# Ejercicio 12

# Escribe un programa que pida al usuario dos números enteros 
#   e imprima la secuencia de números entre ellos (incluidos) en orden ascendente.
# Si el primer número es mayor que el segundo, imprime la secuencia en orden descendente.
# Debes imprimir la secuencia de números en una sola línea, separados por espacios.

numero1 = int (input("Introduce el primer número: "))
numero2 = int (input("Introduce el segundo número: "))

if numero1 > numero2:
    for i in range(numero1, numero2+1):
        print(i, end=" ")
else:
    for i in range(numero1, numero2-1, -1):
        print(i, end=" ")
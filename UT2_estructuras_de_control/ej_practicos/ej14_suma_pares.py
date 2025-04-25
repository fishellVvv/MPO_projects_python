# Ejercicio 14

# Escribe un programa que pida al usuario un número entero positivo 
#   e imprima la suma de los números pares por un lado 
#   y la suma de los números impares por otro.
# El programa debe imprimir ambos resultados.

numero = int(input("Indica un numero entero positivo: "))
suma_pares = suma_impares = 0
for i in range(numero+1):
    if (i%2 == 0):
        suma_pares += i
    else:
        suma_impares += i
print(f"La suma de los pares es {suma_pares} y la suma de los impares es {suma_impares}.")
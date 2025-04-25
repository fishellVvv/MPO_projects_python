# Ejercicio 5 - Múltiple de 3 o 5

# Escribe un programa que pida al usuario un número entero positivo 
#   e imprima solamente los números múltiplos de 3 o de 5 dentro de ese rango.
# Si el número es múltiplo de 3, imprime el número seguido de el mensaje "es múltiplo de 3".
# Si el número es múltiplo de 5, imprime el número seguido del mensaje "es múltiplo de 5".
# Si el número es múltiplo de ambos no debes imprimir nada.

numero = int(input("Escribe un numero entero positivo: "))
for i in range(numero):
    if (i%3 == 0 and i%5 == 0):
        pass
    elif (i%3 == 0):
        print (i, "es múltiplo de 3")
    elif (i%5 == 0):
        print (i, "es múltiplo de 5")
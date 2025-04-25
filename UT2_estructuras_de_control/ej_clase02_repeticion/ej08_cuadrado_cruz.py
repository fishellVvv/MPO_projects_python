# Cuadrado con cruz

# Escribe un programa que pida al usuario un número entero positivo impar y dibuje un cuadrado de x con una cruz en el medio.
# Por ejemplo, si el usuario ingresa 5, el cuadrado debe verse así:
# xxxxx
# xx xx
# x x x
# xx xx
# xxxxx

lado = int(input("Define el tamaño del cuadrado: "))
for i in range(lado):
    for j in range(lado):
        if i == 0 or i == lado-1: # lados superior e inferior
            print ("x", end="")
        elif j == 0 or j == lado-1: # lados izquierdo y derecho
            print ("x", end="")
        elif j == i: # primera diagonal
            print ("x", end="")
        elif i == lado-j-1: # segunda diagonal
            print ("x", end="")
        else:
            print(" ", end="")
    print ()
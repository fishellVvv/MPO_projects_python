'''
Ejercicio 22

Escribe un programa que inicialmente te indique el número de casos a tratar.
Después, para cada caso, te introduzca un número entero positivo del qual debes imprimir todos los divisores.
Un divisor de un número n es un número entero que divide a n sin dejar residuo.
El programa debe imprimir todos los divisores del número introducido en una sola línea, separados por espacios.
'''

casos = int(input("Introduce el número de casos: "))

for i in range(casos):
    num = int(input("Introduce un numero entero positivo: "))
    
    if num < 0:
        print("El número debe ser entero positivo.")
    else:
        print("Divisores:", end=" ")
        for j in range(1, num+1):
            if num % j == 0:
                print(j, end=" ")
        print()
'''
Ejercicio 21

Escribe un programa que te introduzca un número entero positivo que corresponde al número de casos a tratar.
Seguidamente te introducen un número entero positivo que corresponde a una serie de números.
Después debes recibir ese total de números e imprimirlos en la misma linea de la terminal,
    separados por un espacio y habiéndoles sumado 1 a cada uno de ellos.
'''

casos = int(input("Introduce el número de casos: "))

for i in range(casos):
    numeros = int(input("Cuántos números vas a introducir? "))
    lista_num = []

    for j in range(numeros):
        num = int(input())
        lista_num.append(num + 1)

    for n in lista_num:    
        print(n, end=" ")
    print()
# Ejercicio 8

# Escribe un programa que pida al usuario tres nombres e immprima True si alguno de los nombres es "Juan", False en caso contrario.

nombre1 = input("Introduce el primer nombre: ")
nombre2 = input("Introduce el segundo nombre: ")
nombre3 = input("Introduce el tercer nombre: ")

print(nombre1 == "Juan" or nombre2 == "Juan" or nombre3 == "Juan")
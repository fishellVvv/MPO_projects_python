'''
Ejercicio 2 - Condigura un mensaje de bienvenida

Escribe un programa que pida al usuario un nombre, un apellido y una edad.
El programa debe definir una función que reciba estos datos y luego imprima un mensaje de bienvenida personalizado.
'''

def condigurador_bienvenida(nombre, apellido, edad):
    """Imprime un mensaje de bienvenida personalizado"""
    print(f"Bienvenid@ {nombre} {apellido}, ¡para nada aparentas tener {edad} años!")

print("ConDigurador de mensajes de bienvenida")
nombre = input("Indica un nombre: ")
apellido = input("Indica un apellido: ")
edad = int(input("Indica una edad: "))

condigurador_bienvenida(nombre, apellido, edad)

'''
Ejercicio 6 - Dias de la semana
Escribe un programa que reciba números enteros positivos hasta la introducción de un 0.
Por cada número, suponiendo que el 1 representa el lunes, el 2 el martes, etc., 
    imprime el nombre del día correspondiente.
'''
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
numero = int(input("Ingrese un número (0 para salir): ")) % 7

while (numero != 0):
    print(dias_semana[numero - 1])
    numero = int(input("Ingrese un número (0 para salir): ")) % 7

print("Fin del programa.")
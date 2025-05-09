'''
Ejercicio 11 - Media de notas

Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar.
Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas.
El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1.
Al final, imprime la media.
'''

evaluaciones = int(input("Número de evaluaciones: "))

for i in range(evaluaciones):
    print()
    nota = 0
    num_notas = 0
    sum_notas = 0

    while nota != -1:
        nota = float(input("Introduce nota (-1 para salir): "))
        if nota != -1:
            num_notas += 1
            sum_notas += nota

    print(f"\nNota media evaluación {i+1}: {sum_notas/num_notas}")
'''
Ejercicio 19

Escribe un programa que dado una serie de notas introducidas por el usuario, hasta que introduzca un -1,
    imprima el número de notas correctas introducidas,
    la media de las notas y cuantas de estas notas son 10.
El programa debe imprimir la media de todas las notas introducidas, menos el -1.
'''
nota = float(input("Introduce las notas:\n"))
num_notas = 0
sum_notas = 0.0
num_diez = 0

while True:
    if 0 <= nota <= 10:
        num_notas += 1
        sum_notas += nota
        if nota == 10:
            num_diez += 1
    elif nota == -1:
        break
    nota = float(input())

if num_notas == 0:
    print("No has introducido ninguna nota.")
else:
    print(f"La media de estas {num_notas} notas es {sum_notas / num_notas}, se han obtenido {num_diez} dieces.")
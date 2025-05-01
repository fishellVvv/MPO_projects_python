# Los alumnos de Prometeo que cursan DAM/DAW + Master andan muy liados y no tienen claro cuando tienen clase y cuando no.

# Haz un programa que les indique si tienen clase de FP, de Máster, o de las dos en un conjunto de fechas dado.
# El usuario introduce un número N, que indica el número de días que quiere ver,
# se deberá imprimir el número del día, si no tienen nada en esa fecha,
# FP si tiene clase de un módulo de DAM/DAW o Máster si ese día tiene clase de máster.

# Los días múltiplos de 3 tienen clase de FP.
# Los días múltiplos de 5, de máster.
# Los días que son múltiplos de 3 y 5 tienen clase de las dos.

# Ejemplo de entrada:
# ---------------------------------
# 15

# Ejemplo de salida:
# ---------------------------------
# 1
# 2
# FP
# 4
# Máster
# FP
# 7
# 8
# FP
# Máster
# 11
# FP
# 13
# 14
# FP + Máster

print("Bienvenido al consultor de clases de DAM/DAW + Master.") # mensajes iniciales

try:
    numero_dias = int(input("Dime cuantos días quieres consultar: ")) # leemos el número de días a consultar
except ValueError: # revisamos que el valor introducido sea un entero
    print("Error: Debes introducir un número entero.")
    exit()

print("A continuación te muestro los días que tienes clase:")

for i in range(1, numero_dias+1): # vamos a iterar desde 1 hasta el número de días indicado
    if(i%3 == 0 and i%5 == 0): # primero comprobamos el caso con dos condiciones para que no se la salte
        print(f"Día: {i}\nClase de FP y de Master")
    elif(i%3 == 0):
        print(f"Día: {i}\nClase de FP")
    elif(i%5 == 0):
        print(f"Día: {i}\nClase de Master")
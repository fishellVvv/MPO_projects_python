# Pide al usuario que introduzca varios números enteros (uno por uno, y que indique "fin" para terminar).
# El programa debe verificar si cada número introducido es un "número de la suerte".
# Se considera un número de la suerte si es múltiplo de 7 (el resto de la división entre 7 es 0).
# Por cada número de la suerte encontrado, el programa imprimirá "¡[número] es un número de la suerte!".
# Al final, mostrará cuántos números de la suerte se encontraron en total.

# Pista: No olvides usar el try/catch 🙂

numeros_suerte = 0
numero_usuario = 0

print("Bienvenido al detector de números de la suerte.") # mensajes iniciales
print("Introduce todos los números que quieras a continuación:")
print("(escribe `fin` en cualquier momento para terminar)")

try:
    while True:
        numero_usuario = int(input("")) # leemos el dato indicado por el usuario
        if (numero_usuario%7 == 0): # comprobamos si es número de la suerte
            numeros_suerte += 1
            print(f"¡{numero_usuario} es un número de la suerte!")
except ValueError:
    print("Fin del juego.") # revisamos que el valor introducido sea un entero
    print(f"Has acumulado {numeros_suerte} números de la suerte.")
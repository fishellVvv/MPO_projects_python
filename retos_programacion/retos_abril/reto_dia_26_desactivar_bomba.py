# Imagina un programa donde el usuario tiene que introducir una secuencia de 4 números para desactivar una "bomba" (simulada).
# Usa un bucle for para pedir cada número.
# Implementa un try-catch para cuando el usuario introduce algo que no es un número,
#     y en ese caso, ¡la bomba hace un sonido gracioso en la consola
#     ("¡Pium! ¡Casi explotas por un carácter extraño!") y se reinician los intentos.
# Solo tienen 3 intentos (tras el primer input) antes de la "explosión" final (un mensaje en la consola).

import random

# inicialización de variables
codigo_usuario = [0, 0, 0, 0]
codigo_secreto = [0, 0, 0, 0]
codigo_comparado = ["·", "·", "·", "·"]
intentos = 3
bomba_activa = True

for i in range(len(codigo_secreto)):
    codigo_secreto[i] = random.randint(0, 9)

# mensaje de bienvenida e instrucciones
print("Hola artificiero, 👨‍🚒💣 se que es tu primer día pero tenemos una urgencia y tienes que desactivar la bomba.")
print("Aquí tienes... 🧨📟")
print("Ante tí ves una pequeña pantalla en la que tienes que introducir cuatro dígitos de uno en uno:")
print("╔═════════════════════════╗")
print("║ Ingresa el código:      ║")
print("╠═════════════════════════╣")
print(f"║ [ {codigo_usuario[0]} ] [ {codigo_usuario[1]} ] [ {codigo_usuario[2]} ] [ {codigo_usuario[3]} ] ║")
print("╚═════════════════════════╝")

# bucle hasta que se desactive o se agoten los intentos
while bomba_activa and intentos >= 0:
    for i in range(len(codigo_usuario)):
        while True:
            try:
                digito = int(input(f"Dígito {i + 1}: "))

                if 0 <= digito <= 9:
                    codigo_usuario[i] = digito
                    if codigo_usuario[i] < codigo_secreto[i]:
                        codigo_comparado[i] = "▲"
                    elif codigo_usuario[i] > codigo_secreto[i]:
                        codigo_comparado[i] = "▼"
                    else:
                        codigo_comparado[i] = "="
                    break
                else:
                    print("Error, introduce un dígito válido (0-9) ⛔️❌")

            except ValueError:
                print("¡Pium! ¡Casi explotas por un carácter extraño! 💥😵")

    # mostramos el resultado tras el intento
    print("\nLa bomba parece evaluar los datos introducidos:")
    print("╔═════════════════════════╗")
    print(f"║ Intentos restantes: {intentos}   ║")
    print("╠═════════════════════════╣")
    print(f"║ [ {codigo_usuario[0]} ] [ {codigo_usuario[1]} ] [ {codigo_usuario[2]} ] [ {codigo_usuario[3]} ] ║")
    print("╠═════════════════════════╣")
    print(f"║ [ {codigo_comparado[0]} ] [ {codigo_comparado[1]} ] [ {codigo_comparado[2]} ] [ {codigo_comparado[3]} ] ║")
    print("╚═════════════════════════╝")

    intentos -= 1

    # verificamos si todos los dígitos son correctos
    if all(simbolo == "=" for simbolo in codigo_comparado):
        bomba_activa = False

# resultado final
if bomba_activa:
    print("¡BOOOOOM! 💣💥🔥☠️")
else:
    print("¡Bomba desactivada! 🎉🟢🧯")
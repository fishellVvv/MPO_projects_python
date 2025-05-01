# El programa elige una palabra secreta (por ejemplo, "programar").
# El usuario tiene 5 intentos para adivinar la palabra.
# En cada intento, el programa compara la palabra introducida por el usuario con la palabra secreta.
# Si son iguales, muestra un mensaje de felicitación y termina.
# Si no son iguales, indica cuántos intentos le quedan.
# Si se agotan los intentos sin adivinar, muestra la palabra secreta y un mensaje de "¡Game Over!".

palabra_secreta = "programar"
intentos = 5

print("Adivina la palabra secreta (tienes 5 intentos).") # mensaje inicial

for i in range(intentos): # hacemos un bucle que itere para cada intento
    palabra_usuario = input(f"Intento número {i + 1}: ") # solicitamos la palabra

    if(palabra_usuario == palabra_secreta): # en caso de acertarla felicitamos y salimos del bucle
        print("Palabra correcta.\n ¡You Win!")
        break
    elif(i < intentos): # si falla comprobamos si quedan intentos y se lo indicamos al usuario
        print(f"Palabra incorrecta, te quedan {intentos - i} intentos.")
    else: # si falla y no le quedan intentos pues game over
        print(f"Palabra incorrecta.\n ¡Game Over!")
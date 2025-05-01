# Jordi nunca se acuerda de abrir las exclamaciones. Él dice que es porque en catalán no se abren las exclamaciones, pero yo creo que simplemente no sabe escribir.
# Vamos a crear un programa que asegure que hay tantos abrir exclamación (¡) como cerrar exclamación (!) para flamearlo.

# Ejemplo de entrada:
# -------------------------
# ¡¡¡Caramba!!!
# Hola!

# Ejemplo de salida:
# -------------------------
# Si
# No

conteo_exclamaciones = 0 # definimos un entero donde vamos a ir contabilizando las exclamaciónes
frase = input("Escribe tu frase: ") # solicitamos y escaneamos la frase

for i in range(len(frase)): # revisamos la frase letra por letra para buscar las exclamaciones
    if frase[i] == "¡":
        conteo_exclamaciones += 1 # cuando se abre una exclamación sumamos 1
    elif frase[i] == "!":
        conteo_exclamaciones -= 1 # cuando se cierra una exclamación restamos 1

if conteo_exclamaciones == 0: # Si las abiertas y las cerradas son las mismas el conteo estará a cero
    print ("Tu frase no tiene exclamaciones sin cerrar. ヽ(´▽`)/")
elif conteo_exclamaciones < 0: # Si se han cerrado más de las que se han abierto el conteo será negativo
    print (f"Tu frase tiene {conteo_exclamaciones * -1} exclamaciones sin abrir. (ಥ_ಥ)")
else: # Si se han abierto más de las que se han cerrado el conteo será positivo
    print (f"Tu frase tiene {conteo_exclamaciones} exclamaciones sin cerrar. (；￣Д￣)")
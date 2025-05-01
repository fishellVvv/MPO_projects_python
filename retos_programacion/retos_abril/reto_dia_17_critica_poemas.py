# Pide al usuario que introduzca un poema de hasta 4 líneas. Lola la Crítica intentará analizar su "métrica" según reglas muy extrañas:
# Línea 1: Debe tener exactamente 5 palabras.
# Línea 2: Debe contener la letra 'z' al menos una vez.
# Línea 3: Debe tener más vocales que consonantes.
# Línea 4: Debe terminar con la misma palabra con la que empezó la primera línea (ignorando mayúsculas/minúsculas).

# Para llevar a cabo el programa:
# Usa un bucle for para leer cada línea del poema.
# Usa if/else para verificar si cada línea cumple su regla. Si no, Lola da una crítica divertida (ej., "¡Demasiadas palabras para mi gusto!", "¡Le falta un toque de 'z'!".).
# Usa try-catch para manejar si el usuario introduce menos de 4 líneas (simulando un poema incompleto).
# Al final, da una "puntuación poética" basada en cuántas reglas cumplió el poema.

cuarteta = []
puntuacion = 0

print("Bienvenido poeta, escribe a continuación una cuarteta (poema de cuatro versos) y nuestra crítica Lola te lo analizará.") # mensaje inicial
print("-Lola: Veamos que tienes para mi:")

try:
    for i in range(4): # escribimos los 4 versos
        verso = input("")
        if not verso.strip():
            raise ValueError("Verso vacío")
        cuarteta.append(verso.lower())

        if i == 0: # Línea 1: Debe tener exactamente 5 palabras
            if len(cuarteta[i].split()) == 5:
                puntuacion += 1
            elif len(cuarteta[i].split()) > 5:
                print("-Lola: ¡Demasiadas palabras para mi gusto!")
            else:
                print("-Lola: ¡Pocas palabras para mi gusto!")
        elif i == 1: # Línea 2: Debe contener la letra 'z' al menos una vez
            if "z" in cuarteta[i]:
                puntuacion += 1
            else:
                print("-Lola: ¡Le falta un toque de 'z'!")
        elif i == 2: # Línea 3: Debe tener más vocales que consonantes
            vocales_consonantes = 0
            for letra in cuarteta[i]:
                if letra.isalpha() and letra in "aeiouáéíóú":
                    vocales_consonantes += 1
                elif letra.isalpha():
                    vocales_consonantes -= 1
            if vocales_consonantes > 0:
                puntuacion += 1
            else:
                print("-Lola: Más consonantes que vocales, ¡qué aspereza lírica!")
        elif i == 3: # Línea 4: Debe terminar con la misma palabra con la que empezó la primera línea
            if cuarteta[0].split()[0] == cuarteta[i].split()[-1]:
                puntuacion += 1
            else:
                print("-Lola: No me engañas, eso no rima con el principio.")

    print(f"\n-Lola: Mi veredicto final es: {puntuacion}/4 puntos poéticos.\n")
    if puntuacion == 4:
        print("-Lola: ¿Cómo lo has hecho?, no lo habrás generado con IA ¿no?")
    elif puntuacion == 3:
        print("-Lola: ¡Excelente!, estaré atenta a tu carrera literaria.")
    elif puntuacion == 2:
        print("-Lola: Me hayo notablemente sorprendida, ¡muy bien hecho!")
    elif puntuacion == 1:
        print("-Lola: No está nada mal para ser un aficionado de la literatura.")
    else:
        print("-Lola: Tampoco esperaba mucho, no me sorprende.")

except ValueError:
    print("-Lola: ¡Un poema incompleto! Me niego a seguir leyendo semejante abandono lírico.")
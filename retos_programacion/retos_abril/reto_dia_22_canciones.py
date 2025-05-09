# El programa elige una canción secreta de una lista.
# El usuario tiene un máximo de 4 intentos para adivinarla.
# En cada intento, pide al usuario el nombre de la canción.
# Si acierta, felicítalo y termina.
# Si falla, proporciona una pista "confusa" basada en la canción secreta
#   (ej. Si la canción es "Yellow Submarine", una pista podría ser "Tiene algo que ver con un color primario y un vehículo acuático... creo").
# Usa un bucle for para controlar los intentos.
# Si se agotan los intentos, revela la canción secreta.
# Si el usuario introduce una respuesta que no es una cadena de texto válida (intenta convertirla a un número, por ejemplo),
#     usa un try-catch para imprimir un mensaje como "¡Eso no suena como el título de una canción!".

import random

canciones_leidas = set()
lista_canciones = [
    {"pista": "Tiene algo que ver con un color primario y un vehículo acuático... creo", "cancion": "Yellow Submarine", "artista": "(The Beatles)"},
    {"pista": "Una ciudad con nombre de pecado... y mucha fama", "cancion": "Viva Las Vegas", "artista": "(Elvis Presley)"},
    {"pista": "Una noche... una especie de jinete... fantasmal", "cancion": "Ghost Riders in the Sky", "artista": "(Johnny Cash)"},
    {"pista": "Es como si fueras rápido, salvaje... y hubieras nacido para ello", "cancion": "Born to Be Wild", "artista": "(Steppenwolf)"},
    {"pista": "Algo que deseas hacer con mucha fuerza... como liberarte", "cancion": "I Want to Break Free", "artista": "(Queen)"},
    {"pista": "Una reina con intenciones... poco pacíficas", "cancion": "Killer Queen", "artista": "(Queen)"},
    {"pista": "Suena a escalera celestial o algo así...", "cancion": "Stairway to Heaven", "artista": "(Led Zeppelin)"},
    {"pista": "Un alojamiento turístico con nombre elegante", "cancion": "Hotel California", "artista": "(Eagles)"},
    {"pista": "Huele como el espíritu... pero de adolescentes", "cancion": "Smells Like Teen Spirit", "artista": "(Nirvana)"},
    {"pista": "Una autopista hacia un destino bastante caluroso", "cancion": "Highway to Hell", "artista": "(AC/DC)"},
    {"pista": "Una sacudida eléctrica muy sonora", "cancion": "Thunderstruck", "artista": "(AC/DC)"},
    {"pista": "Una forma cariñosa de referirse a una hija encantadora", "cancion": "Sweet Child O' Mine", "artista": "(Guns N' Roses)"},
    {"pista": "Nombre de mujer que también es una tormenta emocional", "cancion": "November Rain", "artista": "(Guns N' Roses)"},
    {"pista": "Cuando nada más importa... salvo la melodía", "cancion": "Nothing Else Matters", "artista": "(Metallica)"},
    {"pista": "Un número... temido por supersticiones y bestias", "cancion": "The Number of the Beast", "artista": "(Iron Maiden)"},
    {"pista": "Una advertencia metálica para quien rompe la ley", "cancion": "Breaking the Law", "artista": "(Judas Priest)"}
]

print("Bienvenido al Juego de Adivinar la Canción (JAC)")
input("Pulsa ENTER para continuar...")
print("Intenta adivinar las canciones con solo una pista, tienes 4 intentos para cada canción.")

# itera hasta que el usuario indique salir
while True:
    # creamos un numero aleatorio dentro de la lista y comprobamos si ya se ha leido
    num_cancion = random.randint(0, len(lista_canciones)-1)
    if num_cancion not in canciones_leidas:
        canciones_leidas.add(num_cancion)

        print(f"\nCanción {len(canciones_leidas)}: {lista_canciones[num_cancion]["pista"]}")
        for i in range(4):
            respuesta = input(f"{i + 1}/4 intentos: ")

            # evaluamos respuestas numericas y vacías
            try:
                if respuesta.strip() == "" or respuesta.isdigit():
                    raise ValueError("No es una canción")
            except ValueError:
                print("¡Eso no suena como el título de una canción!")

            if respuesta.lower() == lista_canciones[num_cancion]["cancion"].lower():
                print(f"¡Exacto! esa es la canción, {lista_canciones[num_cancion]["cancion"]} {lista_canciones[num_cancion]["artista"]}\n")
                break
            else:
                print("Incorrecto, ese no es el nombre")
                if i == 3:
                    print(f"\nEl nombre de la canción es: {lista_canciones[num_cancion]["cancion"]} {lista_canciones[num_cancion]["artista"]}")
        print(f"Hemos leido {len(canciones_leidas)} canciones.")

        # pregunta si se queda sin canciones y reinicia la lista
        if len(canciones_leidas) >= len(lista_canciones):
            continuar = input("Ya no me quedan más canciones. ¿Quieres volver a empezar? (Y/N): ").lower()

            while continuar not in ["y", "n"]:
                continuar = input("Opción no válida. ¿Quieres intentar otra canción? (Y/N): ").lower()

            if continuar == "y":
                canciones_leidas = set()
            else:
                exit()

        # pregunta si seguir solo si aún hay canciones por jugar
        continuar = input("¿Quieres intentar otra canción? (Y/N): ").lower()
        while continuar not in ["y", "n"]:
            continuar = input("Opción no válida. ¿Quieres intentar otra canción? (Y/N): ").lower()

        if continuar == "n":
            exit()
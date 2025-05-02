# El robot adivinador de personalidades hace 3 preguntas con 3 opciones cada una (diseña preguntas divertidas como "¿Qué prefieres hacer un sábado por la noche?").
# Cada opción está asociada a una "casa de personalidad" diferente (ej. "Aventurero", "Reflexivo", "Social").
# Usa un bucle for para hacer las 3 preguntas.
# Para cada pregunta, pide al usuario que elija una opción (1, 2 o 3).
# Usa if/else para asignar puntos a cada casa de personalidad según la respuesta elegida.
# Si el usuario introduce una opción inválida (no 1, 2 o 3), usa un try-catch para simular una "confusión del robot" e asigna un punto aleatorio a una de las casas.
# Después de las 3 preguntas, determina la casa con más puntos.
# Si hay un empate, elige una al azar.
# Anuncia la personalidad del usuario con un mensaje divertido basado en la casa ganadora (ej. "¡Eres un intrépido Aventurero, listo para conquistar cualquier código!").

import random

opcion = -1
puntos = [0, 0, 0]
preguntas_leidas = set()
lista_preguntas = [
    {"pregunta": "¿Qué prefieres hacer un sábado por la noche?",
    "respuestas": ["1. Escalar una montaña", "2. Leer un libro", "3. Ir de fiesta"]},
    {"pregunta": "Tu desayuno ideal es...",
    "respuestas": ["1. Un batido energético", "2. Té con tostadas", "3. Churros con amigos"]},
    {"pregunta": "¿Qué llevarías a una isla desierta?",
    "respuestas": ["1. Una navaja multiusos", "2. Un diario", "3. A tu mejor amigo"]},
    {"pregunta": "¿Tu superpoder favorito sería...?",
    "respuestas": ["1. Volar", "2. Leer la mente", "3. Hablar todos los idiomas"]},
    {"pregunta": "Elige una mascota:",
    "respuestas": ["1. Un halcón", "2. Un gato", "3. Un loro"]},
    {"pregunta": "Color que más te define:",
    "respuestas": ["1. Rojo", "2. Azul", "3. Amarillo"]},
    {"pregunta": "Estás en un grupo de trabajo, tú...",
    "respuestas": ["1. Tomas la iniciativa", "2. Organizas y planificas", "3. Conectas a todos"]},
    {"pregunta": "Tu transporte favorito:",
    "respuestas": ["1. Moto", "2. Tren", "3. Autobús"]},
    {"pregunta": "Tu reacción ante una sorpresa:",
    "respuestas": ["1. ¡Vamos allá!", "2. ¿Qué está pasando?", "3. ¡Qué emoción!"]},
    {"pregunta": "Tu lugar favorito en casa:",
    "respuestas": ["1. El balcón", "2. La biblioteca", "3. El salón"]}
]

# itera hasta haber realizado 3 preguntas
while len(preguntas_leidas) < 3:
    num_pregunta = random.randint(0, len(lista_preguntas)-1)
    if num_pregunta not in preguntas_leidas:
        preguntas_leidas.add(num_pregunta)

        # presenta una pregunta aleatoria no repetida
        print("\n",lista_preguntas[num_pregunta]["pregunta"])
        for respuesta in lista_preguntas[num_pregunta]["respuestas"]:
            print(respuesta)

        try:
            opcion = int(input("\nElige una opción: "))
            if opcion > 3 or opcion < 1:
                raise ValueError("Robot confundido")
        except ValueError:
            opcion = random.randint(1, 3)
            print(f"\nEstoy confundido, creo que querias decir {opcion}...")

        puntos[opcion-1] += 1

# si hay empate triple (1, 1, 1), suma un punto al azar
if puntos[0] == puntos[1] and puntos[0] == puntos[2]:
    opcion = random.randint(1, 3)

print("\nTest completado! tú personalidad es ",end="")
if puntos[0] > puntos[1] and puntos[0] > puntos[2]:
    print("aventurero.\nLos aventureros os caracterizáis por lanzaros a lo desconocido sin mirar atrás.\nTu mochila siempre está lista y tu frase favorita es: \"¿Qué podría salir mal?\"\n")
elif puntos[1] > puntos[0] and puntos[1] > puntos[2]:
    print("reflexivo.\nLos reflexivos os caracterizáis por pensar… mucho… a veces demasiado.\nAnalizas tanto cada situación que hasta tus decisiones llevan bibliografía.\n")
else:
    print("social.\nLos sociales os caracterizáis por tener siempre planes... incluso cuando querías quedarte en casa.\nTu superpoder: convertir cualquier reunión en una fiesta.\n")
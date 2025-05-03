# Emiliano el profe de Filosofía es el encargado de evaluar un examen de 3 preguntas de opción múltiple (A, B, C).
# Define las respuestas correctas para cada pregunta.
# Pide al usuario que introduzca sus respuestas para cada pregunta.
# Usa un bucle for para leer las 3 respuestas del usuario.
# Usa if/else para comparar cada respuesta del usuario con la respuesta correcta, asignando puntos (ej. 1 punto por respuesta correcta).
# Introduce una "respuesta ambigua" para una de las preguntas (ej. la respuesta correcta podría ser 'A' o 'B').
# Si el usuario elige cualquiera de las opciones ambiguas, asigna medio punto.
# Usa try-catch para manejar si el usuario introduce una opción inválida (algo diferente de A, B o C),
#     penalizando con 0 puntos para esa pregunta y mostrando un mensaje de "¡Respuesta inválida!".
# Al final, muestra la puntuación total del usuario.

lista_preguntas = [
    {"pregunta": "¿Cuál es la principal obra de Platón?",
    "respuestas": ["A. La Política", "B. La República", "C. Ética a Nicómaco"],
    "puntuaciones": [0, 1, 0]},
    {"pregunta": "¿Qué es más importante según el existencialismo?",
    "respuestas": ["A. La existencia", "B. La libertad", "C. La moral absoluta"],
    "puntuaciones": [0.5, 0.5, 0]},
    {"pregunta": "¿Qué significa el \"mito de la caverna\" de Platón?",
    "respuestas": ["A. Una metáfora sobre la percepción y la verdad", "B. Un texto sobre astronomía", "C. Una parábola sobre la guerra"],
    "puntuaciones": [1, 0, 0]}
]
puntos = 0

print("Bienvenido al examen, a continuación se plantearán 3 preguntas.")
print("Por favor, escoge una respuesta para cada pregunta.")

for i in range(len(lista_preguntas)):
    print("\n",lista_preguntas[i]["pregunta"])
    for respuesta in lista_preguntas[i]["respuestas"]:
        print(respuesta)

    try:
        respuesta_usuario = input("\nRespuesta: ").lower()

        if respuesta_usuario not in ("a", "b", "c"):
            raise ValueError("Respuesta inválida")
        
        indice = {"a": 0, "b": 1, "c": 2}[respuesta_usuario]
        puntos += lista_preguntas[i]["puntuaciones"][indice]
        
    except ValueError:
        print("¡Respuesta inválida!")

print(f"\nTu puntuación final es: {puntos} puntos.")

if puntos == 2.5:
    print("¡Excelente! ¡Has acertado todo!")
elif puntos >= 1.5:
    print("Nada mal, has tocado fondo en la caverna y visto algo de luz.")
else:
    print("Necesitas repasar filosofía... y rápido.")
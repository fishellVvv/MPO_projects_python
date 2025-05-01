# Hoy en clase, a Federico le han dicho que las flashcards son un buen mét_odo de estudio.
# Pero Federico no tiene nada para escribir en su casa. ¿Se te ocurre alguna forma para que pueda estudiar con el mét_odo mencionado?

# Pues claro que sí, vas a crear un programa que:
# Almacene las flashcards en una lista (pregunta, respuesta).
# Permita al usuario añadir nuevas flashcards.
# Muestra una pregunta aleatoria de la lista.
# Solicite una respuesta del usuario.
# Compare la respuesta del usuario con la correcta.
# Indique si la respuesta es correcta o incorrecta.
# Permita continuar practicando o salir.

# Ejemplo:
# ------------------------
# Anverso: La programación es…
# Reverso: Darle una serie de instrucciones a una máquina para que ejecute una acción específica.

import random


opcion = 0
flashcards = [
    ["La programación es…", "Darle una serie de instrucciones a una máquina para que ejecute una acción específica."], 
    ["¿Cuál es la mejor película de la historia?", "The Matrix"], 
    ["¿Cuál es el sentido de la vida, el universo y todo lo demás?", "42"]
    ]

print("Bienvenido Federico, iniciando flashcards:\n") # mensaje de inicio

while(opcion != 3): # salimos al poner la opción 3
    print("1. Añadir nuevas Flashcards.")
    print("2. Pregunta aleatoria.")
    print("3. Salir.")
    opcion = int(input("\nElige una opción: ")) # pedimos una opción

    if(opcion == 1):
        print("\nAñadir nuevas Flashcards:\n")
        pregunta = input("Introduce la pregunta: ") # solicitamos la pregunta
        respuesta = input("Introduce la respuesta: ") # solicitamos la respuesta
        flashcards.append([pregunta, respuesta])
        print("\nFlashcard añadida, ¿que quieres hacer ahora?\n")
    elif(opcion == 2):
        print("\nPregunta aleatoria: ")
        pregunta_random = random.randint(1, len(flashcards)) # creamos un numero random entre 1 y el numero de flashcards
        print(f"\nPregunta: {flashcards[pregunta_random][0]}") # mostramos la pregunta aleatoria
        respuesta_usuario = input("Tu respuesta: ") # leemos la respuesta del usuario

        if(respuesta_usuario == flashcards[pregunta_random][1]): # si acierta
            print("\n✅ ¡Correcto!\n")
        else: # si la respuesta no es exacta le decimos la correcta
            print(f"\n❌ Incorrecto. La respuesta era: {flashcards[pregunta_random][1]}")

        input("Pulsa ENTER para volver al menú...") #solicitamos ENTER para dar tiempo a leer la respuesta
        print("\n¿Que quieres hacer ahora?\n")
    elif(opcion == 3):
        print("\nByeeee!") # despedida y salida
    else:
        print("\nEsa opción no está, elige una de estas:\n") # en caso de que la opción no exista volvemos al menú
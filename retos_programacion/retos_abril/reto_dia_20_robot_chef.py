# Un robot chef está aprendiendo a cocinar, pero solo conoce recetas con ciertos ingredientes.
# Tienes dos listas de ingredientes: ingredientes_conocidos (ej. "tomate", "cebolla", "ajo") y ingredientes_secretos (ej. "polvo de hadas", "lágrimas de unicornio").
# - Pide al usuario que introduzca una lista de 5 ingredientes para una receta.
# Usa un bucle for para iterar sobre los ingredientes del usuario.
# Para cada ingrediente, verifica con if/else si está en ingredientes_conocidos. Si lo está, el robot dice "¡Excelente elección!".
# Si el ingrediente está en ingredientes_secretos, el robot, usando un try-catch para simular una reacción mágica inesperada, imprime un mensaje como "¡Chispas! ¡Este ingrediente tiene propiedades mágicas!".
# Si el ingrediente no está en ninguna de las listas, el robot dice "¿Qué es eso? ¡No tengo ni idea de cómo usarlo!".
# Al final, muestra cuántos ingredientes conocidos, secretos y desconocidos intentó usar el usuario.

ingredientes_conocidos = ["tomate", "cebolla", "ajo", "aceite", "sal", "pimienta", "pollo", "ternera", "pescado", "arroz", "pasta", "pan", "queso", "huevo"]
ingredientes_secretos = ["polvo de hadas", "lágrimas de unicornio", "esencia de dragón", "pluma de fénix", "brisa de luna", "escama de sirena"]
num_ing_conocidos = 0
num_ing_secretos = 0
num_ing_desconocidos = 0

print("Bienvenido! soy el robot Chef, vamos a evaluar los ingredientes.")
print("Por favor, a continuación enseñame los 5 ingredientes de tu receta.\n")

# iteramos sobre los 5 ingredientes introducidos por el usuario
for i in range(5):
    ingrediente = input(f"Ingrediente {i + 1}: ")
    try:
        if ingrediente.lower() in ingredientes_secretos:
            raise ValueError("Destello mágico")
        elif ingrediente.lower() in ingredientes_conocidos:
            num_ing_conocidos += 1
            print("¡Excelente elección!")
        else:
            num_ing_desconocidos += 1
            print("¿Qué es eso? ¡No tengo ni idea de cómo usarlo!")
    except ValueError:
        num_ing_secretos += 1
        print("¡Chispas! ¡Este ingrediente tiene propiedades mágicas!")

print("\n¡Perfecto!, para la receta tenemos: ")
print(f"Ingredientes conocidos: {num_ing_conocidos}")
print(f"Ingredientes secretos: {num_ing_secretos}")
print(f"Ingredientes desconocidos: {num_ing_desconocidos}")

# mensajes personalizados
if num_ing_desconocidos > 3:
    print("\nA ver como sale este experimento, ya me contarás.")
elif num_ing_secretos == 5:
    print("\n¡Esto no es una receta, es un hechizo de nivel experto!")
else:
    print("\n¡Seguro que queda una receta increíble!")
# Crea un programa que pida al usuario que introduzca nombres de flores.
# Almacena estos nombres en una lista.
# Luego, con un bucle for-each, revisa cada nombre.
# Si el nombre tiene menos de 3 letras, ¡decláralo una "palabra marchita" y usa un try-catch para intentar
#     acceder a una cuarta letra (que no existirá), capturando la StringIndexOutOfBoundsException (IndexError) con un mensaje
#     divertido como: "¡Tan corta que ni siquiera tiene una cuarta letra para oler!".

# usamos un conjunto para evitar duplicados
flores = set()

print("Bienvenido al Jardinero de Palabras Marchitas.")
print("A continuación introduce el nombres de flores (pulsa enter sin escribir nada para finalizar)\n")

while True:
    flor = input(f"Nombre de la flor {len(flores) + 1}: ")
    if flor == "":
        break
    if flor in flores:
        print("Esta flor ya la has dicho... 🪴")
    else:
        flores.add(flor)

print("\nAnalizando las flores...\n")

for flor in flores:
    print(f"Analizando la flor \"{flor}\": ")
    try:
        # provocamos IndexError si no tiene 4 letras
        test = flor[3]
        print("Ésta es una flor curiosa... 🪷")
    except IndexError:
        print("¡Tan corta que ni siquiera tiene una cuarta letra para oler! 🌱")

if flores:
    print("\n¡Adiós! 🍀")
else:
    print("\nNo se ha plantado ninguna flor... 🌧️")
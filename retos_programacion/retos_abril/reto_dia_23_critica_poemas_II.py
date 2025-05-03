# Lola te va a pedir 2 palabras e intentará determinar si riman.
# La regla de rima simplificada es: las ÚLTIMAS DOS letras deben ser iguales (ignorando mayúsculas/minúsculas).
# Usa if/else para comparar las últimas dos letras.
# Si riman, imprime "¡Estas palabras riman!".
# Si no, imprime "¡No riman!".
# Usa bloques try-catch para manejar posibles errores:
# Si alguna de las palabras tiene menos de dos letras, captura la excepción (ej. StringIndexOutOfBoundsException)
#     y muestra un mensaje como "¡Necesito al menos dos letras para rimar!".
# Si el usuario introduce algo que no se puede tratar como una cadena
#     (aunque esto es más difícil de simular directamente con nextLine(),
#     puedes intentarlo si pides la entrada de otra forma), captura un error
#     genérico y responde con "¿Eso se considera una palabra?".

print("Bienvenido de nuevo poeta, escribe dos palabras que rimen y nuestra crítica Lola te lo analizará.")
print("-Lola: Veamos que tienes para mi:")

try:
    palabra_1 = input("Primera palabra: ")
    palabra_2 = input("Segunda palabra: ")

    # comprobación de longitud de palabras
    if len(palabra_1) < 2 or len(palabra_2) < 2:
        raise IndexError("Palabras demasiado cortas")

    if palabra_1.lower() == palabra_2.lower():
        print("\n-Lola: Homer con Homer rima... ¡¡¡Muuuak!!!")
    elif palabra_1.lower()[-2:] == palabra_2.lower()[-2:]:
        print("\n-Lola: ¡Estas palabras riman!")
    else:
        print("\n-Lola: ¡No riman!")

except IndexError:
    print("\n-Lola: ¡Necesito palabras de al menos dos letras para rimar!")
except Exception as e:
    print("\n-Lola: ¿Eso se considera una palabra?")
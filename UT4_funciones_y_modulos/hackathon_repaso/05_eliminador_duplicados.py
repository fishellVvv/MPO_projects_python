palabras = input("Introduce palabras separadas por coma(,): ")
palabras_separadas = palabras.split(",")
palabras_sin_duplicados = set(palabras_separadas)

print(sorted(palabras_sin_duplicados))
texto = input("Introduce una frase: ").split()

caracteres = 0
palabras = 0
palabra_larga = ""

for p in texto:
    palabras += 1
    for c in p:
        caracteres += 1
    if len(p) > len(palabra_larga):
        palabra_larga = p

print(f"Hay {palabras} palabras y {caracteres} letras, la palabra más larga es '{palabra_larga}'.")

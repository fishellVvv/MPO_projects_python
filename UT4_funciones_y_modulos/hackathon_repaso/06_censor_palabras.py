censura = ["tonto", "feo", "culo", "pedo", "pis"]
texto = input("Escribe una frase: ")

for p in censura:
    texto = texto.replace(p, "*"*len(p))

print(texto)

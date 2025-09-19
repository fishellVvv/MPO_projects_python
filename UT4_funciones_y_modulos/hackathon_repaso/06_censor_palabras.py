censura = ["tonto", "feo"]

texto = input("Escribe una frase: ")
lista_palabras = texto.split()

for p in lista_palabras:
    if p in censura:
        print("*"*len(p))
    else:
        print(p)
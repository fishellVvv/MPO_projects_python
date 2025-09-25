palabra = list(input("Introduce una palabra: "))
palabra_invertida = ""
vocales = list("aeiou")

for i in range(len(palabra)-1, -1, -1):
    if palabra[i].lower() in vocales:
        palabra_invertida += "*"
    else:
        palabra_invertida += palabra[i]

print(palabra_invertida)

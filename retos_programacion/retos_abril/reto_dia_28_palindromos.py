# Crea un programa con un array de palabras.
# Utiliza un bucle for-each para analizar cada palabra.
# Si una palabra es un palíndromo (se lee igual al revés),
#     ¡declárala "misteriosamente palíndroma: [palabra]"!

palabras = ["Palabra", "Oso", "Mundo", "Reconocer", "Abracadabra", "Sometemos"]

for palabra in palabras:
    if palabra.lower() == palabra.lower()[::-1]:
        print(f"Misteriosamente palíndroma: {palabra}")
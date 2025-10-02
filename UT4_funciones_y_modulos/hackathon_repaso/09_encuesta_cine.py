entrada = ""
lista = []

while entrada != "fin":
    entrada = input("Introduce el título de una película: ")
    if entrada != "fin":
        lista.append(entrada)

lista_ordenada = sorted(set(lista))

print(f"\nHas introducido {len(lista)} películas.")
print(f"La primera película que has introducido es '{lista[0]}'")
print(f"La última película que has introducido es '{lista[-1]}'")
print("Aquí tienes el listado completo de películas que has introducido:")
for peli in lista_ordenada:
    print(peli)
print()

texto = input("Introuduce un texto: ").lower().split()
palabra = input("Introduce la palabra a buscar: ").strip()
num = 0

for i in range(len(texto)):
    if texto[i] == palabra:
        print(f"Palabra '{texto[i]}' localizada en {i + 1}.")
print(f"La palabra aparece un total de {texto.count(palabra)} veces.\n")

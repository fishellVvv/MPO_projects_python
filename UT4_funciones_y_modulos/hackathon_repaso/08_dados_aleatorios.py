from random import randint

dados = [randint(1, 6) for _ in range(10)]
for i in range(len(dados)):
    print(f"Dado nº {i + 1}: {dados[i]}")

contador = {}
for d6 in dados:
    contador[d6] = contador.get(d6, 0) + 1
max_f = max(contador.values())

print("\nModa(s): ", end="")
for num, f in contador.items():
    if f == max_f:
        print(num, end=" ")
print("\n")

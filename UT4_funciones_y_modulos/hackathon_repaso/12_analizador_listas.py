def analizar_lista(lista):
    maximo = max(lista)
    minimo = min(lista)
    media = float(sum(lista) / len(lista))
    unicos = set(lista)

    analisis = {"max": maximo, "min": minimo, "media": media, "unicos": unicos}
    return analisis

lista = input("\nIntroduce números separados por coma (1, 2, 3): ").split(", ")
try:
    lista_num = [int(num) for num in lista]
    analisis = analizar_lista(lista_num)
    print("\nAnálisis estadístico:\n"
        f"Máximo: {analisis['max']}\n"
        f"Mínimo: {analisis['min']}\n"
        f"Media: {analisis['media']:.2f}\n"
        f"Valores únicos: ", end=""
    )
    for n in analisis["unicos"]:
        print(f"{n} ", end="")
    print("\n")
except ValueError:
    print("Error: valores incorrectos.")

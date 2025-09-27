alumnos = [
    ["Luis", 8.5, 9, 7],
    ["Victor", 10, 10, 10],
    ["Carmen", 5, 6, 6]
]

def media_fila(fila):
    notas = fila[1:]
    return sum(notas) / len(notas)

resumen = [[fila[0], media_fila(fila)] for fila in alumnos]

ancho_nombre = max(len(fila[0]) for fila in alumnos + [["Nombre  "]])

print( "┌" + ("─" * (ancho_nombre + 2)) + "┬───────┬───────┬───────┬───────┐")
print(f"│ {'Nombre'.ljust( ancho_nombre )} │ N1    │ N2    │ N3    │ Media │")
print( "├" + ("─" * (ancho_nombre + 2)) + "┼───────┼───────┼───────┼───────┤")
for fila in alumnos:
    n1, n2, n3 = fila[1:]
    media = media_fila(fila)
    print(f"│ {fila[0].ljust(ancho_nombre)} │ {n1:>5.2f} │ {n2:>5.2f} │ {n3:>5.2f} │ {media:>5.2f} │")
print( "└" + ("─" * (ancho_nombre + 2)) + "┴───────┴───────┴───────┴───────┘")

print("\nResumen:")
for nombre, media in resumen:
    print(f"{nombre}, nota media: {media:.2f}")
print()

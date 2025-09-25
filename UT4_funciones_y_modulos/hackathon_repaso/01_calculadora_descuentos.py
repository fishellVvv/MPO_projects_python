precio = float(input("Introduce un precio: "))
descuento = float(input("Introduce un descuento (en %): "))

print(f"El precio con descuento es {precio - (precio * descuento / 100):.2f} €")

# Ejercicio 9

# Escribe un programa que pida el precio de un producto y, si supera los 100€, aplique un descuento del 10%.
# Muestra el precio final.

precio = float(input("Introduce el precio del producto: "))

if precio > 100:
    descuento = precio * 0.1
    precio_final = precio - descuento
else:
    precio_final = precio

print(f"El precio final es: {precio_final}€")
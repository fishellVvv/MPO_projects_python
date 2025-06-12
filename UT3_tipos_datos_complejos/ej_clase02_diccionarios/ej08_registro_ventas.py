'''
Ejercicio 8 - Registro de ventas

Escribe un programa que gestione un diccionario de productos, y por cada producto una lista de ventas diarias representadas como tuplas (día, unidades_vendidas).
Haz un menú que permita al usuario:
    1. Añadir un producto con su nombre.
    2. Añadir un registro de ventas para un producto específico.
    3. Consultar las ventas totales de un producto.
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".
'''

inventario = {}
opcion = 0

while opcion != 4:
    opcion = int(input("\nElige una opción: \n" \
        "1. Añadir producto\n" \
        "2. Añadir registro de venta\n" \
        "3. Consultar ventas totales\n" \
        "4. SALIR\n\n"))

    if opcion == 1:
        producto = input("Indica el nombre del producto: ").lower().strip()
        if producto in inventario:
            print("El producto ya existe en el inventario.")
        else:
            inventario[producto] = []
            print("Producto registrado.")
        
    elif opcion == 2:
        producto = input("Indica el nombre del producto: ").lower().strip()
        dia = int(input("Indica el día de la venta (numero entero): "))
        unidades = int(input("Indica las unidades vendidas (numero entero): "))
        if producto in inventario:
            inventario[producto].append((dia, unidades))
            print("Venta registrada.")
        else:
            print("El producto no existe en el inventario.")
        
    elif opcion == 3:
        producto = input("Indica el nombre del producto a consultar: ").lower().strip()
        if producto in inventario:
            total = 0
            for (dia, unidades) in inventario[producto]:
                total += unidades

            print(f"Ventas totales de {producto}: {total} unidades")
        else:
            print("El producto no existe en el inventario.")
        
    elif opcion > 4 or opcion < 1:
        print("\nElige una opción válida")

print("\nFin del programa.")
inventario = {}

while True:
    try:
        opcion = int(input(
            "\nSISTEMA DE GESTIÓN\n"
            "1. Añadir productos\n"
            "2. Vender productos\n"
            "3. Visualizar inventario\n"
            "0. Salir\n"
        ))
        print()
    except ValueError:
        print("Error: introduce una opción válida.")
        continue

    match opcion:
        case 1:
            nombre = input("Nombre: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    print("Error: la cantidad debe ser positiva.")
                    continue
            except ValueError:
                print("Error: cantidad inválida.")
                continue

            inventario[nombre] = inventario.get(nombre, 0) + cantidad
            print(
                f"Añadidas {cantidad} unidad(es) de '{nombre}'. "
                f"Stock actual: {inventario[nombre]}"
            )

        case 2:
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    print("Error: la cantidad debe ser positiva.")
                    continue
            except ValueError:
                print("Error: cantidad inválida.")
                continue

            stock = inventario.get(nombre)
            if stock is None:
                print(f"'{nombre}' no existe en el inventario.")
            elif stock < cantidad:
                print(f"Stock insuficiente (disponible {stock}).")
            else:
                inventario[nombre] = stock - cantidad
                print(f"Venta realizada. Stock de '{nombre}': {inventario[nombre]}")

        case 3:
            if not inventario:
                print("Inventario vacío.")
            else:
                print("Inventario:")
                for producto, cantidad in sorted(inventario.items()):
                    print(f"- {producto}: {cantidad} unidad(es).")

        case 0:
            print("Saliendo...")
            break

        case _:
            print("Elige una opción válida.")
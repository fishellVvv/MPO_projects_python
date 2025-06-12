'''
Ejercicio 3 - Inventario de productos

Escribe un programa que gestione un inventario de productos utilizando un diccionario.
El programa debe permitir al usuario añadir productos con su nombre y cantidad, eliminar productos y consultar la cantidad de un producto específico.
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".
'''

inventario = {}
opcion = 0

while opcion != 4:
    opcion = int(input("\nElige una opción: \n" \
        "1. Añadir producto\n" \
        "2. Eliminar producto\n" \
        "3. Consultar cantidad\n" \
        "4. SALIR\n"))

    if opcion == 1:
        producto = input("\nIntroduce el nombre del producto: ")
        cantidad = int(input("Introduce la cantidad: "))
        inventario[producto] = cantidad
    elif opcion == 2:
        producto = input("\nIntroduce el nombre del producto a eliminar: ")
        if producto in inventario:
            del inventario[producto]
            print(f"producto {producto} eliminado del inventario.")
        else:
            print(f"El producto {producto} no se encuentra en el inventario.")
    elif opcion == 3:
        producto = input("\nIntroduce el nombre del producto: ")
        if producto in inventario:
           print(f"{producto}: {inventario[producto]} unidades")
        else:
            print(f"El producto {producto} no se encuentra en el inventario.")
    elif opcion > 4 or opcion < 1:
        print("\nElige una opción válida")

print("\nFin del programa.")
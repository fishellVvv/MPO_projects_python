'''
Ejercicio 5 - Biblioteca digital

Escribe un programa que gestione una biblioteca digital utilizando un diccionario.
El programa permite al usuario añadir libros con su título, autor y año de publicación.
El usuario debe poder consultar los libros por autor o por año de publicación.
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".
'''

biblioteca = {}
opcion = 0

while opcion != 4:
    opcion = int(input("\nElige una opción: \n" \
        "1. Añadir libro\n" \
        "2. Consultar libros por autor\n" \
        "3. Consultar libros por año de publicación\n" \
        "4. SALIR\n"))
    
    if opcion == 1:
        titulo = input("\nIntroduce el título del libro: ")
        autor = input("Introduce el autor del libro: ")
        año = int(input("Introduce el año de publicación del libro: "))

        biblioteca[titulo] = {"autor": autor, "año": año}
        print(f"Libro {titulo} añadido a la biblioteca.")

    elif opcion == 2:
        autor_buscado = input("\nIntroduce el autor: ")
        encontrados = []

        for titulo, datos in biblioteca.items():
            if datos["autor"].lower() == autor_buscado.lower():
                encontrados.append((titulo, datos["año"]))
        if encontrados:
            print(f"Libros de {autor_buscado}:")
            for libro in encontrados:
                print(f"- {libro[0]} ({libro[1]})")
        else:
            print("No hay libros de este autor en la biblioteca.")

    elif opcion == 3:
        año_buscado = int(input("\nIntroduce el año de publicación "))
        encontrados = []

        for titulo, datos in biblioteca.items():
            if datos["año"] == año_buscado:
                encontrados.append((titulo, datos["autor"]))
        if encontrados:
            print(f"Libros de {año_buscado}:")
            for libro in encontrados:
                print(f"- {libro[0]} ({libro[1]})")
        else:
            print("No hay libros de este año en la biblioteca.")

    elif opcion > 4 or opcion < 1:
        print("\nElije una opción válida.")
print("\nPrograma finalizado.")
'''
Ejercicio 7 - Búsqueda por valor en un diccionario

Escribe un programa que replique el comportamiento del ejercicio 1, pero en lugar de buscar por clave (pais), el usuario debe buscar por valor (capital).
El programa debe permitir al usuario introducir una capital y devolver el país correspondiente.
Si la capital no está en el diccionario, el programa debe informar al usuario.
'''

paises = {}
entrada = input("Indica un valor de la forma 'PAIS-CAPITAL' o escribe 'FIN INSERCIONES' para terminar\n").lower()

while entrada != "fin inserciones":
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises[pais] = capital
    
    entrada = input("Indica un valor de la forma 'PAIS-CAPITAL' o escribe 'FIN INSERCIONES' para terminar\n").lower()

consulta = input("Intruduce el nombre de la capital que quieres consultar: ").lower()

for pais, capital in paises.items():
    if capital.lower() == consulta:
        print(f"El país del cual {consulta.capitalize()} es la capital es {pais.capitalize()}.")
    else:
        print(f"No hay ningún país con capital {consulta.capitalize()}.")

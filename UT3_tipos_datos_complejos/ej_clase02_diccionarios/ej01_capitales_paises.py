'''
Ejercicio 1 - Capitales y países

Escribe un programa que almacene en un diccionario las capitales de varios paises, se introducirán los datos con la forma PAIS-CAPITAL. 
Esto debe ejecutarse indefinidamente hasta que el usuario intruduzca "FIN INSERCIONES". 
El programa debe permitir al usuario consultar la capital de un pais introduciendo su nombre. 
Si el país no está en el diccionario, el programa debe informar al usuario.
'''

paises = {}
entrada = input("Indica un valor de la forma 'PAIS-CAPITAL' o escribe 'FIN INSERCIONES' para terminar\n").lower()

while entrada != "fin inserciones":
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises[pais] = capital
    
    entrada = input("Indica un valor de la forma 'PAIS-CAPITAL' o escribe 'FIN INSERCIONES' para terminar\n").lower()

consulta = input("Intruduce el nombre del país que quieres consultar: ").lower()
if consulta in paises:
    print(f"La capital de {consulta.capitalize()} es {paises[consulta].capitalize()}")
else:
    print("No existe ese registro en el diccionario.")
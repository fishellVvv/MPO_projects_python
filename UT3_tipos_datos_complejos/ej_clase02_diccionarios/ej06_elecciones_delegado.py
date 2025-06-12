'''
Ejercicio 6 - Elecciones a delegado

Escribe un programa que simule unas elecciones a delegado de clase.
El programa debe permitir votar por un candidato introduciendo su nombre.
Al finalizar la votación, el programa debe mostrar el candidato ganador y el número de votos obtenidos.
Si hay un empate, el programa debe informar al usuario del primer candidato que alcanzó el número máximo de votos.
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN VOTACIONES".
'''

candidatos = {}

print("Bienvenido a las elecciones para delegadod e clase:")
voto = input("Introduce tu voto (escribe 'FIN VOTACIONES' para terminar): ")

while voto.lower() != "fin votaciones":
    if voto in candidatos:
        candidatos[voto] += 1
    else:
        candidatos[voto] = 1

    voto = input("Introduce tu voto: ")

if not candidatos:
    print("\nNo se han registrado votos.")
else:
    max_votos = max(candidatos.values())

    ganador = None
    for nombre, votos in candidatos.items():
        if votos == max_votos:
            ganador = nombre
            break

    print("\nResultados de la votación:")
    print(f"- Ganador: {ganador} (obtuvo {max_votos} votos).")
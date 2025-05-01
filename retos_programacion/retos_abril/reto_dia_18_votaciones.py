# Simula una votación simple para 3 candidatos ("Coder", "Debugger", "Tester").
# Pide a 5 votantes que introduzcan su voto (el nombre del candidato).
# Usa un bucle for para simular los 5 votantes.
# Usa un diccionario (o similar) para llevar el conteo de votos para cada candidato.
# Usa if/else para verificar si el voto introducido es para uno de los candidatos válidos.
# Si no lo es, incrementa un contador de "votos inválidos".
# Introduce la posibilidad de un "error de conteo" aleatorio (simula lanzar una excepción dentro del if/else de los votos válidos).
# Usa un try-catch alrededor del proceso de conteo. Si ocurre el error, muestra un mensaje de "¡Error en el conteo! ¡Se descarta este voto!".
# Al final, muestra el número de votos para cada candidato y el número total de votos inválidos.

import random


recuento_votos = {"Coder": 0, "Debugger": 0, "Tester": 0}
votos_invalidos = 0

print("Bienvenido a la votación, los candidatos son: Coder, Debugger y Tester.") # mensaje inicial
print("Por favor, a continuación introduce el voto de cada votante y pulsa Enter para continuar.")

for i in range(5): # iteramos los 5 votantes
    voto = input(f"Votante {i +1}: ")

    try:
        if voto in recuento_votos: # comprobamos que el voto cruce con algún candidato
            if random.random() < 0.1:
                raise ValueError("Error de conteo") # hay un 10% de que el voto se invalide
            recuento_votos[voto] += 1
        else:
            raise ValueError("Error de conteo") # si el voto no coincide con ningún candidato, lanzamos el error y descartamos el voto
    except ValueError: # aquí se recuentan los votos invalidados y se muestra un mensaje de error
        votos_invalidos += 1
        print("¡Error en el conteo! ¡Se descarta este voto!")

print("\nConteo final de votos: ")
for candidato, num_votos in recuento_votos.items(): # iteramos todos los candidatos
    print(f"{candidato}:   \t{num_votos} votos")
print(f"Invalidos: \t{votos_invalidos} votos") # mostramos también el recuento de los votos invalidados
# Imagina una emocionante carrera entre caracoles cibernéticos. Cada caracol tiene una velocidad aleatoria entre 1 y 5 (¡qué emoción!).

# Escribe un programa que simule una carrera de 20 "pasos" entre dos caracoles.
# En cada paso, la posición de cada caracol aumenta según su velocidad.
# Al final, ¡declara al caracol ganador (o si hay un emocionante empate)!

# Pista: usar random

import random

gary = "__@/" # las referencias
rayo = "__O/" # <3
pos_gary = 0
pos_rayo = 0
META = 20 # la posición de meta se establece como una constante

print("Bienvenidos todos a la XIV Carrera Intergaláctica de Caracoles Cibernéticos!!!") # comentarios de inicio
print("Con todos ustedes los protagonistas del evento:")
print(f"Con el dorsal 42, el caracol Gary!!!:\t{gary}")
print(f"Y con el dorsal 95, Rayo McSnail!!!:\t{rayo}")
print("\n¡Ya están en sus marcas!\n")

print("\t  SALIDA → |___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___| META [20 m]\n") # dibujamos la pista en estado inicial
print(f"Gary [{pos_gary:>2} m]:\t{gary}") # Gary el Caracol
print(f"Rayo [{pos_rayo:>2} m]:\t{rayo}") # Rayo McSnail
print()

while(pos_gary < META and pos_rayo < META): # este bucle iterará mientras que ninguno haya llegado a la meta
    pos_gary += random.randint(1, 5) # la posición de Gary aumenta entre 1 y 5 en cada iteración
    pos_rayo += random.randint(1, 5) # la de rayo también

    if(pos_gary >= META or pos_gary >= META):
        print("🏁 La carrera ha terminado!!!\n") # mensaje final si hay meta
    elif(pos_gary > pos_rayo):
        print("Gary va lanzado a por la victoria!\n")
    elif(pos_gary < pos_rayo):
        print("Rayo McSnail está delante!\n")
    else:
        print("La carrera no puede ser mas emocionante, cualquiera puede ganar!\n")

    print("\t  SALIDA → |___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___-___| META [20 m]\n") # dibujamos la pista en cada iteración
    print(f"Gary [{pos_gary:>2} m]:\t".ljust(4), end="")
    for i in range(pos_gary): # se dibujan tantos ". " como metros ha avanzado
        print(".".ljust(4), end="")
    print(gary)
    print(f"Rayo [{pos_rayo:>2} m]:\t".ljust(4), end="")
    for i in range(pos_rayo):
        print(".".ljust(4), end="")
    print(rayo)
    print()

if(pos_gary > pos_rayo):
    print("🏆 Gary el Caracol ha ganado la copa!!!\n") # mensaje final en caso de victoria de Gary
elif(pos_gary < pos_rayo):
    print("🏆 Rayo McSnail ha ganado la copa!!!\n") # mensaje final en caso de victoria de Rayo
else:
    print("🤝 Increíble! Tenemos un empate!!! Todo se decidirá en la siguiente ronda!\n") # mensaje final en caso de empate
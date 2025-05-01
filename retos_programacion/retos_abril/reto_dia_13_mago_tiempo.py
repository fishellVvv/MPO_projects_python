# ¿Alguna vez te has levantado con la necesidad de crear un cronómetro? Tranquilo, no eres el único. Hoy vas a poder hacer tu sueño realidad.
# Crea un programa que:
# Pida al usuario que ingrese el número de segundos que desea contar.
# Usa un bucle para contar desde el primer segundo hasta el número total de segundos indicado por el usuario.
# Cada vez que el cronómetro llegue a 60 segundos, debe reiniciar los segundos a 0 y sumar 1 minuto.
# Cuando los minutos lleguen a 60, debe reiniciar los minutos a 0 y sumar 1 hora.
# El cronómetro debe mostrar el tiempo en formato hh:mm:ss, donde hh son las horas, mm los minutos y ss los segundos.

# PISTA: Para que el cronómetro se actualice cada segundo, puedes utilizar la función time.sleep(1).
#     Esto hará que el programa espere 1 segundo entre cada iteración del bucle, imitando el comportamiento de un cronómetro real.

# Ejemplo:
# ---------
# 00:00:01
# 00:00:02
# 00:00:03
# etc.

import time

print("⏱ Cronómetro Mágico ⏱") # mensajes iniciales
print("\nIndica el número de segundos que quieres contar con el cronómetro mágico.")
print("Recuerda que un minuto son 60 segundos y una hora son 3600 segundos.")
numero_segundos = int(input("Número de Segundos: "))
print("\n----------")

for i in range(1, numero_segundos+1): # iteramos hasta contar todos los segundos
    print(f"{int(i / 3600):02d}:{int((i % 3600) / 60):02d}:{(i % 60):02d}") # hh:mm:ss
    time.sleep(1) # pausa la ejecución 1 segundo

print("----------\n")
print("⏰ ¡Tiempo! ⏰")
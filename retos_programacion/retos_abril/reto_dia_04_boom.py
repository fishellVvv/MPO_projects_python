# Un resplandor y hace ¡BOOM! y digo, ains ya está aquí la guerra
# Como dice la señora del famoso meme, un día estalló la guerra. Haz un programa que, dado un número que se pasa por entrada, haga una cuenta atrás y acabe con un ¡BOOM!.

# Ejemplo de entrada:
# -----------------------------
# 5

# Ejemplo de salida:
# -----------------------------
# 5
# 4
# 3
# 2
# 1
# ¡BOOM!

duracion_resplandor = int (input ("- La Antonia: Un resplandor...\n Indica la duración del resplandor: ")) # solicitamos la duración de la cuenta atrás

for i in range(duracion_resplandor, 0, -1): # recorremos en un bucle todas las posiciones desde el valor dado hasta 1
    print(i, end=" ")

print ("\n- La Antonia: ...y hace ¡BOOM! y digo, ains ya está aquí la guerra\n") # y ¡BOOM!
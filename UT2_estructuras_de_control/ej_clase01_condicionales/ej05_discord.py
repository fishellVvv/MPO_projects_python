# Ejercicio 5 - Puede entrar en el servidor de Discord?

# Escribe un programa que pida un rol y una academia de estudios,
# si el rol es "alumno" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial y al de los alumnos, donde se critica a los profes.
# Si el rol es "profesor" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial, pero no al de los alumnos.
# En cualquier otro caso, el programa debe imprimir "No tienes acceso al servidor de Discord".

rol = input("Introduce tu rol (alumno/profesor): ").lower()
academia = input("Introduce tu academia de estudios (Prometeo/otra): ").lower()

if rol == "alumno" and academia == "prometeo":
    print("Tienes acceso al servidor de Discord oficial y al de los alumnos.")
elif rol == "profesor" and academia == "prometeo":
    print("Tienes acceso al servidor de Discord oficial, pero no al de los alumnos.")
else:
    print("No tienes acceso al servidor de Discord.")
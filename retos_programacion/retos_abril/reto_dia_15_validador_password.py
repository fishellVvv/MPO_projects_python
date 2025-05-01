# Resulta que nos piden que programemos un validador de contraseñas.
# Algo fácil para los alumnos de Prometeo.
# Solo tenemos que decir si, una contraseña introducida por terminal es válida o no.
# Para que una contraseña sea válida debe:

# Tener al menos 8 caracteres.
# Tener al menos una letra minúscula.
# Tener al menos una letra mayúscula.
# Tener al menos un número.
# Tener al menos un símbolo especial de entre los siguientes *, ?, !, ^, “, $.
# No contener la palabra GIT, en ningún formato (ni GIT, ni git, ni gIt, ni giT, ni Git, ni GIt, ni gIT, ni GiT). Odiamos Git.

import re
password_valida = False

print("Validador de contraseñas.") # mensaje inicial

while not password_valida:
    password = input("\nPor favor, introduce una contraseña válida: ") # solicitamos la contraseña

    if len(password) < 8: # vamos revisando los requisitos
        print("❌ La contraseña es demasiado corta, debe tener al menos 8 caracteres")
    elif not re.search(r"[a-z]", password):
        print("❌ La contraseña debe tener al menos una letra minúscula")
    elif not re.search(r"[A-Z]", password):
        print("❌ La contraseña debe tener al menos una letra mayúscula")
    elif not re.search(r"[0-9]", password):
        print("❌ La contraseña debe tener al menos un número")
    elif not re.search(r'[*?!^"$]', password):
        print("❌ La contraseña debe tener al menos un símbolo especial")
    elif "git" in password.lower():
        print("❌ La contraseña no puede contener la palabra 'git' (en ningún formato)")
    else:
        print("\n✅ Contraseña válida. ¡Buen trabajo!")
        password_valida = True
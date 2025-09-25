from random import randint, shuffle


def generar_password(longitud):
    if longitud < 4:
        raise ValueError("mínimo 4")

    MAYUS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    MINUS = list("abcdefghijklmnopqrstuvwxyz")
    NUMB = list("0123456789")
    SIMB = list("!@#$%^&*")
    TODO = [MAYUS, MINUS, NUMB, SIMB]

    pwd = []
    pwd.append(MAYUS[randint(0, len(MAYUS)-1)])
    pwd.append(MINUS[randint(0, len(MINUS)-1)])
    pwd.append(NUMB[randint(0, len(NUMB)-1)])
    pwd.append(SIMB[randint(0, len(SIMB)-1)])
    for _ in range(longitud - 4):
        tipo_car = randint(0, len(TODO)-1)
        pwd.append(TODO[tipo_car][randint(0, len(TODO[tipo_car])-1)])

    shuffle(pwd)
    return "".join(pwd)

try:
    long_pass = int(input("Indica una longitud para tu password (mayor que 4): "))
    print(f"Password: {generar_password(long_pass)}")
except ValueError:
    print("Error: valor incorrecto.")
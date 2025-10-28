from datetime import datetime

def get_access(userName, password):
    whiteList = ["Victor", "Jordi"]
    correctPassword = "cl500"
    access = False

    if (userName in whiteList and password == correctPassword):
        access = True

    time = datetime.now().isoformat(timespec="seconds")
    line = f"{time}, {userName}, {access}\n"

    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(line)

    if (access):
        print("Acceso concedido")
    else:
        print("Acceso denegado")

userName = input("Nombre de usuario: ")
password = input("Contraseña: ")

try:
    get_access(userName, password)
except Exception as e:
    print(e)

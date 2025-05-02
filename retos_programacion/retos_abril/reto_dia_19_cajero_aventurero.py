# Simula un cajero automático con un saldo inicial.
# Permite al usuario realizar las siguientes acciones (usando un bucle for para un máximo de 3 intentos fallidos de PIN):
# - Introducir PIN: Pide al usuario un PIN (establece uno secreto).
#     Si lo introduce incorrectamente 3 veces, bloquea la cuenta (simula esto con un mensaje y terminal).
# - Consultar Saldo: Muestra el saldo actual.
# - Retirar Fondos: Pide la cantidad a retirar.
#     Usa try-catch para manejar si el usuario introduce algo que no es un número.
#     Si la cantidad es válida, verifica si hay suficiente saldo.
#     Si no, informa del saldo insuficiente.
#     Si todo va bien, resta la cantidad del saldo y muestra un mensaje de éxito.
# - Salir: Termina la simulación.
#     El programa debe mostrar un menú de opciones en cada paso hasta que el usuario elija salir o la cuenta se bloquee.

pin_tarjeta = 1234
intentos_pin = 3
saldo = 1000

print("Bienvenido al Cajero Aventurero.")

# solicita PIN hasta agotar los intentos
while intentos_pin > 0:
    try:
        pin_usuario = int(input("Ingrese su PIN: "))
    except ValueError:
        print("Pin no válido. Solo se permiten números.")
        continue

    if pin_usuario == pin_tarjeta:
        print("PIN correcto, accediendo...")
        break
    else:
        intentos_pin -= 1
        print(f"PIN erróneo: intentos restantes: {intentos_pin}")
        if intentos_pin == 0:
            print("PIN erróneo, la cuenta se ha bloqueado.")
            exit()

# menú principal: bucle hasta que el usuario elija salir
while True:
    print("\n-----------------------------------------")
    print(" *** Bienvenido al Cajero Aventurero ***")
    print("0. Salir")
    print("1. Consultar saldo")
    print("2. Retirar fondos\n")

    try:
        op_menu = int(input("Elija una opción: "))
    except ValueError:
        print("Opción no válida.")
        continue

    if op_menu == 0:
        print("Gracias por usar el Cajero Aventurero.\n")
        break

    elif op_menu == 1:
        print(f"Saldo actual: {saldo} €")
        input("\nPulse ENTER para continuar...")

    elif op_menu == 2:
        if saldo == 0:
            print("Saldo insuficiente.")
            continue
        try:
            cantidad = int(input("Cantidad a retirar: "))
            if cantidad <= 0:
                print("Por favor, introduce una cantidad positiva.")
            elif cantidad > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= cantidad
                print(f"Retirada de fondos realizada, saldo restante: {saldo} €")
        except ValueError:
            print("Por favor, introduce una cantidad positiva.")
        input("\nPulsa ENTER para continuar...")

    else:
        print("Opción fuera de rango.")
        continue
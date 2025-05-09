'''
Ejercicio 15 - Banca online

Escribe un programa que simule una cuenta bancaria.
El programa debe permitir al usuario realizar las siguientes operaciones:
1. Ingresar dinero
2. Retirar dinero
3. Consultar saldo
4. Salir
Inicializa el saldo en 0 y permite al usuario realizar operaciones hasta que decida salir.
'''

saldo = 0.00

while True:
    print("\nBANCA ONLINE")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = int(input("\nElige una opción: "))
    
    match opcion:
        case 1:
            movimiento = float(input("\nIndica el saldo a ingresar: "))
            saldo += movimiento
            print(f"Ingreso de {movimiento} € realizado.")
        case 2: 
            movimiento = float(input("\nIndica el saldo a retirar: "))
            saldo -= movimiento
            print(f"Retirada de {movimiento} € realizada.")
        case 3:
            print(f"El saldo actual de la cuenta es {saldo} €")
        case 4:
            print("\nSaliendo de la banca online.")
            break
        case _:
            print("\nLa opción no se encuentra en la lista")

    input("\nPulsa ENTER para continuar")
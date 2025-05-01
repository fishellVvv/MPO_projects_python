# Crea una calculadora muy especial que a veces está de buen humor y otras no.
# Pide al usuario que introduzca dos números y la operación (+, -, *, /).
# Si la operación es división (/) y el segundo número es 0, la calculadora se pondrá de mal humor y lanzará un error
# (simúlalo con un try-catch que imprima un mensaje como "¡¿Dividir por cero?! ¡¿Acaso quieres destruir el universo?!").
# Para las otras operaciones, realiza el cálculo normal y muestra el resultado con un mensaje alegre como "¡Tadá! El resultado es...".

print("¡Hola!\n (^_^)／ Soy la calculadora felíz. Aunque los infinitos me enfadan... por favor, no me hagas calcular infinitos.\n") # mensaje inicial

try:
    num1 = int(input("Introduce el primer número: ")) # solicitamos el primer número
    operacion = input("Introduce la operación (+, -, *, /): ") # solicitamos la operación
    num2 = int(input("Introduce el segundo número: ")) # solicitamos el segundo número

    if operacion == "+":
        print(f"\nSumandooooo... {num1} + {num2} es igual a {num1 + num2} ＼(＾▽＾)／")
    elif operacion == "-":
        print(f"Vamos con esa resta; {num1} - {num2} es igual a {num1 - num2} (⌒‿⌒)")
    elif operacion == "*":
        print(f"¡Me encantan las multiplicaciones! {num1} * {num2} es igual a {num1 + num2} (•‿•)")
    elif operacion == "/":
        print(f"\n¡Tadá! El resultado de {num1} / {num2} es igual a {num1 / num2} (⁀‿⁀)")
    else:
        print("\nPero, ¿Que dices? ¡Eso no es lo que te he pedido! (ಠ_ಠ)")
except ZeroDivisionError:
        print("\n¡¿Dividir por cero?! ¡¿Acaso quieres destruir el universo?! (҂‾ ▵‾)︻デ═一")
except ValueError:
        print("\nPero, ¿Que dices? ¡Eso no es lo que te he pedido! (ಠ_ಠ)")
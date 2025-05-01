# Una tienda de galletas artesanales vende al por mayor en su página web. Cada caja de galletas cuesta 6€. Solicita la cantidad de cajas de galletas en cada venta y dependiendo de la cantidad introducida se realizan los siguientes pasos:
# Si la cantidad de cajas de galletas vendidas es menor a 5: no se permiten compras inferiores a 5 cajas de galletas.
# Si la cantidad de cajas de galletas es mayor o igual a 5, pero menor a 15: los gastos de envío son de 10€.
# Si la cantidad de cajas de galletas es mayor a 15: El envío es gratuito.

# Promociones:
# Si el precio total es inferior a 120€ no hay promociones.
# Si el precio total supera los 120€ pero es menor a 250€: Tiene un descuento del 5%.
# Si el precio total supera los 250€: Tiene un descuento del 10%.

# Muestra al cliente un mensaje por pantalla según la cantidad de cajas de galletas que quiera comprar:
# Número total de cajas a comprar.
# Total € de la compra.
# Gastos de envío (si los tiene o si es gratuito)
# Descuento por compra (Indicar al cliente cuántos € falta para entrar en una promoción si la compra es <100€ o el importe de descuento generado si es superior)

PRECIO_CAJA = 6 # definimos el precio de la caja como una constante
cajas_minimas = 5
gastos_envio = 10
envio_gratuito = 15
minimo_promo_1 = 120
minimo_promo_2 = 250
descuento_promo = 0

print("🍪🍪🍪 Bienvenido a COOKIES SUPER RICAS S.A. 🍪🍪🍪") # texto de inicio
print("Nuestras galletas son las más ricas del multiverso.")
print("\nAntes de pedir recuerda nuestras ofertas:")
print("¡¡¡OFERTA Coockie Monster!!!: 5% de descuento en compras a partir de las 120 cajas.")
print("¡¡¡OFERTA Coockie Clicker!!!: 10% de descuento en compras a partir de las 250 cajas.")
print("\n(compra mínima de 5 cajas) ", end="")
print("(los pedidos de menos de 15 cajas tendrán un coste adicional de 10 € de gastos de envío) ", end="")
print("(COOKIES SUPER RICAS S.A. se reserva el derecho a opinar sobre la ricura de sus propias galletas)")

try:
    numero_cajas_pedido = int(input("\nPor favor, indica el número de cajas de galletas que deseas comprar: ")) # solicitamos un número de cajas
except ValueError: # revisamos que el valor introducido sea un entero
    print("Error: Debes introducir un número entero.")
    exit()

if(numero_cajas_pedido < cajas_minimas): # si no llega al mínimo salimos
    print(f"\nLo sentimos, el número de cajas mínimo es {cajas_minimas}")
else:
    if(numero_cajas_pedido >= envio_gratuito): # comprobamos si hay que descontar los gastos de envío
        gastos_envio = 0

    if((numero_cajas_pedido * PRECIO_CAJA) + gastos_envio > minimo_promo_2): # comprobamos la oferta mayor primero para que no salte
        descuento_promo = 0.1
    elif((numero_cajas_pedido * PRECIO_CAJA) + gastos_envio > minimo_promo_1): # comprobamos la otra oferta en caso de ni haber entrado la primera
        descuento_promo = 0.05
    
    print("\nResumen del pedido:") # imprimimos el resumen del pedido
    print(f"\nNúmero de cajas pedidas: {numero_cajas_pedido}")
    print(f"A {PRECIO_CAJA} € cada caja, suman un total de {numero_cajas_pedido * PRECIO_CAJA} €")
    print(f"Gastos de envio: {gastos_envio} €")
    print(f"Dexcuento por oferta: {descuento_promo * 100} %")
    # se aplica precio de las cajas de galletas más los gastos de envío y luego a eso lo convertimos a € y le aplicamos el descuento
    print(f"\nTotal a pagar: {((numero_cajas_pedido * PRECIO_CAJA) + gastos_envio) * (1 - descuento_promo)} €")
    print("\n🍪🍪🍪 Muchas gracias por comprar en COOKIES SUPER RICAS S.A. Vuelva pronto!!! 🍪🍪🍪")
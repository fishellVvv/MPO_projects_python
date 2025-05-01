# Juan está trabajando en un Mercadona en el que no hay cajero automático, él siempre calcula el cambio de los clientes de cabeza. ¿Se te ocurre alguna forma de hacerle la vida más sencilla al pobre chaval?

# Crea un programa que:
# Reciba la cantidad de dinero (double) que el usuario ha entregado para pagar.
# Compare la cantidad entregada con el precio del producto y calcule la diferencia.
# Súmale el IVA porque esto es España, redondeado a dos décimas (+21%)
# Devuelva el valor utilizando la menor cantidad de billetes y monedas posibles siendo estos;
#     billete de 500 €, billete de 200 €, billete de 100 €, billete de 50 €, billete de 20 €, billete de 10 €, billete de 5 €,
#     moneda de 2 €, moneda de 1 €, moneda de 50 cénts, moneda de 20 cénts, moneda de 10 cénts, moneda de 2 cénts y moneda de 1 cént.

# Pero cuidado, si un cliente intenta pagar con menos dinero del necesario… ¡Tendrás que avisarle antes de que se lleve el producto gratis!

# Ejemplo:
# El producto cuesta 17 €.
# El cliente te da 20 pavos.
# El cambio es de 1 moneda de 1 euro y 1 moneda de 2 euros.

import random
from tokenize import Double

cambio_valores = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] # vamos a trabajar con enteros porque usaremos los valores en céntimos y al mostralos los dividiremos por 100 para simplificar las operaciones
cambio_etiquetas = ["billetes de 500 €", "billetes de 200 €", "billetes de 100 €", "billetes de 50 €", "billetes de 20 €", "billetes de 10 €", "billetes de 5 €", "monedas de 2 €", "monedas de 1 €", "monedas de 50 cént.", "monedas de 20 cént.", "monedas de 10 cént.", "monedas de 5 cént.", "monedas de 2 cént.", "monedas de 1 cént."] # y las etiquetas de los diferentes tipos de billetes y monedas

print ("Iniciando cajero...\n** Bienvenido a Mercadona **\nEscaneando producto...") # mensajes iniciales
precio_producto = random.randint(100, 10000) # generamos un valor aleatorio para el coste del producto entre 1 y 100 euros (en centimos)
precio_con_IVA = round(precio_producto * 1.21) # calculamos el precio con IVA redondeando al céntimo
print (f"\nEl precio es:  {precio_producto / 100:>8.2f} €") # mostramos en pantalla el "ticket"  :>6.2f alinea a la derecha la cifra
print (f"+ IVA 21%:     {(precio_con_IVA - precio_producto) / 100:>8.2f} €")
print ("-------------------------")
print (f"Total a pagar: {precio_con_IVA / 100:>8.2f} €")

try:
    dinero_cliente = float(input("\nIntroduce la cantidad de dinero aportada por el cliente: ")) # solicitamos la cantidad de dinero que el cliente paga
except ValueError: # excepción que nos avisa de que el dato dado no es del tipo esperado
    print ("\nEntrada no válida. Debes introducir una cantidad numérica (ej: 125.50).")
    exit()

dinero_recibido = round(dinero_cliente * 100) # convertimos a céntimos y redondeamos

el_cambio = dinero_recibido - precio_con_IVA # calculamos el cambio

if(el_cambio > 0): # si nos da suficiente dinero, calculamos el cambio y el desglose
    print(f"\nEl cambio es: {el_cambio / 100} €")
    print("Desglose del cambio: ")

    for i in range(len(cambio_valores)): # iteramos los valores del Array de mayor a menor (del billete de 500 € a la moneda de 1 céntimo)
        cantidad = int(el_cambio / cambio_valores[i]) # calculamos cuantos billetes o monedas de este tipo "caben" en el cambio
        if (cantidad > 0):
            print(f"\t{cantidad} {cambio_etiquetas[i]}") # si el Valor del Array es menor al cambio, calculamos cuantos billetes o monedas de este tipo hay que dar
            el_cambio %= cambio_valores[i] # recalculamos el cambio dejando el resto, de esta manera en la siguiente iteración podemos comprobar el siguiente valor del Array

    print("\nGracias por comprar en Mercadona.\n") # mensaje de despedida
elif(el_cambio == 0): # si nos da el dinero exacto salta a esta opción
    print("\nEl cambio es: 0.00 €\n\nGracias por comprar en Mercadona.\n")
else: # si falta dinero salta a esta opción
    print("\nFalta dinero, ¿donde está la pasta?\n")
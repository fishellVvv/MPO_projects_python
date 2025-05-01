# Escribe un programa que le pregunte al usuario su nombre.
# Si el nombre comienza con la letra "A" (mayúscula o minúscula), el robot responderá con un saludo entusiasta como: ¡Hola, Asombroso/a "Nombre"!.
# Si el nombre tiene más de 7 letras, el robot dirá: ¡Vaya, "Nombre", ¡qué nombre tan largo y sofisticado!.
# Para cualquier otro nombre, el robot simplemente dirá: Saludos, "Nombre".

# ¡Prepara al robot para t_odo tipo de nombres! Como un saludo especial a un nombre que empiece por A y tenga 7 letras, o que cuente un chiste si saluda a Jaimito...

nombre = input("¡Buenas!, ¿Como te llamas?\n") # preguntamos el nombre y lo escaneamos

if(nombre[0].lower() == 'a' and len(nombre) > 7): # compruebo primero los casos compuestos para que no se los salte
    print(f"¡Hola, Asombroso/a {nombre}, qué nombre tan largo y sofisticado!")
elif(len(nombre) > 7):
    print(f"¡Vaya, {nombre}, qué nombre tan largo y sofisticado!")
elif(nombre[0].lower() == 'a'):
    print(f"¡Hola, Asombroso/a {nombre}!")
elif(nombre.lower() == "jaimito"):
    print("Me se un chiste con tu nombre;\n—Profe, ¿me castigaría por algo que no he hecho?\n—Claro que no, Jaimito.\n—¡Menos mal! Porque no he hecho los deberes.") # perdón...
elif(nombre.lower() == "victor"):
    print("Ah si, otra vez tu... Hola, supongo...")
else:
    print(f"Saludos, {nombre}.")
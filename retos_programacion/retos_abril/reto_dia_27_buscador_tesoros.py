# Crea un programa que tenga un array de cadenas de texto.
# Utiliza un bucle for-each para examinar cada cadena.
# Si una cadena contiene la palabra "tesoro" (sin importar mayúsculas o minúsculas),
#     ¡anuncia el descubrimiento con un "¡Tesoro encontrado: [cadena]!"!

cadenas = [
    "¡He encontrado el Tesoro escondido en la playa!",
    "Dicen que el tEsOrO está enterrado bajo la vieja iglesia.",
    "Lo que siento por ti es un verdadero TES0RO del alma.",
    "Aquel mapa apuntaba directamente al tesorito maldito.",
    "Su apellido era Montesorovaldi, de origen italiano.",
    "En la caverna hallaron una caja etiquetada como teso_r0...",
    "Mi gato se llama Tesora y duerme todo el día.",
    "Nunca supe que la palabra atestoronado existía...",
    "Un antiguo manuscrito mencionaba el TeSoRaCo de los Andes.",
    "Te adoro más que a cualquier TresorO perdido."
]

for cadena in cadenas:
    if "tesoro" in cadena.lower():
        print(f"¡Tesoro encontrado: [{cadena}]!")
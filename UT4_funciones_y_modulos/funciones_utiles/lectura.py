'''
Funciones para leer diferentes tipos de datos con control de errores
'''

from funciones_utiles.escritura import imprimir


def leer_entero(mensaje = "Introduce un número entero: ", color = None):
    try:
        imprimir(mensaje, color)
        entero = int(input())
    except ValueError:
        raise ValueError
    return entero

def leer_string(mensaje = "Introduce un texto: ", color = None):
    imprimir(mensaje, color)
    return input()

def leer_string_en_lista(mensaje = "Introduce un texto: ", color = None):
    imprimir(mensaje, color)
    return input().split(" ")

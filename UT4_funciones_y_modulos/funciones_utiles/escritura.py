'''
Funciones para imprimir con difrentes añadidos y con control de errores
'''

from colorama import Style

def imprimir(mensaje, color = None):
    if color != None:
        mensaje = color + mensaje + Style.RESET_ALL
    print(mensaje)

def imp_marco (mensaje, color = None):
    frases = mensaje.split("\n")
    long_frase = [len(frase) for frase in frases]
    long_max = max(long_frase)
    msj_marco = ""
    for frase in frases:
        msj_marco += "│ " + frase + " " * (long_max - len(frase)) + " │\n"
    barra_sup = "┌─" + "─" * long_max + "─┐" + "\n"
    barra_inf = "└─" + "─" * long_max + "─┘"
    msj_completo = barra_sup + msj_marco + barra_inf
    if color != None:
        msj_marco = color + msj_completo + Style.RESET_ALL
    print(msj_completo)

def pulsa_enter(color = None):
    if color != None:
        input(color + "\nPulsa enter para continuar..." + Style.RESET_ALL)
    else:
        input("\nPulsa enter para continuar...")
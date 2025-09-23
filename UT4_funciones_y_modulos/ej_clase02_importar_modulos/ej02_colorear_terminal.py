'''
Ejercicio 2 - Coloreando la Terminal con colorama

Vamos a evolucionar el programa del ejercicio anterior para que los mensajes se muestren con colores utilizando el módulo colorama.

Concretamente vamos a modificar la opción de listar archivos.

En vez de imprimir los nombres de los archivos directamente, vamos a colorearlos según su tipo:
    - Archivos de texto (.txt) en verde.
    - Archivos de imagen (.jpg, .png) en azul.
    - Archivos de audio (.mp3, .wav) en amarillo.
    - Otros archivos en blanco.
'''

from operator import concat
import os
from pathlib import Path
from colorama import Fore

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from funciones_utiles.lectura import leer_entero, leer_string
from funciones_utiles.escritura import imprimir, imp_marco, pulsa_enter

colm = {
    "MENU": Fore.BLUE,
    "EXIT": Fore.RED,
    "SUCCESS": Fore.LIGHTGREEN_EX,
    "ERROR": Fore.LIGHTRED_EX,
    "INPUT": Fore.LIGHTYELLOW_EX,
    "CONTINUE": Fore.LIGHTWHITE_EX
}

def main():
    os.chdir(Path(__file__).resolve().parent) # Sitúa el cwd en la carpeta del script

    while True:
        menu_principal()
        try:
            opcion = leer_entero("Selecciona una opción: ", colm["INPUT"])
        except ValueError:
            imprimir("❌ Error: introduce un número del 0 al 4.", colm["ERROR"])
            continue

        match opcion:
            case 1:
                ruta = leer_string("Introduce la ruta que quieres consultar: ", colm["INPUT"])
                if ruta == "":
                    ruta = "."
                    if ruta[-1] != "\\":
                        ruta = ruta + "\\"

                try:
                    archivos = listar_archivos(ruta)
                    print()
                    for archivo in archivos:
                        imprimir(archivo, colorear(obtener_extension(ruta, archivo)))
                except FileNotFoundError:
                    imprimir(f"❌ Error: la ruta {ruta} no existe", colm["ERROR"])
                pulsa_enter(colm["CONTINUE"])

            case 2:
                nombre = leer_string("Indica el archivo a verificar: ", colm["INPUT"]).strip()
                if existe_archivo(nombre):
                    imprimir(f"✅ El archivo {nombre} existe.", colm["SUCCESS"])
                else:
                    imprimir(f"❌ El archivo {nombre} no existe.", colm["ERROR"])
                pulsa_enter(colm["CONTINUE"])

            case 3:
                nombre = leer_string("Indica el nombre del nuevo archivo: ", colm["INPUT"]).strip()
                if existe_archivo(nombre):
                    imprimir(f"❌ Error: el archivo {nombre} ya existe", colm["ERROR"])
                else:
                    archivo = crear_archivo(nombre)
                    imprimir(f"✅ Archivo {archivo.name} creado con exito.", colm["SUCCESS"])
                pulsa_enter(colm["CONTINUE"])

            case 4:
                nombre = leer_string("Indica el nombre de la nueva carpeta: ", colm["INPUT"]).strip()
                try:
                    crear_directorio(nombre)
                    imprimir(f"✅ Carpeta {nombre} creada con exito.", colm["SUCCESS"])
                except FileExistsError:
                    imprimir(f"❌ Error: el archivo {nombre} ya existe", colm["ERROR"])
                pulsa_enter(colm["CONTINUE"])

            case 0:
                imprimir("Saliendo...", colm["EXIT"])
                break

            case _:
                imprimir("❌ Error: introduce un número del 0 al 4.", colm["ERROR"])
    
    imprimir("\nFin del programa.", colm["EXIT"])

def menu_principal():
    print()
    imp_marco("""GESTOR DE ARCHIVOS
1. Listar archivos de un directorio
2. Verificar si un archivo existe
3. Crear un nuevo archivo
4. Crear un nuevo directorio
0. Salir""",
    colm["MENU"])

def listar_archivos(ruta = "."):
    try:
        return os.listdir(ruta)
    except FileNotFoundError:
        raise FileNotFoundError

def existe_archivo(nombre):
    return os.path.exists(nombre)

def crear_archivo(nombre):
    return open(nombre, "x")

def crear_directorio(nombre):
    try:
        os.mkdir(nombre)
    except FileExistsError:
        raise FileExistsError
    
def obtener_extension(ruta, archivo):
    if os.path.isdir(ruta+archivo):
        return "dir"
    elif len(archivo.split(".")) == 1:
        return "file"
    else:
        return "." + archivo.split(".")[-1]
    
def colorear(extension):
    if extension == "dir":
        return Fore.MAGENTA
    elif extension == ".txt":
        return Fore.GREEN
    elif extension in [".jpg", ".png"]:
        return Fore.BLUE
    elif extension in [".mp3", ".wav"]:
        return Fore.YELLOW
    else:
        return Fore.WHITE

if __name__ == '__main__':
    main()

'''
Ejercicio 1 - Gestor de Archivos con Python (módulo os)

Desarrollar un programa en Python que permita gestionar archivos y directorios mediante un menú interactivo, utilizando las funciones principales del módulo os.

El programa debe incluir las siguientes funcionalidades:

1. Menú principal con las siguientes opciones:
    Listar archivos del directorio actual
    Verificar si un archivo existe
    Crear un nuevo archivo
    Crear un nuevo directorio
    Salir

2. Implementación de cada opción:
    Listar archivos: Mostrar todos los archivos y carpetas en el directorio actual.
    Verificar existencia: Pedir al usuario un nombre de archivo y comprobar si existe.
    Crear archivo: Solicitar un nombre y generar un archivo vacío.
    Crear directorio: Pedir un nombre y crear una carpeta nueva.

3. Manejo de errores:
    Evitar que el programa falle si el usuario ingresa datos incorrectos.
    Mostrar mensajes claros (ej: "❌ El archivo no existe", "✅ Operación exitosa").

4. Bucle infinito:
    El menú debe mostrarse continuamente hasta que el usuario elija "Salir".
'''

import os
from pathlib import Path

def main():
    os.chdir(Path(__file__).resolve().parent) # Sitúa el cwd en la carpeta del script

    while True:
        menu_principal()
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, introduce un número del 0 al 4.")
            continue

        match opcion:
            case 1:
                print("\nListado de archivos:\n📂 .")
                try:
                    imprimir_arbol()
                except Exception as e:
                    print(f"❌ Error listando el directorio: {e}")
                input("\nPulsa enter para continuar...")
            case 2:
                nombre = input("Indica el archivo a verificar: ").strip()
                if existe_archivo(nombre):
                    print(f"✅ El archivo {nombre} existe.")
                else:
                    print(f"❌ El archivo {nombre} no existe.")
                input("\nPulsa enter para continuar...")
            case 3:
                nombre = input("Indica el nombre del nuevo archivo: ").strip()
                if existe_archivo(nombre):
                    print(f"❌ Error: el archivo {nombre} ya existe")
                else:
                    archivo = crear_archivo(nombre)
                    print(f"✅ Archivo {archivo.name} creado con exito.")
                input("\nPulsa enter para continuar...")
            case 4:
                nombre = input("Indica el nombre de la nueva carpeta: ").strip()
                try:
                    crear_directorio(nombre)
                    print(f"✅ Carpeta {nombre} creada con exito.")
                except FileExistsError:
                    print(f"❌ Error: el archivo {nombre} ya existe")
                input("\nPulsa enter para continuar...")
            case 0:
                print("Saliendo...")
                break
            case _:
                print("Por favor, introduce un número del 0 al 4.")
    
    print("\nFin del programa.")

def menu_principal():
    print("\n--GESTOR DE ARCHIVOS--\n")
    print("1. Listar archivos del directorio actual")
    print("2. Verificar si un archivo existe")
    print("3. Crear un nuevo archivo")
    print("4. Crear un nuevo directorio")
    print("0. Salir\n")

def imprimir_arbol(ruta='.'):
    # Árbol de archivos y carpetas (dirs primero).
    base = Path(ruta)

    def clave_orden(e: os.DirEntry):
        # Ordena carpetas y luego archivos
        tipo = not e.is_dir(follow_symlinks=False)
        nombre = e.name.casefold()
        return (tipo, nombre)

    def _listar(dirpath: Path, prefijo=""):
        # Lista cada paso del arbol
        with os.scandir(dirpath) as iteracion:
            entradas = (e for e in iteracion if not e.name.startswith('.'))
            entradas = sorted(entradas, key=clave_orden)

        total = len(entradas)
        for i, entrada in enumerate(entradas, 1):
            conector = " └" if i == total else " ├"
            if entrada.is_dir():
                print(f"{prefijo}{conector}📂 {entrada.name}")
                extension = "  " if i == total else " │"
                _listar(dirpath / entrada.name, prefijo + extension)
            else:
                print(f"{prefijo}{conector}📄 {entrada.name}")

    try:
        _listar(base)
    except Exception:
        raise Exception

def existe_archivo(nombre):
    return os.path.exists(nombre)

def crear_archivo(nombre):
    return open(nombre, "x")

def crear_directorio(nombre):
    try:
        os.mkdir(nombre)
    except FileExistsError:
        raise FileExistsError

if __name__ == '__main__':
    main()

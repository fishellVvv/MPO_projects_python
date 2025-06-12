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
from xmlrpc.client import boolean
opcion = 0

# Mueve el cwd al directorio del script
os.chdir(os.path.dirname(__file__))

def menu_principal():
    """Imprime el menú principal"""
    print("\n--GESTOR DE ARCHIVOS--\n")
    print("1. Listar archivos del directorio actual")
    print("2. Verificar si un archivo existe")
    print("3. Crear un nuevo archivo")
    print("4. Crear un nuevo directorio")
    print("5. Salir\n")

def listar_archivos():
    """Muestra todos los archivos y carpetas en el directorio actual"""
    try:
        print("\nListado de archivos: ")
        for root, _, files in os.walk('.'):
            nivel = root.count(os.sep)
            indent = ' ' * (nivel * 2)
            if root != '.':
                print(f"{indent}📂 {os.path.basename(root)}/")
            for f in files:
                print(f"{indent}  📄 {f}")
    except Exception as e:
        print(f"❌ Error listando el directorio: {e}")

    input("\nPulsa enter para continuar...")

def verificar_existencia():
    """Solicita un nombre de archivo y comprueba si existe"""
    archivo = input("Indica el archivo a verificar: ").strip()

    if os.path.exists(archivo):
        print(f"✅ El archivo {archivo} existe.")
    else:
        print(f"❌ El archivo {archivo} no existe.")

    input("\nPulsa enter para continuar...")

def crear_archivo():
    """Solicita un nombre y genera un archivo vacío"""
    try:
        nuevo_archivo = input("Indica el nombre del nuevo archivo: ").strip()
        open(nuevo_archivo, "w").close()
        print(f"✅ Archivo {nuevo_archivo} creado con exito.")
    except Exception as e:
        print(f"❌ Error creando el archivo: {e}")

    input("\nPulsa enter para continuar...")

def crear_directorio():
    """Solicita un nombre y crea una carpeta nueva"""
    try:
        nueva_carpeta = input("Indica el nombre de la nueva carpeta: ").strip()
        os.mkdir(nueva_carpeta)
        print(f"✅ Carpeta {nueva_carpeta} creada con exito.")
    except Exception as e:
        print(f"❌ Error creando la carpeta: {e}")

    input("\nPulsa enter para continuar...")

while opcion != 5:
    menu_principal()
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Por favor, introduce un número del 1 al 5.")
        continue

    if opcion == 1:
        listar_archivos()
    elif opcion == 2:
        verificar_existencia()
    elif opcion == 3:
        crear_archivo()
    elif opcion == 4:
        crear_directorio()
    elif opcion < 1 or opcion > 5:
        print("Por favor, introduce un número del 1 al 5.")
    
print("\nFin del programa.")

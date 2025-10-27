# Script que recibe por parámetro una ruta de un archivo e imprime el contenido del mismo

import sys

if len(sys.argv) != 2:
    print("El script debe ejecutarse con la ruta de un archivo por parámetro")
else:
    with open(sys.argv[1], 'r') as file:
        file_lines = file.read()
        print(file_lines)

# PS G:\Otros ordenadores\Mi PC\Drive\04. Estudios\01. FP DAW (Primero)\02. MPO (Python)\MPO_projects_python\UT6_automatizacion\ejercicioClaseContenidoArchivo> python3 contenidoArchivo.py ejemplo.txt
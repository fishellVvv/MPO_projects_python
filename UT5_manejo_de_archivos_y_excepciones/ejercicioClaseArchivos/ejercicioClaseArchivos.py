"""
Programa que lea el archivo sistema_log_extenso.txt
e imprima por pantalla solo los mensajes tipo ERROR
"""

log = open("./UT5_manejo_de_archivos_y_excepciones/ejercicioClaseArchivos/sistema_log_extenso.txt", "r")
log_data = log.readlines()

for line in log_data:
    if "ERROR" in line:
        print(line, end="")

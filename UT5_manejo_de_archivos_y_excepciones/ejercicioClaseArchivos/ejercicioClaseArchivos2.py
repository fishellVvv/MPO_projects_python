# Programa que lea el archivo sistema_log_extenso.txt y copie en otro archivo errores.txt solo los mensajes tipo ERROR

log = open("./UT5_manejo_de_archivos_y_excepciones/ejercicioClaseArchivos/sistema_log_extenso.txt", "r")
log_errores = open("./UT5_manejo_de_archivos_y_excepciones/ejercicioClaseArchivos/errores.txt", "w")
log_data = log.readlines()

for line in log_data:
    if "ERROR" in line:
        log_errores.write(line)

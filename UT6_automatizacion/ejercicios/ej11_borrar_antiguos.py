import os
from datetime import datetime, timedelta

def delete_old(path, del_date):
    if not os.path.exists(path):
        raise FileNotFoundError("El directorio especificado no existe")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} no es un directorio")
    
    try:
        del_datetime = datetime.strptime(del_date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Fecha inválida (usa YYYY-MM-DD): {e}")
    
    removed = []
    for item in os.listdir(path):
        path_item = os.path.join(path, item)
        if not os.path.isfile(path_item):
            continue
            
        file_mtime = os.path.getmtime(path_item)
        file_datetime = datetime.fromtimestamp(file_mtime)

        if (del_datetime - file_datetime) > timedelta(0):
            try:
                os.remove(path_item)
                removed.append(item)
            except Exception as e:
                print(f"No se pudo borrar '{item}': {e}")

    return removed

path = input("Indica la ruta de los ficheros que quieres eliminar:\n")
del_date= input("Indica la fecha desde la que quieres eliminar (YYYY-MM-DD):\n")

try:
    print(delete_old(path, del_date))
except Exception as e:
    print(e)

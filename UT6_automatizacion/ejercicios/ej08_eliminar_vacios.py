import os

def remove_empty(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El directorio especificado no existe")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} no es un directorio")

    removed = []
    for item in os.listdir(path):
        path_item = os.path.join(path, item)
        if os.path.isfile(path_item) and os.path.getsize(path_item) == 0:
            try:
                os.remove(path_item)
                removed.append(item)
            except PermissionError:
                print(f"El archivo {item} no se pudo eliminar (en uso)")

    return removed

path = input("Indica la ruta del directorio:\n")

try:
    print(f"Eliminados: {remove_empty(path)}")
except Exception as e:
    print(e)

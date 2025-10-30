import os

def remove_by_ext(path, ext):
    if not os.path.exists(path):
        raise FileNotFoundError("El directorio especificado no existe")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} no es un directorio")
    
    if ext[0] != "." or len(ext) < 2:
        raise ValueError(f"{ext} no es un formato de extensión válido")

    removed = []
    for item in os.listdir(path):
        path_item = os.path.join(path, item)
        filename, file_ext = os.path.splitext(item)
        if file_ext == ext:
            os.remove(path_item)
            removed.append(item)

    return removed

path = input("Indica la ruta del directorio:\n")
ext = input("Indica la extensión de los archivos a eliminar:\n")

try:
    print(f"Eliminados: {remove_by_ext(path, ext)}")
except Exception as e:
    print(e)

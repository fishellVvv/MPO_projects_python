import os

def count_files(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El directorio especificado no existe")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} no es un directorio")

    counter = 0
    content = os.listdir(path)
    for item in content:
        path_item = os.path.join(path, item)
        if os.path.isfile(path_item):
            counter += 1

    return counter

path = input("Indica la ruta del directorio:\n")

try:
    print(count_files(path))
except Exception as e:
    print(e)

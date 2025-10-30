import os

def remove_empty(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El directorio especificado no existe")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} no es un directorio")

    removed = []
    list_content = os.listdir(path)
    for item in list_content:
        path_item = os.path.join(path, item)
        if os.path.isfile(path_item):
            with open(path_item, "r") as file:
                content = file.read()
                if not content:
                    os.remove(path_item)
                    removed.append(item)

    return removed

path = input("Indica la ruta del directorio:\n")

try:
    print(remove_empty(path))
except Exception as e:
    print(e)

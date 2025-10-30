import os

def delete_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El archivo especificado no existe")
    if os.path.isdir(path):
        raise ValueError(f"{path} es un directorio")
    
    os.remove(path)

    return f"El archivo {path} ha sido eliminado con éxito"
    
path = input("Indica la ruta del fichero que quieres eliminar:\n")

try:
    print(delete_file(path))
except Exception as e:
    print(e)

import os

def rename_file(path, new_name):
    if not os.path.exists(path):
        raise FileNotFoundError("El archivo especificado no existe")
    if not os.path.isfile(path):
        raise IsADirectoryError(f"{path} no es un archivo")
    
    base_new = os.path.basename(new_name)
    if base_new != new_name:
        raise ValueError("El nuevo nombre no debe contener rutas; solo el nombre del archivo.")
    if not base_new.strip():
        raise ValueError("El nuevo nombre no puede estar vacío.")
    
    new_path = os.path.join(os.path.dirname(path), new_name)

    if os.path.exists(new_path):
        raise FileExistsError(f"El archivo {new_path} ya existe")

    os.rename(path, new_path)
    
    return f"El archivo {path} ha sido renombrado como {new_path} con éxito"
    
path = input("Indica la ruta del fichero que quieres renombrar:\n")
new_name = input("Indica el nuevo nombre del fichero:\n")

try:
    print(rename_file(path, new_name))
except Exception as e:
    print(e)

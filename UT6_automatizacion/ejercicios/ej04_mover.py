import os

def move_file(src_path, dest_dir):
    if not os.path.exists(src_path):
        raise FileNotFoundError("El archivo especificado no existe")
    if not os.path.isfile(src_path):
        raise IsADirectoryError(f"{src_path} no es un archivo")
    
    if not os.path.exists(dest_dir):
        raise FileNotFoundError("El directorio de destino no existe")
    if not os.path.isdir(dest_dir):
        raise NotADirectoryError(f"{dest_dir} no es un directorio")
    
    dest_path = os.path.join(dest_dir, os.path.basename(src_path))

    if os.path.exists(dest_path):
        raise FileExistsError(f"El archivo {dest_path} ya existe")
    if os.path.abspath(dest_path) == os.path.abspath(src_path):
        raise ValueError("El destino es el mismo directorio")
    
    os.rename(src_path, dest_path)

    return f"El archivo {src_path} ha sido movido a {dest_dir} con éxito"
    
src_path = input("Indica la ruta del fichero que quieres mover:\n")
dest_dir = input("Indica la ruta a la que lo quieres mover:\n")

try:
    print(move_file(src_path, dest_dir))
except Exception as e:
    print(e)

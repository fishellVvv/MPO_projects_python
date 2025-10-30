import os

def copy_dir_files(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        raise FileNotFoundError("El directorio especificado no existe")
    if not os.path.isdir(src_dir):
        raise NotADirectoryError(f"{src_dir} no es un directorio")
    
    if not os.path.exists(dest_dir):
        raise FileNotFoundError("El directorio de destino no existe")
    if not os.path.isdir(dest_dir):
        raise NotADirectoryError(f"{dest_dir} no es un directorio")
    
    if src_dir == dest_dir:
        raise ValueError("Las rutas son iguales")

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.exists(dest_path):
            raise FileExistsError(f"El archivo {dest_path} ya existe")
        
        # with open(src_path, "r") as src_file, open(dest_path, "w") as dest_file:
        #     dest_file.write(src_file.read())

        with open(src_path, "r") as src_file:
            data = src_file.read()
        with open(dest_path, "w") as dest_file:
            dest_file.write(data)

    return f"Los archivos de {src_dir} han sido movidos a {dest_dir} con éxito"

src_dir = input("Indica la ruta de los ficheros que quieres mover:\n")
dest_dir = input("Indica la ruta a la que los quieres mover:\n")

try:
    print(copy_dir_files(src_dir, dest_dir))
except Exception as e:
    print(e)

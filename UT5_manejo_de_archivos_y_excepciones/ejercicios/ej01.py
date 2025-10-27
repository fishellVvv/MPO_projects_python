import os

def count_lines(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El archivo no existe")
    
    with open(path, 'r') as file:
        return len(file.readlines())

try:
    print(f"El archivo tiene {count_lines('ejemplo.txt')} lineas")
except Exception as e:
    print(e)

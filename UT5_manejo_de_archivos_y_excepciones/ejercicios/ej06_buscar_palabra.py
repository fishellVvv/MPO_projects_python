import os

def find_lines_by_word(path, word):
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe")
    if len(word) == 0:
        raise ValueError("La palabra a reemplazar no puede ser vacía")
    
    with open(path, "r", encoding="utf-8") as file:
        for num, line in enumerate(file, start=1):
            if word in line:
                print(f"{num}: {line}", end="")

path = input("Qué archivo quieres usar?\n")
word = input("Qué palabra quieres buscar?\n")

try:
    find_lines_by_word(path, word)
except Exception as e:
    print(e)

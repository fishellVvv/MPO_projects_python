import os

def find_lines_all_positions(path, word):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"El archivo {path} no existe")
    if not word:
        raise ValueError("La palabra a reemplazar no puede ser vacía")
    
    print(f"\nBuscando '{word}' en '{path}':")
    
    goal = word.lower()
    with open(path, "r", encoding="utf-8") as file:
        for num, line in enumerate(file, start=1):
            text = line.lower()

            i = 0
            while True:
                pos = text.find(goal, i)
                if pos == -1:
                    break
                print(f"línea {num}: posición {pos} ({line.rstrip()})")
                i = pos + 1

path = input("Qué archivo quieres usar?\n")
word = input("Qué palabra quieres buscar?\n")

try:
    find_lines_all_positions(path, word)
except Exception as e:
    print(e)

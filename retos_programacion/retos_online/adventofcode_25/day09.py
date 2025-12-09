def day09(cords):
    print(f"cords: {cords}") # debug

    areas = []
    for a in range(len(cords)):
        for b in range(len(cords)):
            if b > a:
                pair_x = [cords[a][0], cords[b][0]]
                pair_y = [cords[a][1], cords[b][1]]
                len_x = max(pair_x) - min(pair_x) + 1
                len_y = max(pair_y) - min(pair_y) + 1
                areas.append(len_x * len_y)
    print(f"areas: {areas}") # debug

    return max(areas)

def day09b(cords):
    pass

lines = list()
with open("retos_programacion/retos_online/adventofcode_25/day09ex.txt", "r") as f:
    lines = f.read().splitlines()
    cords = []
    for line in lines:
        cords.append([int(n) for n in line.split(",")])

print(day09(cords))
print(day09b(cords))

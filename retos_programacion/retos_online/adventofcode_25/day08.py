from math import sqrt

def calc_dist(cord1, cord2):
    return sqrt(((cord1[0] - cord2[0]) ** 2) + ((cord1[1] - cord2[1]) ** 2) + ((cord1[2] - cord2[2]) ** 2))

def day08(cords):
    result = 1

    distances = []
    for i in range(len(cords)):
        for j in range(len(cords)):
            if j > i:
                distances.append([calc_dist(cords[i], cords[j]), i, j])

    connections = []
    nd = 10
    for dist in sorted(distances):
        if len(connections) < nd:
            connections.append([dist[1], dist[2]])

    print(f"connections:") # debug
    for con in connections:
        print(f"{con}") # debug

    circuits = [[i] for i in range(len(cords))]

    for a, b in connections:
        circ_a = None
        circ_b = None

        for circ in circuits:
            if a in circ:
                circ_a = circ
            if b in circ:
                circ_b = circ

        if circ_a is None or circ_b is None:
            continue

        if circ_a is circ_b:
            continue

        for n in circ_b:
            if n not in circ_a:
                circ_a.append(n)

        circuits.remove(circ_b)

    print(f"circuits:") # debug
    for circ in circuits:
        print(f"{circ}") # debug

    circ_lens = reversed(sorted([len(circ) for circ in circuits]))

    nc = 3
    i = 0
    for cl in circ_lens:
        if i < nc:
            result *= cl
            i += 1

    return result

def day08b(cords):
    result = 0
    
    return result

lines = list()
with open("retos_programacion/retos_online/adventofcode_25/day08ex.txt", "r") as f:
    lines = f.read().splitlines()
    cords = []
    for line in lines:
        cords.append([int(n) for n in line.split(",")])

print(day08(cords))
print(day08b(cords))

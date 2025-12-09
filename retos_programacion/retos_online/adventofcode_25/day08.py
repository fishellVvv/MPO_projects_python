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
    nd = 1000
    for dist in sorted(distances):
        if len(connections) < nd:
            connections.append([dist[1], dist[2]])

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

    circ_lens = reversed(sorted([len(circ) for circ in circuits]))

    nc = 3
    i = 0
    for cl in circ_lens:
        if i < nc:
            result *= cl
            i += 1

    return result

def day08b(cords):
    result = 1

    distances = []
    for i in range(len(cords)):
        for j in range(len(cords)):
            if j > i:
                distances.append([calc_dist(cords[i], cords[j]), i, j])

    connections = []
    for dist in sorted(distances):
        connections.append([dist[1], dist[2]])

    circuits = [[i] for i in range(len(cords))]
    i_last = []
    j_last = []
    for i, j in connections:
        circ_i = None
        circ_j = None

        for circ in circuits:
            if i in circ:
                circ_i = circ
            if j in circ:
                circ_j = circ

        if circ_i is None or circ_j is None:
            continue

        if circ_i is circ_j:
            continue

        for n in circ_j:
            if n not in circ_i:
                circ_i.append(n)

        circuits.remove(circ_j)
        i_last = cords[i]
        j_last = cords[j]

    return i_last[0] * j_last[0]

lines = list()
with open("retos_programacion/retos_online/adventofcode_25/day08.txt", "r") as f:
    lines = f.read().splitlines()
    cords = []
    for line in lines:
        cords.append([int(n) for n in line.split(",")])

print(day08(cords))
print(day08b(cords))

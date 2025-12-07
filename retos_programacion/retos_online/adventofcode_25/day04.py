def cal_adj_pos(matrix, x, y):
    adj = []

    min_x = x-1 if x-1 >= 0 else x
    max_x = x+1 if x+1 <= len(matrix)-1 else x
    min_y = y-1 if y-1 >= 0 else y
    max_y = y+1 if y+1 <= len(matrix[x])-1 else y

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            if i != x or j != y:
                adj.append(matrix[i][j])

    return adj

def day04(matrix):
    result = 0
    print(matrix) # debug
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print(matrix[x][y], end="") # debug
            adjacents = cal_adj_pos(matrix, x, y)
            print(f" -> {adjacents}", end="") # debug
            roll_count = 0
            for r in adjacents:
                if r == "@":
                    roll_count += 1
            print(f" -> {roll_count}") # debug
            if matrix[x][y] == "@" and roll_count < 4:
                result += 1
        print() # debug
    return result

def day04b(matrix):
    pass

lines = list()
with open("retos_programacion/retos_online/adventofcode_25/day04.txt", "r") as f:
    lines = f.readlines()

    matrix = []
    for line in lines:
        line = line.rstrip("\n")
        row = []
        for roll in line:
            row.append(roll)
        matrix.append(row)

print(day04(matrix))
print(day04b(matrix))

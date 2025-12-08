def day07(matrix):
    result = 0
    # for line in matrix: # debug
    #     print(line) # debug

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            match matrix[i][j]:
                case "S":
                    matrix[i+1][j] = "|"
                case "^":
                    if matrix[i-1][j] == "|":
                        matrix[i][j-1] = "|"
                        matrix[i][j+1] = "|"
                        result += 1
                case ".":
                    if matrix[i-1][j] == "|":
                        matrix[i][j] = "|"

    # for line in matrix: # debug
    #     print(line) # debug
    return result

def day07b(matrix):
    pass

lines = list()
with open("retos_programacion/retos_online/adventofcode_25/day07.txt", "r") as f:
    lines = f.read().splitlines()
    matrix = []
    for line in lines:
        row = []
        for ch in line:
            row.append(ch)
        matrix.append(row)

print(day07(matrix))
print(day07b(matrix))

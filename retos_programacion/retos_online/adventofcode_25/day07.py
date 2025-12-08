def day07(matrix):
    result = 0
    
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
    #     for ch in line: # debug
    #         print(ch, end=" ") # debug
    #     print() # debug
    return result

def day07b(matrix):
    result = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            match matrix[i][j]:
                case "S":
                    matrix[i+1][j] = "|"
                case "^":
                    if matrix[i-1][j] == "|":
                        matrix[i][j-1] = "|"
                        matrix[i][j+1] = "|"
                case ".":
                    if matrix[i-1][j] == "|":
                        matrix[i][j] = "|"

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            match matrix[i][j]:
                case "S":
                    matrix[i+1][j] = 1
                case "^":
                    if type(matrix[i-1][j]) == int:
                        if matrix[i][j-1] == "|":
                            matrix[i][j-1] = matrix[i-1][j]
                        elif type(matrix[i][j-1]) == int:
                            matrix[i][j-1] += matrix[i-1][j]
                        
                        if matrix[i][j+1] == "|":
                            matrix[i][j+1] = matrix[i-1][j]
                        elif type(matrix[i][j+1]) == int:
                            matrix[i][j+1] += matrix[i-1][j]
                case "|":
                    if type(matrix[i-1][j]) == int:
                        matrix[i][j] = matrix[i-1][j]
                case int():
                    if type(matrix[i-1][j]) == int:
                        matrix[i][j] += matrix[i-1][j]

    for n in matrix[-1]:
        if type(n) == int:
            result += n

    # for line in matrix: # debug
    #     for ch in line: # debug
    #         print(ch, end=" ") # debug
    #     print() # debug
    return result

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

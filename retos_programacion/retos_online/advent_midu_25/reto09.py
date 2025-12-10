def move_reno(board, moves):
    lines = board.split("\n")[1:-1]
    matrix = []
    reno = [0, 0]
    for i in range(len(lines)):
        new_line = []
        for j in range(len(lines[i])):
            new_line.append(lines[i][j])
            if lines[i][j] == "@":
                reno[0] = i
                reno[1] = j
        matrix.append(new_line)

    for move in moves:
        match move:
            case "L":
                reno[1] -= 1
            case "R":
                reno[1] += 1
            case "U":
                reno[0] -= 1
            case "D":
                reno[0] += 1

        if reno[0] < 0 or reno[0] >= len(matrix) or reno[1] < 0 or reno[1] >= len(matrix[0]):
            return 'crash'
        elif matrix[reno[0]][reno[1]] == "#":
            return 'crash'
        elif matrix[reno[0]][reno[1]] == "*":
            return 'success'

    return 'fail'

board ='''
.....
.*#.*
.@...
.....
'''

print(move_reno(board, 'D'))
# ➞ 'fail' -> se mueve pero no recoge nada
print(move_reno(board, 'U'))
# ➞ 'success' -> recoge algo (*) justo encima
print(move_reno(board, 'RU'))
# ➞ 'crash' -> choca contra un obstáculo (#)
print(move_reno(board, 'RRRUU'))
# ➞ 'success' -> recoge algo (*)
print(move_reno(board, 'DD'))
# ➞ 'crash' -> se choca con la parte de abajo del tablero
print(move_reno(board, 'UUU'))
# ➞ 'success' -> recoge algo del suelo (*) y luego se choca por arriba
print(move_reno(board, 'RR'))
# ➞ 'fail' -> se mueve pero no recoge nada

def day06(lines):
    result = 0
    for i in range(len(lines[0])):
        sum = 0
        prod = 1

        for j in range(len(lines)-1):
            if lines[-1][i] == "+":
                sum += lines[j][i]
            else:
                prod *= lines[j][i]
        
        if lines[-1][i] == "+":
            result += sum
        else:
            result += prod

    return result

def day06b(colums):
    result = 0

    groups = []
    current = []
    for col in colums:
        if all(ch == " " for ch in col):
            if current:
                groups.append(current)
                current = []
        else:
            current.append(col)
    if current:
        groups.append(current)

    problems = []
    for group in groups:
        op = None
        for col in group:
            if col[-1] != " ":
                op = col[-1]
                break

        nums = []
        for col in reversed(group):
            digits = "".join(ch for ch in col[:-1] if ch.isdigit())
            nums.append(int(digits))

        problems.append(nums + [op])

    for problem in problems:
        sum = 0
        prod = 1

        if problem[-1] == "+":
            for num in problem[:-1]:
                sum += num
        else:
            for num in problem[:-1]:
                prod *= num

        if problem[-1] == "+":
            result += sum
        else:
            result += prod
    
    return result

lines = list()
with open("retos_programacion/retos_online/adventofcode_25/day06.txt", "r") as f:
    lines = f.read().splitlines()

    sep_ls = []
    for line in lines[:-1]:
        num_l = [int(n) for n in line.split()]
        sep_ls.append(num_l)
    sig_l = [s for s in lines[-1].split()]
    sep_ls.append(sig_l)

    colums = [[],]
    for l in lines:
        for i, ch in enumerate(l):
            if i >= len(colums):
                colums.append([])
            colums[i].append(ch)

print(day06(sep_ls))
print(day06b(colums))

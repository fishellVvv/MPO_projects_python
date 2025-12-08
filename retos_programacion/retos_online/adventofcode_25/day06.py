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

def day06b(lines):
    result = 0

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
    print(f"lista -> {sep_ls}") # debug

print(day06(sep_ls))
print(day06b(sep_ls))

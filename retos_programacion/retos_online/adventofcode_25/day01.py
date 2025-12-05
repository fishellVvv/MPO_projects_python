def day01(input):
    result = 0
    base = 50

    for line in input:
        num = int(line[1:])
        if line[0] == "R":
            base = (base + num) % 100 
        else:
            base = (base - num) % 100

        if base == 0:
            result += 1

    return result

def day01b(input):
    result = 0
    base = 50

    for line in input:
        num = int(line[1:])
        if line[0] == "R":
            base += num
            if base > 99:
                result += base // 100
                base %= 100 
        else:
            if base == 0:
                result -= 1
            base -= num
            if base <= 0:
                result += (base // -100) + 1
                base %= 100

    return result

input = list()
with open("retos_programacion/retos_online/adventofcode_25/day01.txt", "r") as f:
    input = f.readlines()

print(day01(input))
print(day01b(input))

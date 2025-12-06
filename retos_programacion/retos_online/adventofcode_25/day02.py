def day02(input):
    result = 0
    id_ranges = input.split(",")
    for r in id_ranges:
        rp = [int(p) for p in r.split("-")]
        for i in range(rp[1] - rp[0] + 1):
            n = str(rp[0] + i)
            len_n = len(n)
            l_n = len_n // 2
            if len_n % 2 == 0 and n[:l_n] == n[l_n:]:
                result += int(n)
    return result

def day02b(input):
    result = 0
    id_ranges = input.split(",")
    for r in id_ranges:
        rp = [int(p) for p in r.split("-")]
        for i in range(rp[1] - rp[0] + 1):
            n = str(rp[0] + i)
            len_n = len(n)
            medio = len_n // 2
            for i in range(medio, 0, -1):
                parte = len_n // i
                if len_n % parte == 0 and n == n[:i] * parte:
                    print(n)
                    result += int(n)
                    break
    return result

input = list()
with open("retos_programacion/retos_online/adventofcode_25/day02.txt", "r") as f:
    input = f.read()

print(day02(input))
print(day02b(input))

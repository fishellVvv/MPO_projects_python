def day03(lines):
    result = 0
    for line in lines:
        joltage = 0
        line = line.rstrip("\n")
        nums = [int(n) for n in line]
        joltage = max(nums[:-1])
        for i in range(0, len(line)-1):
            if nums[i] == joltage:
                joltage = (joltage * 10) + max(nums[i+1:])
        result += joltage
    return result

def day03b(lines, batts):
    result = 0

    for line in lines:
        joltage = 0
        joltage_batt = []
        digit = batts

        line = line.rstrip("\n")
        nums = [int(n) for n in line]

        ini = 0
        while digit > 0:
            end = len(nums) - digit + 1

            t_max = max(nums[ini:end])

            for i in range(len(nums[:end])):
                if i >= ini and nums[i] == t_max:
                    new_batt = (nums[i], i, digit)
                    joltage_batt.append(new_batt)
                    ini = i+1
                    break
            digit -= 1

        for batt in joltage_batt:
            joltage = (joltage * 10) + batt[0]
        result += joltage
    return result

lines = list()
with open("retos_programacion/retos_online/adventofcode_25/day03.txt", "r") as f:
    lines = f.readlines()

print(day03(lines))
print(day03b(lines, 12))

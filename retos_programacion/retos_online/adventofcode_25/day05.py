def day05(ranges, nums):
    result = 0
    for n in nums:
        for range in ranges:
            if n >= range[0] and n <= range[1]:
                result += 1
                break
    return result

def day05b_bad_idea(ranges):
    nums = []
    for r in ranges:
        for i in range(r[0], r[1]+1):
            nums.append(i)
    return len(set(nums))

def day05b(ranges):
    ranges = sorted(ranges)
    merged = []

    for start, end in ranges:
        if not merged:
            merged.append([start, end])
        else:
            last_start, last_end = merged[-1]

            if start > last_end + 1:
                merged.append([start, end])
            else:
                if end > last_end:
                    merged[-1][1] = end

    total = 0
    for start, end in merged:
        total += end - start + 1

    return total

lines = list()
with open("retos_programacion/retos_online/adventofcode_25/day05.txt", "r") as f:
    lines = f.read().splitlines()
    sep_index = lines.index('')
    ranges = list(map(lambda range: (int(range.split("-")[0]), int(range.split("-")[1])), lines[:sep_index]))
    nums = [int(n) for n in lines[sep_index + 1:]]

print(day05(ranges, nums))
print(day05b(ranges))

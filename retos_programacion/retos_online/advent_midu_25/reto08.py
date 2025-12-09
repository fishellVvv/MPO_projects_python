def find_unique_toy(toy):
    ch_dict = {}
    for ch in toy:
        if ch.lower() not in ch_dict.keys():
            ch_dict[ch.lower()] = 0
        ch_dict[ch.lower()] += 1

    for ch in toy:
        if ch_dict[ch.lower()] == 1:
            return ch

    return ''

print(find_unique_toy('Gift')) # 'G'
print(find_unique_toy('sS')) # ''
print(find_unique_toy('reindeeR')) # 'i'
print(find_unique_toy('AaBbCc')) # ''
print(find_unique_toy('abcDEF')) # 'a'
print(find_unique_toy('aAaAaAF')) # 'F'
print(find_unique_toy('sTreSS')) # 'T'
print(find_unique_toy('z')) # 'z'

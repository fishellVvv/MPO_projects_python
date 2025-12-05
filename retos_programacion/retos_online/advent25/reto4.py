def decode_santa_pin(code):
    blocks = code[1:-1].split('][')
    digits = []

    for block in blocks:
        if block == '<':
            if not digits:
                return None
            digits.append(digits[-1])
            continue

        d = int(block[0])
        for op in block[1:]:
            if op == "+":
                d = (d + 1) % 10
            elif op == "-":
                d = (d - 1) % 10

        digits.append(str(d))

    if len(digits) != 4:
        return None
    
    return "".join(digits) 

print(decode_santa_pin('[1++][2-][3+][<]')) # "3144"
print(decode_santa_pin('[9+][0-][4][<]')) # "0944"
print(decode_santa_pin('[1+][2-]')) # null
print(decode_santa_pin('[<][2-][9+][0-]')) # null

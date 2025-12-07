from typing import List, Dict

def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    order = []
    counts = {}

    for glove in gloves:
        color = glove["color"]
        hand = glove["hand"]

        if color not in counts:
            counts[color] = {"L": 0, "R": 0}
            order.append(color)

        counts[color][hand] += 1

    result = []
    for color in order:
        left = counts[color]["L"]
        right = counts[color]["R"]
        pairs = min(left, right)

        result.extend([color] * pairs)

    return result

gloves = [
    { "hand": 'L', "color": 'red' },
    { "hand": 'R', "color": 'red' },
    { "hand": 'R', "color": 'green' },
    { "hand": 'L', "color": 'blue' },
    { "hand": 'L', "color": 'green' }
]
print(match_gloves(gloves))

gloves2 = [
  { "hand": 'L', "color": 'gold' },
  { "hand": 'R', "color": 'gold' },
  { "hand": 'L', "color": 'gold' },
  { "hand": 'L', "color": 'gold' },
  { "hand": 'R', "color": 'gold' }
]
print(match_gloves(gloves2))

gloves3 = [
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'blue' }
]
print(match_gloves(gloves3))

gloves6 = [
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'L', "color": 'green' },
  { "hand": 'R', "color": 'red' }
]
print(match_gloves(gloves6))

gloves7 = [
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'L', "color": 'green' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'L', "color": 'green' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'L', "color": 'green' },
  { "hand": 'R', "color": 'red' }
] # ['green', 'red', 'red', 'green', 'red', 'green']
print(match_gloves(gloves6))
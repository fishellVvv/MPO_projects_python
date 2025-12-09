from typing import List, Dict

def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    pairs = []
    singles = []

    for glove in gloves:
        hand = glove["hand"]
        color = glove["color"]

        lost_pair = {"hand": 'R', "color": color} if hand == "L" else {"hand": 'L', "color": color}

        if lost_pair in singles:
            singles.remove(lost_pair)
            pairs.append(color)
        else:
            singles.append(glove)

    return pairs

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
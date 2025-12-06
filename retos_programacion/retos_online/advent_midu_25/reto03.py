def draw_gift(size, symbol):
  lines = []

  if size < 2:
    return ''

  border = symbol * size
  line = symbol + ' ' * (size - 2) + symbol

  lines.append(border)
  for _ in range(size - 2):
    lines.append(line)
  lines.append(border)
  
  result = '\n'.join(lines)
  return result

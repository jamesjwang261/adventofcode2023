f = open('advent11_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]
lines = [[c for c in line] for line in lines]

ncol = len(lines[0])
for i in reversed(range(len(lines))):
  if '#' not in lines[i]:
    lines.insert(i, ['.']*ncol)

nrow = len(lines)
for j in reversed(range(len(lines[0]))):
  col = [lines[i][j] for i in range(nrow)]
  if '#' not in col:
    for i in range(nrow):
      lines[i].insert(j, '.')

# for line in lines:
#   print(''.join(line))

nrow = len(lines)
ncol = len(lines[0])

galaxies = []
for i in range(nrow):
  for j in range(ncol):
    if lines[i][j] == '#':
      galaxies.append((i,j))

res = 0
for i in range(len(galaxies)-1):
  for j in range(i+1, len(galaxies)):
    res += abs(galaxies[i][0] - galaxies[j][0])
    res += abs(galaxies[i][1] - galaxies[j][1])

print(res)

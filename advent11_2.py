f = open('advent11_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]
lines = [[c for c in line] for line in lines]

nrow = len(lines)
ncol = len(lines[0])

row_expansion = set()
col_expansion = set()

for i in range(nrow):
  if '#' not in lines[i]:
    row_expansion.add(i)

for j in range(ncol):
  col = [lines[i][j] for i in range(nrow)]
  if '#' not in col:
    col_expansion.add(j)

galaxies = []
for i in range(nrow):
  for j in range(ncol):
    if lines[i][j] == '#':
      galaxies.append((i,j))

res = 0
expansion = 999999
for i in range(len(galaxies)-1):
  for j in range(i+1, len(galaxies)):
    x1, y1 = galaxies[i]
    x2, y2 = galaxies[j]
    res += abs(x1 - x2) + abs(y1 - y2)
    
    for x in range(min(x1, x2)+1, max(x1, x2)):
      if x in row_expansion:
        res += expansion
        # print(x)
    
    for y in range(min(y1, y2)+1, max(y1, y2)):
      if y in col_expansion:
        res += expansion
        # print(y)

print(res)

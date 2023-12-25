# something went wrong with my logic in trying to figure out
# if a point was an internal point vs external point


f = open('advent10_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]
lines_old = lines.copy()

lines = [[c for c in line] for line in lines]

Sx = -1
Sy = -1
for y in range(len(lines)):
  if 'S' in lines[y]:
    Sx = lines[y].index('S')
    Sy = y
assert lines[Sy][Sx] == 'S'

assert lines[Sy-1][Sx] == '|'
# start by going up
from_dir = 'down'
curX = Sx
curY = Sy-1
while not (curX == Sx and curY == Sy):
  print(curX, curY, from_dir)
  cur_char = lines[curY][curX]
  lines[curY][curX] = 'X'
  match cur_char:
    case '|':
      if from_dir == 'down':
        lines[curY][curX] = 'U'
        curY -= 1
      elif from_dir == 'up':
        lines[curY][curX] = 'D'
        curY += 1
      else:
        print('bad |')
    case '-':
      if from_dir == 'left':
        curX += 1
      elif from_dir == 'right':
        curX -= 1
      else:
        print('bad -')
    case 'L':
      if from_dir == 'up':
        curX += 1
        from_dir = 'left'
      elif from_dir == 'right':
        curY -= 1
        from_dir = 'down'
      else:
        print('bad L')
        break
    case 'J':
      if from_dir == 'left':
        curY -= 1
        from_dir = 'down'
      elif from_dir == 'up':
        curX -= 1
        from_dir = 'right'
      else:
        print('bad J')
    case '7':
      if from_dir == 'down':
        curX -= 1
        from_dir = 'right'
      elif from_dir == 'left':
        curY += 1
        from_dir = 'up'
      else:
        print('bad 7')
    case 'F':
      if from_dir == 'down':
        curX += 1
        from_dir = 'left'
      elif from_dir == 'right':
        curY += 1
        from_dir = 'up'
      else:
        print('bad F')
    case _:
      print('bad match')

lines[Sy][Sx] = 'X'

char_set = set(['X', 'U', 'D'])
for y in range(len(lines)):
  for x in range(len(lines[y])):
    if lines[y][x] not in char_set:
      lines[y][x] = '.'

lines_tmp = [''.join(line) for line in lines]
f = open('test.txt', 'w')
for line in lines_tmp:
  f.write(f'{line}\n')
f.close()

for y in range(len(lines)):
  for x in range(len(lines[y])):
    if lines[y][x] == 'X':
      lines[y][x] = lines_old[y][x]
    elif lines[y][x] == 'U':
      lines[y][x] = 'U'
    elif lines[y][x] == 'D':
      lines[y][x] = 'D'

lines_tmp = [''.join(line) for line in lines]
f = open('test2.txt', 'w')
for line in lines_tmp:
  f.write(f'{line}\n')
f.close()

up_set = set(['J', 'L', 'D'])
area = 0
in_area = False
for y in range(len(lines)):
  for x in range(len(lines[y])):
    if lines[y][x] != '.':
      if lines[y][x] in up_set:
        in_area = not in_area
    elif in_area:
      area += 1

print(area)

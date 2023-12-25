f = open('advent10_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

Sx = -1
Sy = -1
for y in range(len(lines)):
  if 'S' in lines[y]:
    Sx = lines[y].index('S')
    Sy = y
assert lines[Sy][Sx] == 'S'

seen = [(Sx, Sy)]

assert lines[Sy-1][Sx] == '|'
# start by going up
from_dir = 'down'
curX = Sx
curY = Sy-1
while not (curX == Sx and curY == Sy):
  # print(curX, curY, from_dir)
  seen.append((curX, curY))
  match lines[curY][curX]:
    case '|':
      if from_dir == 'down':
        curY -= 1
      elif from_dir == 'up':
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

# shoelace formula
area = seen[0][0] * (seen[1][1] - seen[-1][1])
for i in range(1, len(seen)-1):
    area += seen[i][0] * (seen[i+1][1] - seen[i-1][1])
area += seen[-1][0] * (seen[0][1] - seen[-2][1])
area = abs(area / 2)

# pick's theorem
interior_points = area - (len(seen) // 2) + 1
print(interior_points)

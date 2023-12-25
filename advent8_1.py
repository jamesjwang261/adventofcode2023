f = open('advent8_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

instructions = lines[0]
maps = dict()
for i in range(2, len(lines)):
  line = lines[i]
  source = line[0:3]
  left = line[7:10]
  right = line[12:15]
  maps[source] = (left, right)

cur = 'AAA'
steps = 0
while cur != 'ZZZ':
  s = steps % len(instructions)
  if instructions[s] == 'L':
    cur = maps[cur][0]
  else:
    cur = maps[cur][1]
  steps += 1
  
print(steps)

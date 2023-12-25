f = open('advent8_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

instructions = lines[0]
instructions_length = len(instructions)
maps = dict()
for i in range(2, len(lines)):
  line = lines[i]
  source = line[0:3]
  left = line[7:10]
  right = line[12:15]
  maps[source] = (left, right)

starts = []
for source in maps:
  if source[2] == 'A':
    starts.append(source)

res = []
for cur in starts:
  steps = 0
  while cur[2] != 'Z':
    s = steps % len(instructions)
    if instructions[s] == 'L':
      cur = maps[cur][0]
    else:
      cur = maps[cur][1]
    steps += 1
  
  res.append(steps)

# print(res)


import math

def find_lcm(nums):
  lcm = 1
  for num in nums:
    lcm = lcm * num // math.gcd(lcm, num)
  return lcm


print(find_lcm(res))

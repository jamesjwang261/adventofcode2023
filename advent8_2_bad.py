# brute force solution that i was trying
# not sure what was going on in the for loop and at this point i'm too ltired to figure out


from tqdm import tqdm

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

# fin = []
# for source in maps:
#   if source[2] == 'Z':
#     fin.append(source)
# fin_set = set(fin)

for steps in tqdm(range(10000000000)):
  # print(cur)
  # if set(cur) == fin_set:
  #   break
  # if all([source[2] == 'Z' for source in cur]):
  #   break
  
  # for source in cur:
  #   if source[2] != 'Z':
  #     break
  # 
  # if instructions[steps % instructions_length] == 'L':
  #   cur = [maps[source][0] for source in cur]
  # else:
  #   cur = [maps[source][1] for source in cur]
  
  current_instruction = instructions[steps % instructions_length]
  for i, source in enumerate(cur):
    if source[2] != 'Z':
      break
    if current_instruction == 'L':
      cur[i] = maps[source][0]
    else:
      cur[i] = maps[source][1]
  
  # if cur[0][2] == 'Z' and cur[1][2] == 'Z' and cur[2][2] == 'Z' and cur[3][2] == 'Z' and cur[4][2] == 'Z' and cur[5][2] == 'Z':
  #   break
  # if instructions[steps % instructions_length] == 'L':
  #   cur[0] = maps[cur[0]][0]
  #   cur[1] = maps[cur[1]][0]
  #   cur[2] = maps[cur[2]][0]
  #   cur[3] = maps[cur[3]][0]
  #   cur[4] = maps[cur[4]][0]
  #   cur[5] = maps[cur[5]][0]
  # else:
  #   cur[0] = maps[cur[0]][1]
  #   cur[1] = maps[cur[1]][1]
  #   cur[2] = maps[cur[2]][1]
  #   cur[3] = maps[cur[3]][1]
  #   cur[4] = maps[cur[4]][1]
  #   cur[5] = maps[cur[5]][1]
    
print(steps)

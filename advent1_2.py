f = open('advent1_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
res = 0
for line in lines:
  first_num = -1
  for i in range(len(line)):
    if line[i] in nums or \
        line[i:i+3] == 'one' or \
        line[i:i+3] == 'two' or \
        line[i:i+5] == 'three' or \
        line[i:i+4] == 'four' or \
        line[i:i+4] == 'five' or \
        line[i:i+3] == 'six' or \
        line[i:i+5] == 'seven' or \
        line[i:i+5] == 'eight' or \
        line[i:i+4] == 'nine' or \
        line[i:i+4] == 'zero':
      if line[i] in nums:
        first_num = int(line[i])
      else:
        if line[i:i+3] == 'one':
          first_num = 1
        elif line[i:i+3] == 'two':
          first_num = 2
        elif line[i:i+5] == 'three':
          first_num = 3
        elif line[i:i+4] == 'four':
          first_num = 4
        elif line[i:i+4] == 'five':
          first_num = 5
        elif line[i:i+3] == 'six':
          first_num = 6
        elif line[i:i+5] == 'seven':
          first_num = 7
        elif line[i:i+5] == 'eight':
          first_num = 8
        elif line[i:i+4] == 'nine':
          first_num = 9
        elif line[i:i+4] == 'zero':
          first_num = 0
      break
  
  last_num = -1
  for i in reversed(range(len(line))):
    if line[i] in nums or \
        line[i:i+3] == 'one' or \
        line[i:i+3] == 'two' or \
        line[i:i+5] == 'three' or \
        line[i:i+4] == 'four' or \
        line[i:i+4] == 'five' or \
        line[i:i+3] == 'six' or \
        line[i:i+5] == 'seven' or \
        line[i:i+5] == 'eight' or \
        line[i:i+4] == 'nine' or \
        line[i:i+4] == 'zero':
      if line[i] in nums:
        last_num = int(line[i])
      else:
        if line[i:i+3] == 'one':
          last_num = 1
        elif line[i:i+3] == 'two':
          last_num = 2
        elif line[i:i+5] == 'three':
          last_num = 3
        elif line[i:i+4] == 'four':
          last_num = 4
        elif line[i:i+4] == 'five':
          last_num = 5
        elif line[i:i+3] == 'six':
          last_num = 6
        elif line[i:i+5] == 'seven':
          last_num = 7
        elif line[i:i+5] == 'eight':
          last_num = 8
        elif line[i:i+4] == 'nine':
          last_num = 9
        elif line[i:i+4] == 'zero':
          last_num = 0
      break

  if not first_num or not last_num:
    print('bad line', line)
  res += 10*first_num + last_num

print(res)

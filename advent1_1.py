f = open('advent1_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
res = 0
for line in lines:
  first_num = -1
  for c in line:
    if c in nums:
      first_num = int(c)
      break
  last_num = -1
  for c in reversed(line):
    if c in nums:
      last_num = int(c)
      break
  if not first_num or not last_num:
    print('bad line', line)
  res += 10*first_num + last_num

print(res)

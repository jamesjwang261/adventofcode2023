f = open('advent4_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

res = 0
for line in lines:
  card_num, rest = line.split(': ')
  # num = card_num.split()[-1]
  winning_str, pick_str = rest.split(' | ') 
  winning_nums = set(winning_str.split())
  pick_nums = pick_str.split()
  win_count = 0
  for n in pick_nums:
    if n in winning_nums:
      win_count += 1
  if win_count > 0:
    res += 2**(win_count-1)

print(res)

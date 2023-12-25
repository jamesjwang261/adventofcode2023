f = open('advent4_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

card_counts = {i: 1 for i in range(len(lines))}

for i in range(len(lines)):
  card_num, rest = lines[i].split(': ')
  # num = card_num.split()[-1]
  winning_str, pick_str = rest.split(' | ') 
  winning_nums = set(winning_str.split())
  pick_nums = pick_str.split()
  win_count = 0
  for n in pick_nums:
    if n in winning_nums:
      win_count += 1
  for j in range(i+1, i+1+win_count):
    card_counts[j] += card_counts[i]

# print(card_counts)
print(sum(card_counts.values()))

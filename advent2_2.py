f = open('advent2_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

res = 0
for line in lines:
  game, pull_str = line.split(': ')
  game_idx = int(game.split(' ')[1])
  pulls = pull_str.split('; ')
  r_min = 0
  b_min = 0
  g_min = 0
  for pull in pulls:
    # print(pull)
    draws = pull.strip().split(', ')
    r = 0
    b = 0
    g = 0
    for draw in draws:
      num, color = draw.split()
      if color == 'red':
        r = int(num)
      elif color == 'blue':
        b = int(num)
      elif color == 'green':
        g = int(num)
      else:
        print('invalid color?', line)
    # print(r, b, g)
    r_min = max(r_min, r)
    b_min = max(b_min, b)
    g_min = max(g_min, g)
  # print(r_min, b_min, g_min)
  # print(r_min * b_min * g_min)
  res += r_min * b_min * g_min
    
print(res)

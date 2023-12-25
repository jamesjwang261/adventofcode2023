f = open('advent2_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

res = 0
for line in lines:
  game, pull_str = line.split(': ')
  game_idx = int(game.split(' ')[1])
  pulls = pull_str.split('; ')
  for pull in pulls:
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
    if r > 12 or g > 13 or b > 14:
      break
  else:
    # print(game_idx)
    res += game_idx
    
print(res)

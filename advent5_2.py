f = open('advent5_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]


# seeds: 79 14 55 13
seed_str = lines.pop(0)
seed_ranges = [int(s) for s in seed_str.split()[1:]]
curs = []
for i in range(len(seed_ranges) // 2):
  l = seed_ranges[i*2]
  rge = seed_ranges[i*2+1]
  curs.append((l, l+rge-1))
# print(curs)


for _ in range(7):
  _ = lines.pop(0)
  _ = lines.pop(0)  # map str
  maps = []
  while lines and lines[0] != '':
    maps.append([int(s) for s in lines.pop(0).split()])
  news = []
  # for cur_l, cur_r in curs:
  while curs:
    cur_l, cur_r = curs.pop(0)
    new = (cur_l, cur_r)  # default map

    for b, l, rge in maps:
      # b, l, rge = maps[1]
      r = l+rge-1
      
      # no intersection
      if (r < cur_l) or (cur_r < l):
        continue
      
      # # full containment
      # if (l <= cur_l) and (cur_r <= r):
      #   # do something
      #   pass
      
      # some amount of partial containment
      # left overhang
      if cur_l < l:
        curs.append((cur_l, l-1))  # add left overhang to curs
        cur_l = l
      # right overhang
      if r < cur_r:
        curs.append((r+1, cur_r))  # add right overhang to curs
        cur_r = r
        
      # assert: [cur_l, cur_r] is contained entirely within [l, r]
      if not (l <= cur_l and cur_r <= r):
        print('bad containment???')
      
      # transform range by mapping
      new = (cur_l + (b-l), cur_r + (b-l))
      break
    
    news.append(new)
  curs = news.copy()

best_loc = curs[0][0]
for l, r in curs:
  best_loc = min(best_loc, l)

print(best_loc)

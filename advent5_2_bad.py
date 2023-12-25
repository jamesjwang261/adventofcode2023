# brute force trying to do the seeds one by one
# obviously not going to work lol


f = open('advent5_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]


# seeds: 79 14 55 13
seed_str = lines.pop(0)
seed_ranges = [int(s) for s in seed_str.split()[1:]]
curs = []
for i in range(len(seed_ranges) // 2):
  b = seed_ranges[i*2]
  r = seed_ranges[i*2+1]
  curs.extend(range(b, b+r))
# print(curs)

for i in range(7):
  _ = lines.pop(0)
  _ = lines.pop(0)  # map str
  maps = []
  while lines and lines[0] != '':
    maps.append([int(s) for s in lines.pop(0).split()])
  news = []
  for cur in curs:
    new = cur
    for a, b, r in maps:
      if cur >= b and cur < b + r:
        new = a + (cur - b)
        break
    news.append(new)
  curs = news.copy()

print(min(curs))

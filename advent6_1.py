f = open('advent6_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

time_str = lines[0]
times = [int(s) for s in time_str.split()[1:]]

dist_str = lines[1]
dists = [int(s) for s in dist_str.split()[1:]]

res = 1
for i in range(len(times)):
  time = times[i]
  dist = dists[i]
  # print(i, time, dist)
  ct = 0
  for t in range(time // 2):
    # print(t, t*(time-t))
    if t * (time-t) > dist:
      ct += 2
  if time % 2 == 0:
    if (time//2)**2 > dist:
      ct += 1
  else:
    if (time//2) * (time//2 + 1) > dist:
      ct += 2
  # print(ct)
  res *= ct
  
print(res)

f = open('advent6_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

time_str = lines[0]
time = int(''.join(time_str.split()[1:]))

dist_str = lines[1]
dist = int(''.join(dist_str.split()[1:]))

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
  
print(ct)

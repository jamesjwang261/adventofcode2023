f = open('advent9_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

res = 0
for line in lines:
  nums = [[int(n) for n in line.split()]]
  while not all(n == 0 for n in nums[-1]):
    nums.append([b - a for a, b in zip(nums[-1], nums[-1][1:])])
  
  nums[-1].append(0)
  for i in reversed(range(len(nums)-1)):
    nums[i].append(nums[i][-1] + nums[i+1][-1])
    
  res += nums[0][-1]

print(res)

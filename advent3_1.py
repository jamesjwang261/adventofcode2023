f = open('advent3_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

symbols = ['/', '-', '#', '&', '*', '=', '$', '+', '@', '%']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

res = 0
for i in range(len(lines)):
  line = lines[i]
  j = 0
  while j < len(line):
    if line[j] in nums:
      k = j
      while k < len(line)-1 and line[k+1] in nums:
        k += 1
      # print(j, k)
      has_symbol = False
      if j > 0 and line[j-1] in symbols:
        has_symbol = True
      if k < len(line)-1 and line[k+1] in symbols:
        has_symbol = True
      if i > 0:
        for p in range(max(0,j-1), min(len(line),k+2)):
          if lines[i-1][p] in symbols:
            has_symbol = True
      if i < len(lines)-1:
        # print(max(0,j-1), min(len(line),k+1))
        for p in range(max(0,j-1), min(len(line),k+2)):
          if lines[i+1][p] in symbols:
            has_symbol = True
      if has_symbol:
        # print(int(line[j:k+1]))
        res += int(line[j:k+1])
      j = k
    j += 1
    
print(res)

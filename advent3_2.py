f = open('advent3_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

res = 0
for i in range(len(lines)):
  line = lines[i]
  for j in range(len(line)):
    if line[j] == '*':
      # print('gear', i, j)
      gear_nums = []
      
      # above
      if i > 0:
        pline = lines[i-1]
        if (j > 0 and pline[j-1] in nums) and (pline[j] not in nums) and (j+1 < len(line) and pline[j+1] in nums):
          l = j-1
          while l > 0 and pline[l-1] in nums:
            l -= 1
          gear_nums.append(int(pline[l:j]))
          r = j+1
          while r+1 < len(pline) and pline[r+1] in nums:
            r += 1
          gear_nums.append(int(pline[j+1:r+1]))
        elif j > 0 and pline[j-1] in nums:
          l = j-1
          while l > 0 and pline[l-1] in nums:
            l -= 1
          r = j-1
          while r+1 < len(pline) and pline[r+1] in nums:
            r += 1
          gear_nums.append(int(pline[l:r+1]))
        elif pline[j] in nums:
          r = j
          while r+1 < len(pline) and pline[r+1] in nums:
            r += 1
          gear_nums.append(int(pline[j:r+1]))
        elif j+1 < len(pline) and pline[j+1] in nums:
          r = j+1
          while r+1 < len(pline) and pline[r+1] in nums:
            r += 1
          gear_nums.append(int(pline[j+1:r+1]))
          
      # left
      if j > 0 and line[j-1] in nums:
        l = j-1
        while l > 0 and line[l-1] in nums:
          l -= 1
        gear_nums.append(int(line[l:j]))
        
      # right
      if j+1 < len(line) and line[j+1] in nums:
        r = j+1
        while r+1 < len(line) and line[r+1] in nums:
          r += 1
        gear_nums.append(int(line[j+1:r+1]))
        
      # below
      if i+1 < len(lines):
        pline = lines[i+1]
        if (j > 0 and pline[j-1] in nums) and (pline[j] not in nums) and (j+1 < len(line) and pline[j+1] in nums):
          l = j-1
          while l > 0 and pline[l-1] in nums:
            l -= 1
          gear_nums.append(int(pline[l:j]))
          r = j+1
          while r+1 < len(pline) and pline[r+1] in nums:
            r += 1
          gear_nums.append(int(pline[j+1:r+1]))
        elif j > 0 and pline[j-1] in nums:
          l = j-1
          while l > 0 and pline[l-1] in nums:
            l -= 1
          r = j-1
          while r+1 < len(pline) and pline[r+1] in nums:
            r += 1
          gear_nums.append(int(pline[l:r+1]))
        elif pline[j] in nums:
          r = j
          while r+1 < len(pline) and pline[r+1] in nums:
            r += 1
          gear_nums.append(int(pline[j:r+1]))
        elif j+1 < len(pline) and pline[j+1] in nums:
          r = j+1
          while r+1 < len(pline) and pline[r+1] in nums:
            r += 1
          gear_nums.append(int(pline[j+1:r+1]))
      
      if len(gear_nums) != 2:
        continue
      res += gear_nums[0] * gear_nums[1]

print(res)

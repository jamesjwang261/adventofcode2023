f = open('advent12_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]


def helper(gears, groups):
    # print(gears, groups)
    # groups exhausted, check if there still are bad gears remaining
    if not groups:
        if '#' in gears:
            return 0
        return 1
    
    res = 0
    s = groups[0]
    i = 0
    while i <= len(gears)-s:
        # good gear in desired range, or bad gear in next slot
        if '.' in gears[i:i+s] or (i+s < len(gears) and gears[i+s] == '#'):
            if gears[i] == '#':
                break
            i += 1
        # fill leftmost s slots with bad gears
        else:
            res += helper(gears[i+s+1:], groups[1:])
            # if current leftmost block starts with #, then we cannot have
            # the leftmost block be any further right
            if gears[i] == '#':
                break
            i += 1
    # if res != 0:
    #     print(gears, groups, res)
    return res
   
res_list = []
total = 0
for line in lines:
    gears, groups = line.split()
    groups = [int(s) for s in groups.split(',')]
    tmp = helper(gears, groups)
    res_list.append(tmp)
    total += tmp

print(total)

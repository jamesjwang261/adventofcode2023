f = open('advent13_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

grid = []
grids = []
for i in range(len(lines)):
    if not lines[i]:
        grids.append(grid)
        grid = []
    else:
        grid.append(lines[i])
grids.append(grid)

total = 0
for grid in grids:
    nrow = len(grid)
    ncol = len(grid[0])
    res = -1
    
    # row check
    # print('doing row check')
    for i in range(nrow-1):
        bad_count = 0
        for k in range(0,i+1):
            if i+1+k >= nrow:
                break
            row1 = grid[i-k]
            row2 = grid[i+1+k]
            bad_count += sum(e1 != e2 for e1, e2 in zip(row1, row2))
        # print(i,bad_count)
        if bad_count == 1:
            res = 100 * (i+1)
            break
    if res >= 0:
        total += res
        continue
    
    # col check
    # print('doing col check')
    for i in range(ncol-1):
        bad_count = 0
        for k in range(0,i+1):
            if i+1+k >= ncol:
                break
            col1 = [grid[j][i-k] for j in range(nrow)]
            col2 = [grid[j][i+1+k] for j in range(nrow)]
            bad_count += sum(e1 != e2 for e1, e2 in zip(col1, col2))
        # print(i,bad_count)
        if bad_count == 1:
            res = i+1
            break
    if res >= 0:
        total += res
        continue
    
    print('res = 0?')
    print(grid)
    break

print(total)

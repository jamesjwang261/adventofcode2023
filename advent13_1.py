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
    for i in range(nrow-1):
        good = True
        for k in range(0,i+1):
            if i+1+k < nrow and grid[i-k] != grid[i+1+k]:
                good = False
                break
        if good:
            res = 100 * (i+1)
            break
    if res >= 0:
        total += res
        continue
    
    # col check
    # print('doing col check')
    for i in range(ncol-1):
        good = True
        for k in range(0,i+1):
            if i+1+k >= ncol:
                break
            col1 = [grid[j][i-k] for j in range(nrow)]
            col2 = [grid[j][i+1+k] for j in range(nrow)]
            if not all(a == b for a, b in zip(col1, col2)):
                good = False
                break
        if good:
            res = i+1
            break
    if res >= 0:
        total += res
        continue
    
    print('res = 0?')

print(total)

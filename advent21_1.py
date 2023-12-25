f = open('advent21_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

grid = [[c for c in line] for line in lines]
nrow = len(grid)
ncol = len(grid[0])

Srow = -1
Scol = -1
for row in range(nrow):
    for col in range(ncol):
        if grid[row][col] == 'S':
            Srow = row
            Scol = col
            break

grid[Srow][Scol] = '.'
clean_grid = [grid[row][:] for row in range(nrow)]

grid[Srow][Scol] = 'O'
cur_grid = [grid[row][:] for row in range(nrow)]

for s in range(64):
    next_grid = [clean_grid[row][:] for row in range(nrow)]
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                if row > 0 and next_grid[row-1][col] != '#':
                    next_grid[row-1][col] = 'O'
                if row < nrow-1 and next_grid[row+1][col] != '#':
                    next_grid[row+1][col] = 'O'
                if col > 0 and next_grid[row][col-1] != '#':
                    next_grid[row][col-1] = 'O'
                if col < ncol-1 and next_grid[row][col+1] != '#':
                    next_grid[row][col+1] = 'O'
    cur_grid = [next_grid[row][:] for row in range(nrow)]
    # print(s)
    # print(cur_grid)
    
ct = 0
for row in range(nrow):
    for col in range(ncol):
        if cur_grid[row][col] == 'O':
            ct += 1
print(ct)

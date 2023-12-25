from tqdm import tqdm
from functools import cache

f = open('advent14_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

# transpose lines so that we push everything to the left (so i can use rfind)
grid = tuple([''.join(row) for row in zip(*lines)])
old_grid = grid
nrow = len(grid)
ncol = len(grid[0])


@cache
def cycle(grid):
    grid = list(grid)
    nrow = len(grid)
    ncol = len(grid[0])
    
    for col in range(1, ncol):
        for row in range(nrow):
            if grid[row][col] == 'O':
                last_block = grid[row][:col].rfind('#')
                last_rock = grid[row][:col].rfind('O')
                last_thing = max(last_block, last_rock)
                grid[row] = grid[row][:last_thing+1] + 'O' + grid[row][last_thing+1:col] + grid[row][col+1:]
                
    return tuple([''.join(row) for row in zip(*grid)][::-1])


# keep doing cycles until we get a repeat
seen_grids = {grid: 0}
for i in range(100000000):
    for _ in range(4):
        grid = cycle(grid)
    if grid in seen_grids:
        print(i, seen_grids[grid])
        break
    seen_grids[grid] = i

# i = 177
j = seen_grids[grid]  # j = 93
mod = i - j
starting_rem = j % mod
desired_rem = 1000000000 % mod
# assert desired_rem > starting_rem

grid = old_grid
for i in range(j + (desired_rem - starting_rem)):
    for _ in range(4):
        grid = cycle(grid)

total = 0
for col in range(ncol):
    ct = sum(grid[row][col]=='O' for row in range(nrow))
    total += ct * (ncol - col)

print(total)

f = open('advent14_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

# transpose lines so that we push everything to the left (so i can use rfind)
grid = [''.join(row) for row in zip(*lines)]
old_grid = grid.copy()

nrow = len(grid)
ncol = len(grid[0])

for col in range(1, ncol):
    for row in range(nrow):
        if grid[row][col] == 'O':
            last_block = grid[row][:col].rfind('#')
            last_rock = grid[row][:col].rfind('O')
            last_thing = max(last_block, last_rock)
            grid[row] = grid[row][:last_thing+1] + 'O' + grid[row][last_thing+1:col] + grid[row][col+1:]

total = 0
for col in range(ncol):
    ct = sum(grid[row][col]=='O' for row in range(nrow))
    total += ct * (ncol - col)

print(total)

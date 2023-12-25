f = open('advent23_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

grid = [[c for c in line] for line in lines]
nrow = len(grid)
ncol = len(grid[0])

# total = 0
# for row in range(nrow):
#     for col in range(ncol):
#         if grid[row][col] == 'O':
#             total += 1
# print(total)

# for row in range(1, nrow-1):
#     for col in range(1, ncol-1):
#         if grid[row][col] == '.':
#             paths = 0
#             if grid[row-1][col] == '.':
#                 paths += 1
#             if grid[row+1][col] == '.':
#                 paths += 1
#             if grid[row][col-1] == '.':
#                 paths += 1
#             if grid[row][col+1] == '.':
#                 paths += 1
#             if paths > 2:
#                 print(row, col)
#                 break

# note: there are no places where we have an uncontrolled 3/4-way intersection
# hence, we do not need to worry about a 'seen' grid

todo = [((1, 1), 1, 'D')]  # (row, col), dist, direc

finishing_dists = set()
while todo:
    (row, col), dist, direc = todo.pop()
    if row == nrow-1 and col == ncol-2:
        finishing_dists.add(dist)
        continue
    
    # direction is forced
    if grid[row][col] == '^':
        todo.append(((row-1, col), dist+1, 'U'))
        continue
    elif grid[row][col] == '>':
        todo.append(((row, col+1), dist+1, 'R'))
        continue
    elif grid[row][col] == 'v':
        todo.append(((row+1, col), dist+1, 'D'))
        continue
    elif grid[row][col] == '<':
        todo.append(((row, col-1), dist+1, 'L'))
        continue
    
    # try moving down
    if direc != 'U':
        if not (grid[row+1][col] == '#' or grid[row+1][col] == '^'):
            todo.append(((row+1, col), dist+1, 'D'))
    
    # try moving right
    if direc != 'L':
        if not (grid[row][col+1] == '#' or grid[row][col+1] == '<'):
            todo.append(((row, col+1), dist+1, 'R'))
    
    # try moving up
    if direc != 'D':
        if not (grid[row-1][col] == '#' or grid[row-1][col] == 'v'):
            todo.append(((row-1, col), dist+1, 'U'))
    
    # try moving left
    if direc != 'R':
        if not (grid[row][col-1] == '#' or grid[row][col-1] == '>'):
            todo.append(((row, col-1), dist+1, 'L'))

# print(finishing_dists)
print(max(finishing_dists))

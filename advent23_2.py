# condensed the grid into a graph of intersections
# where edges represent the distance between intersections
# running longest-path on a 34-node graph where max node weight = 4 isn't that bad


f = open('advent23_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

grid = [[c for c in line] for line in lines]
nrow = len(grid)
ncol = len(grid[0])

for row in range(nrow):
    for col in range(ncol):
        if not grid[row][col] == '#':
            grid[row][col] = '.'

# grid_str = [''.join(line) for line in grid]
# f = open('test.txt', 'w')
# for line in grid_str:
#   f.write(f'{line}\n')
# f.close()


def get_neighbors(row, col):
    neighbors = 0
    if grid[row-1][col] == '.':
        neighbors += 1
    if grid[row+1][col] == '.':
        neighbors += 1
    if grid[row][col-1] == '.':
        neighbors += 1
    if grid[row][col+1] == '.':
        neighbors += 1
    return neighbors


intersections = set()
for row in range(1, nrow-1):
    for col in range(1, ncol-1):
        if grid[row][col] == '.':
            neighbors = get_neighbors(row, col)
            if neighbors > 2:
                intersections.add((row, col))
# print(intersections)
n_ints = len(intersections)

int_dict = {}


def walk_until_intersection(row, col, direc):
    dist = 1
    while (row, col) not in intersections:
        # try moving down
        if direc != 'U' and not grid[row+1][col] == '#':
            row += 1
            direc = 'D'
        # try moving right
        elif direc != 'L' and not grid[row][col+1] == '#':
            col += 1
            direc = 'R'
        # try moving up
        elif direc != 'D' and not grid[row-1][col] == '#':
            row -= 1
            direc = 'U'
        # try moving left
        elif direc != 'R' and not grid[row][col-1] == '#':
            col -= 1
            direc = 'L'
        else:
            print('no direction?')
            break
        dist += 1

    return((row, col), dist)


# find starting node
row, col = 1, 1
direc = 'D'
int_dict[0], start_dist = walk_until_intersection(row, col, direc)


# find ending node
row, col = nrow-2, nrow-2
direc = 'U'
int_dict[1], end_dist = walk_until_intersection(row, col, direc)


i = 2
for row, col in intersections:
    if (row, col) != int_dict[0] and (row, col) != int_dict[1]:
        int_dict[i] = (row, col)
        i += 1

idx_dict = {value: key for key, value in int_dict.items()}


edges = [[0] * n_ints for _ in range(n_ints)]

for i in int_dict:
    if i <= 1:
        continue
    irow, icol = int_dict[i]
        
    # try moving up
    if grid[irow-1][icol] == '.':
        row, col = irow-1, icol
        direc = 'U'
        cords, dist = walk_until_intersection(row, col, direc)
        new_idx = idx_dict[cords]
        # if edges[i][new_idx] != 0:
        #     print('check edge weights are same')
        #     print(edges[i][new_idx])
        #     print(dist)
        edges[i][new_idx] = dist
        edges[new_idx][i] = dist
    
    # try moving right
    if grid[irow][icol+1] == '.':
        row, col = irow, icol+1
        direc = 'R'
        cords, dist = walk_until_intersection(row, col, direc)
        new_idx = idx_dict[cords]
        edges[i][new_idx] = dist
        edges[new_idx][i] = dist
    
    # try moving down
    if grid[irow+1][icol] == '.':
        row, col = irow+1, icol
        direc = 'D'
        cords, dist = walk_until_intersection(row, col, direc)
        new_idx = idx_dict[cords]
        edges[i][new_idx] = dist
        edges[new_idx][i] = dist
    
    # try moving left
    if grid[irow][icol-1] == '.':
        row, col = irow, icol-1
        direc = 'L'
        cords, dist = walk_until_intersection(row, col, direc)
        new_idx = idx_dict[cords]
        edges[i][new_idx] = dist
        edges[new_idx][i] = dist
    

# NOTE: assumes that node 0 and node 1 are not connected, which is true


def dfs(cur, visited, dist, max_dist):
    if cur == 1:  # end node
        return max(dist, max_dist)
    
    for neighbor, weight in enumerate(edges[cur]):
        if not visited[neighbor] and weight != 0:
            visited[neighbor] = True
            max_dist = dfs(neighbor, visited, dist + weight, max_dist)
            visited[neighbor] = False

    return max_dist

visited = [False] * n_ints
visited[0] = True

res = dfs(0, visited, 0, 0)


# print(start_dist, res, end_dist)
print(start_dist + res + end_dist)

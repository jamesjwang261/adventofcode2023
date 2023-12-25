f = open('advent16_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

grid = [[c for c in line] for line in lines]
nrow = len(grid)
ncol = len(grid[0])

# left = 1
# right = 2
# down = 4
# up = 8

def do_part1(start):
    todo = [start]

    energized = [[0] * ncol for _ in range(nrow)]
    
    while todo:
        cur_i, cur_j, direc = todo.pop(0)
        # print('todo', todo)
        # print('new from todo', cur_i, cur_j, direc)
        
        while not energized[cur_i][cur_j] & direc:
            # print(cur_i, cur_j, direc)
            energized[cur_i][cur_j] += direc
            
            # figure out new direction
            if grid[cur_i][cur_j] == '/':
                if direc == 2:
                    direc = 8
                elif direc == 1:
                    direc = 4
                elif direc == 4:
                    direc = 1
                elif direc == 8:
                    direc = 2
            elif grid[cur_i][cur_j] == '\\':
                if direc == 2:
                    direc = 4
                elif direc == 1:
                    direc = 8
                elif direc == 4:
                    direc = 2
                elif direc == 8:
                    direc = 1
            elif grid[cur_i][cur_j] == '|':
                if direc == 2 or direc == 1:
                    if cur_i > 0:
                        todo.append((cur_i-1, cur_j, 8))  # do this later
                    direc = 4
            elif grid[cur_i][cur_j] == '-':
                if direc == 4 or direc == 8:
                    if cur_j > 0:
                        todo.append((cur_i, cur_j-1, 1))  # do this later
                    direc = 2
            
            # move in the new direction
            if direc == 2:
                if cur_j < ncol-1:
                    cur_j += 1
                else:
                    break
            elif direc == 1:
                if cur_j > 0:
                    cur_j -= 1
                else:
                    break
            elif direc == 4:
                if cur_i < nrow - 1:
                    cur_i += 1
                else:
                    break
            elif direc == 8:
                if cur_i > 0:
                    cur_i -= 1
                else:
                    break
                
    total = 0
    for i in range(nrow):
        for j in range(ncol):
            if energized[i][j]:
                total += 1
    
    return total

best_total = 0
for j in range(ncol):
    best_total = max(best_total, do_part1((0, j, 4)))
    best_total = max(best_total, do_part1((nrow-1, j, 8)))
for i in range(nrow):
    best_total = max(best_total, do_part1((i, 0, 2)))
    best_total = max(best_total, do_part1((i, nrow-1, 1)))

print(best_total)

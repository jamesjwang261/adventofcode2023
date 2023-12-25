# a holy mess of bodge
# was a fun puzzle trying to piece together the grid


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

MAX_STEPS = nrow*2

# START AT BOTOTOM LEFT
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[-1][0] = 'O'
BL_step_list = [1]
for s in range(MAX_STEPS):
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
    
    ct = 0
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                ct += 1
    BL_step_list.append(ct)
# print(BL_step_list)


# START AT UPPER LEFT
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[0][0] = 'O'
UL_step_list = [1]
for s in range(MAX_STEPS):
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
    
    ct = 0
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                ct += 1
    UL_step_list.append(ct)
# print(UL_step_list)


# START AT UPPER RIGHT
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[0][-1] = 'O'
UR_step_list = [1]
for s in range(MAX_STEPS):
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
    
    ct = 0
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                ct += 1
    UR_step_list.append(ct)
# print(UR_step_list)


# START AT BOTTOM RIGHT
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[-1][-1] = 'O'
BR_step_list = [1]
for s in range(MAX_STEPS):
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
    
    ct = 0
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                ct += 1
    BR_step_list.append(ct)
# print(BR_step_list)


# NOTE: all step lists settle into the same patterns
# print(UL_step_list)
# print(UR_step_list)
# print(BL_step_list)
# print(BR_step_list)



# HOW LONG TO REACH TOP?
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[Srow][Scol] = 'O'
top_steps = -1
top_row = -1
top_col = -1
for s in range(MAX_STEPS):
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
    
    for col in range(ncol):
        if cur_grid[0][col] == 'O':
            top_steps = s + 1
            top_row = 0
            top_col = col
    if top_steps >= 0:
        break
# print(top_steps)
# print(top_row, top_col)


# HOW LONG TO REACH RIGHT?
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[Srow][Scol] = 'O'
right_steps = -1
right_row = -1
right_col = -1
for s in range(MAX_STEPS):
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
    
    for row in range(nrow):
        if cur_grid[row][-1] == 'O':
            right_steps = s + 1
            right_row = row
            right_col = ncol-1
    if right_steps >= 0:
        break
# print(right_steps)
# print(right_row, right_col)


# HOW LONG TO REACH BOT?
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[Srow][Scol] = 'O'
bot_steps = -1
bot_row = -1
bot_col = -1
for s in range(MAX_STEPS):
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
    
    for col in range(ncol):
        if cur_grid[-1][col] == 'O':
            bot_steps = s + 1
            bot_row = nrow-1
            bot_col = col
    if bot_steps >= 0:
        break
# print(bot_steps)
# print(bot_row, bot_col)


# HOW LONG TO REACH LEFT?
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[Srow][Scol] = 'O'
left_steps = -1
left_row = -1
left_col = -1
for s in range(MAX_STEPS):
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
    
    for row in range(nrow):
        if cur_grid[row][0] == 'O':
            left_steps = s + 1
            left_row = row
            left_col = 0
    if left_steps >= 0:
        break
# print(left_steps)
# print(left_row, left_col)


# NOTE: IN FULL GRID, ALL 4 CARDINAL DIRECTIONS FROM S ARE ALL OPEN
# HENCE, SHORTEST PATH TO EDGE IS A STRAIGHT LINE
# THANK GOD OTHERWISE MORE BODGE WOULD BE NEEDED LOL


# START AT BOTTOM MID
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[-1][Scol] = 'O'
B_step_list = [1]
for s in range(MAX_STEPS):
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
    
    ct = 0
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                ct += 1
    B_step_list.append(ct)
# print(B_step_list)


# START AT RIGHT MID
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[Srow][-1] = 'O'
R_step_list = [1]
for s in range(MAX_STEPS):
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
    
    ct = 0
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                ct += 1
    R_step_list.append(ct)
# print(R_step_list)


# START AT UP MID
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[0][Scol] = 'O'
U_step_list = [1]
for s in range(MAX_STEPS):
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
    
    ct = 0
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                ct += 1
    U_step_list.append(ct)
# print(U_step_list)


# START AT LEFT MID
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[Srow][0] = 'O'
L_step_list = [1]
for s in range(MAX_STEPS):
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
    
    ct = 0
    for row in range(nrow):
        for col in range(ncol):
            if cur_grid[row][col] == 'O':
                ct += 1
    L_step_list.append(ct)
# print(L_step_list)


# NOTE: all step lists settle into the same patterns
# print(B_step_list)
# print(R_step_list)
# print(U_step_list)
# print(L_step_list)



TOTAL_STEPS = 26501365

k = (TOTAL_STEPS - 1) // nrow
m = (TOTAL_STEPS - 1) % nrow

even_diag = BR_step_list[2*nrow]
odd_diag = BR_step_list[2*nrow-1]

res = 0
for d in range(1, k-1):
    if d % 2 == 1:
        res += odd_diag * d * 4
    else:
        res += even_diag * d * 4

res += (k-1) * UL_step_list[m + nrow]
res += (k-1) * UR_step_list[m + nrow]
res += (k-1) * BL_step_list[m + nrow]
res += (k-1) * BR_step_list[m + nrow]

res += k * UL_step_list[m]
res += k * UR_step_list[m]
res += k * BL_step_list[m]
res += k * BR_step_list[m]


k = (TOTAL_STEPS - (nrow // 2) - 1) // nrow
m = (TOTAL_STEPS - (nrow // 2) - 1) % nrow

even_ord = B_step_list[2*nrow]
odd_ord = B_step_list[2*nrow-1]

res += (k // 2) * odd_ord * 4
res += ((k-1) // 2) * even_ord * 4

res += B_step_list[m + nrow]
res += L_step_list[m + nrow]
res += U_step_list[m + nrow]
res += R_step_list[m + nrow]

res += B_step_list[m]
res += L_step_list[m]
res += U_step_list[m]
res += R_step_list[m]



# just walk a large odd number of steps on the original grid to see how many get filled
cur_grid = [grid[row][:] for row in range(nrow)]
cur_grid[Srow][Scol] = 'O'
for s in range(2*nrow+1):
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

# grid_str = [''.join(line) for line in cur_grid]
# f = open('test.txt', 'w')
# for line in grid_str:
#   f.write(f'{line}\n')
# f.close()

ct = 0
for row in range(nrow):
    for col in range(ncol):
        if cur_grid[row][col] == 'O':
            ct += 1
# print(ct)


res += ct
print(res)

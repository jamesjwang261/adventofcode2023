from collections import defaultdict

f = open('advent22_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

maxx = 0
maxy = 0
maxz = 0

block_dict = {}  # idx -> (idx_l, idx_r)

for i, line in enumerate(lines):
    l, r = line.split('~')
    lx, ly, lz = l.split(',')
    rx, ry, rz = r.split(',')
    lx, ly, lz = int(lx), int(ly), int(lz)
    rx, ry, rz = int(rx), int(ry), int(rz)
    maxx = max(maxx, lx, rx)
    maxy = max(maxy, ly, ry)
    maxz = max(maxz, lz, rz)
    block_dict[i+1] = ((lx, ly, lz), (rx, ry, rz))
    
grid = [[[0] * (maxz+1) for _ in range(maxy+1)] for _ in range(maxx+1)]

for i in block_dict:
    (lx, ly, lz), (rx, ry, rz) = block_dict[i]
    for x in range(min(lx, rx), max(lx, rx)+1):
        for y in range(min(ly, ry), max(ly, ry)+1):
            for z in range(min(lz, rz), max(lz, rz)+1):
                grid[x][y][z] = i

supported = defaultdict(set)

for sz in range(1, maxz+1):
    for sx in range(maxx+1):
        for sy in range(maxy+1):
            if grid[sx][sy][sz] != 0:
                block_num = grid[sx][sy][sz]
                (lx, ly, lz), (rx, ry, rz) = block_dict[block_num]
                
                # vertical block
                if lz != rz:
                    lz, rz = min(lz, rz), max(lz, rz)
                    new_bot = lz
                    while new_bot > 1 and grid[sx][sy][new_bot-1] == 0:
                        new_bot -= 1
                    fall_dist = lz - new_bot
                    for d in range(fall_dist):
                        grid[sx][sy][rz-d] = 0
                        grid[sx][sy][lz-d-1] = block_num
                    block_dict[block_num] = ((sx, sy, new_bot), (sx, sy, rz-fall_dist))
                    if grid[sx][sy][new_bot-1] != 0:
                        supported[block_num].add(grid[sx][sy][new_bot-1])
                
                elif ly != ry:
                    ly, ry = min(ly, ry), max(ly, ry)
                    new_bot = sz
                    while new_bot > 1:
                        can_fall = True
                        for y in range(ly, ry+1):
                            if grid[sx][y][new_bot-1] != 0:
                                can_fall = False
                                break
                        if not can_fall:
                            break
                        new_bot -= 1
                    for y in range(ly, ry+1):
                        grid[sx][y][sz] = 0
                        grid[sx][y][new_bot] = block_num
                    block_dict[block_num] = ((sx, ly, new_bot), (sx, ry, new_bot))
                    for y in range(ly, ry+1):
                        if grid[sx][y][new_bot-1] != 0:
                            supported[block_num].add(grid[sx][y][new_bot-1])
                
                elif lx != rx:
                    lx, rx = min(lx, rx), max(lx, rx)
                    new_bot = sz
                    while new_bot > 1:
                        can_fall = True
                        for x in range(lx, rx+1):
                            if grid[x][sy][new_bot-1] != 0:
                                can_fall = False
                                break
                        if not can_fall:
                            break
                        new_bot -= 1
                    for x in range(lx, rx+1):
                        grid[x][sy][sz] = 0
                        grid[x][sy][new_bot] = block_num
                    block_dict[block_num] = ((lx, sy, new_bot), (rx, sy, new_bot))
                    for x in range(lx, rx+1):
                        if grid[x][sy][new_bot-1] != 0:
                            supported[block_num].add(grid[x][sy][new_bot-1])
                
                else:  # 1x1x1 block
                    new_bot = sz
                    while new_bot > 1 and grid[sx][sy][new_bot-1] == 0:
                        new_bot -= 1
                    grid[sx][sy][sz] = 0
                    grid[sx][sy][new_bot] = block_num
                    block_dict[block_num] = ((sx, sy, new_bot), (sx, sy, new_bot))
                    if grid[sx][sy][new_bot-1] != 0:
                        supported[block_num].add(grid[sx][sy][new_bot-1])

can_remove = set(range(1, len(block_dict)+1))
for block_num in supported:
    if len(supported[block_num]) == 1:
        num = list(supported[block_num])[0]
        if num in can_remove:
            can_remove.remove(num)

print(len(can_remove))

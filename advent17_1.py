"""
really jank dictionary setup to prevent paths of length more than 3
i figured out a better way to do it in part b,
then basically copy-pasted it to solve part 1 again
see advent17_1_better.py
"""

import heapq


f = open('advent17_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

grid = [[int(c) for c in line] for line in lines]
nrow = len(grid)
ncol = len(grid[0])

end = (nrow-1, ncol-1)

# # start by going right, hardcoded
# queue = [(2, 0, 1, 'r1')]  # dist, cur_i, cur_j, direc
# dist_dict = {(0, 1): {'r1': 2}}
# 
# # start by going down, hardcoded
# queue = [(2, 1, 0, 'd1')]  # dist, cur_i, cur_j, direc
# dist_dict = {(1, 0): {'d1': 2}}

# # start by going right or down
# queue_list = [[(grid[0][1], 0, 1, 'r1')], [(grid[1][0], 1, 0, 'd1')]]
# dist_dict_list = [{(0, 1): {'r1': grid[0][1]}}, {(1, 0): {'d1': grid[1][0]}}]

queue = [(0, 0, 0, 'x0')]  # dist, cur_i, cur_j, direc
dist_dict = {}

while queue:
    cur_dist, cur_i, cur_j, cur_direc = heapq.heappop(queue)
    
    if cur_i == nrow-1 and cur_j == ncol-1:
        # print(cur_dist)
        break
    
    # try to move right
    if cur_direc[0] != 'l' and cur_direc != 'r3' and cur_j < ncol-1:
        if cur_direc[0] != 'r':
            new_direc = 'r1'
        elif cur_direc == 'r1':
            new_direc = 'r2'
        elif cur_direc == 'r2':
            new_direc = 'r3'
        
        new_cord = (cur_i, cur_j+1)
        
        new_dist = cur_dist + grid[new_cord[0]][new_cord[1]]
        if new_cord not in dist_dict:
            dist_dict[new_cord] = {new_direc: new_dist}
            heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
        elif new_direc not in dist_dict[new_cord] or new_dist < dist_dict[new_cord][new_direc]:
            dist_dict[new_cord][new_direc] = new_dist
            heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
    
    # try to move left
    if cur_direc[0] != 'r' and cur_direc != 'l3' and cur_j > 0:
        if cur_direc[0] != 'l':
            new_direc = 'l1'
        elif cur_direc == 'l1':
            new_direc = 'l2'
        elif cur_direc == 'l2':
            new_direc = 'l3'
            
        new_cord = (cur_i, cur_j-1)
       
        new_dist = cur_dist + grid[new_cord[0]][new_cord[1]]
        if new_cord not in dist_dict:
            dist_dict[new_cord] = {new_direc: new_dist}
            heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
        elif new_direc not in dist_dict[new_cord] or new_dist < dist_dict[new_cord][new_direc]:
            dist_dict[new_cord][new_direc] = new_dist
            heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
            
    # try to move up
    if cur_direc[0] != 'd' and cur_direc != 'u3' and cur_i > 0:
        if cur_direc[0] != 'u':
            new_direc = 'u1'
        elif cur_direc == 'u1':
            new_direc = 'u2'
        elif cur_direc == 'u2':
            new_direc = 'u3'
            
        new_cord = (cur_i-1, cur_j)
       
        new_dist = cur_dist + grid[new_cord[0]][new_cord[1]]
        if new_cord not in dist_dict:
            dist_dict[new_cord] = {new_direc: new_dist}
            heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
        elif new_direc not in dist_dict[new_cord] or new_dist < dist_dict[new_cord][new_direc]:
            dist_dict[new_cord][new_direc] = new_dist
            heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
            
    # try to move down
    if cur_direc[0] != 'u' and cur_direc != 'd3' and cur_i < nrow-1:
        if cur_direc[0] != 'd':
            new_direc = 'd1'
        elif cur_direc == 'd1':
            new_direc = 'd2'
        elif cur_direc == 'd2':
            new_direc = 'd3'
            
        new_cord = (cur_i+1, cur_j)
       
        new_dist = cur_dist + grid[new_cord[0]][new_cord[1]]
        if new_cord not in dist_dict:
            dist_dict[new_cord] = {new_direc: new_dist}
            heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
        elif new_direc not in dist_dict[new_cord] or new_dist < dist_dict[new_cord][new_direc]:
            dist_dict[new_cord][new_direc] = new_dist
            heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))

print(cur_dist)

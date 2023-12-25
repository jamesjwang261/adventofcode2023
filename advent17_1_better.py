# improved solution that is an easier case of 17_2


import heapq


f = open('advent17_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

grid = [[int(c) for c in line] for line in lines]
nrow = len(grid)
ncol = len(grid[0])

end = (nrow-1, ncol-1)

queue = [(0, 0, 0, 'x')]
dist_dict = {}

while queue:
    cur_dist, cur_i, cur_j, cur_direc = heapq.heappop(queue)
    # print(cur_dist, cur_i, cur_j, cur_direc)
    
    if cur_i == nrow-1 and cur_j == ncol-1:
        # print(cur_dist)
        break
    
    # try to move right
    if cur_direc != 'r' and cur_direc != 'l':
        new_direc = 'r'
        new_dist = cur_dist
        for move in range(1, 4):
            if cur_j + move >= ncol:
                break
            new_cord = (cur_i, cur_j + move)
        
            new_dist += grid[new_cord[0]][new_cord[1]]
            if new_cord not in dist_dict:
                dist_dict[new_cord] = {new_direc: new_dist}
                heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
            elif new_direc not in dist_dict[new_cord] or new_dist < dist_dict[new_cord][new_direc]:
                dist_dict[new_cord][new_direc] = new_dist
                heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
    
    # try to move left
    if cur_direc != 'l' and cur_direc != 'r':
        new_direc = 'l'
        new_dist = cur_dist
        for move in range(1, 4):
            if cur_j - move < 0:
                break
            new_cord = (cur_i, cur_j - move)
        
            new_dist += grid[new_cord[0]][new_cord[1]]
            if new_cord not in dist_dict:
                dist_dict[new_cord] = {new_direc: new_dist}
                heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
            elif new_direc not in dist_dict[new_cord] or new_dist < dist_dict[new_cord][new_direc]:
                dist_dict[new_cord][new_direc] = new_dist
                heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
           
    # try to move up
    if cur_direc != 'u' and cur_direc != 'd':
        new_direc = 'u'
        new_dist = cur_dist
        for move in range(1, 4):
            if cur_i - move < 0:
                break
            new_cord = (cur_i - move, cur_j)
        
            new_dist += grid[new_cord[0]][new_cord[1]]
            if new_cord not in dist_dict:
                dist_dict[new_cord] = {new_direc: new_dist}
                heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
            elif new_direc not in dist_dict[new_cord] or new_dist < dist_dict[new_cord][new_direc]:
                dist_dict[new_cord][new_direc] = new_dist
                heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
            
    # try to move down
    if cur_direc != 'd' and cur_direc != 'u':
        new_direc = 'd'
        new_dist = cur_dist
        for move in range(1, 4):
            if cur_i + move >= nrow:
                break
            new_cord = (cur_i + move, cur_j)
        
            new_dist += grid[new_cord[0]][new_cord[1]]
            if new_cord not in dist_dict:
                dist_dict[new_cord] = {new_direc: new_dist}
                heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
            elif new_direc not in dist_dict[new_cord] or new_dist < dist_dict[new_cord][new_direc]:
                dist_dict[new_cord][new_direc] = new_dist
                heapq.heappush(queue, (new_dist, new_cord[0], new_cord[1], new_direc))
    
    # print(queue)
    # print(dist_dict)

print(cur_dist)

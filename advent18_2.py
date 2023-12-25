f = open('advent18_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

cur_x = 0
cur_y = 0
points = [(cur_x, cur_y)]
perimeter = 0
for line in lines:
    _, _, hex_str = line.split()
    hex_num = hex_str[2:7]
    dist = int(hex_num, 16)
    direc = hex_str[7] 
    if direc == '0':
        cur_x += dist
    elif direc == '1':
        cur_y += dist
    elif direc == '2':
        cur_x -= dist
    elif direc == '3':
        cur_y -= dist
    points.append((cur_x, cur_y))
    perimeter += dist


# CODE TO VIEW THE GRID

# trans_points = []
# max_x = 0
# max_y = 0
# for x, y in points:
#     trans_points.append((x - min_x, y - min_y))
#     max_x = max(max_x, x - min_x)
#     max_y = max(max_y, y - min_y)
# 
# grid = [['.'] * (max_x+1) for _ in range(max_y+1)]
# for i in range(len(trans_points)-1):
#     x1, y1 = trans_points[i]
#     x2, y2 = trans_points[i+1]
#     for x in range(min(x1, x2), max(x1, x2)+1):
#         for y in range(min(y1, y2), max(y1, y2) + 1):
#             grid[y][x] = '#'
# 
# grid_str = [''.join(line) for line in grid]
# f = open('test.txt', 'w')
# for line in grid_str:
#   f.write(f'{line}\n')
# f.close()
# 
# nrow = len(grid)
# ncol = len(grid[0])


# grid_str = [''.join(line) for line in grid]
# f = open('test2.txt', 'w')
# for line in grid_str:
#   f.write(f'{line}\n')
# f.close()


# shoelace formula calculates area given the middle of squares

points.append(points[1])  # for convenience, P[n] = P[0] and P[n+1] = P[1]

area = 0
for i in range(1, len(points)-1):
    area += points[i][0] * (points[i-1][1] - points[i+1][1])
area = abs(area / 2)
# print(area)

int_points = area - (perimeter / 2) + 1  # pick's theorem gives us internal area
print(int_points + perimeter)  # total area = interior + perimeter

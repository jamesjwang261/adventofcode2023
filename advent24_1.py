f = open('advent24_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

# 212542581053874, 357959731032403, 176793474286781 @ -88, -256, -240
vecs = []
for line in lines:
    pos, vel = line.split(' @ ')
    px, py, pz = pos.split(', ')
    vx, vy, vz = vel.split(', ')
    vecs.append(((int(px), int(py)), (int(vx), int(vy))))


def find_collision_point(vec1, vec2):
    (x1, y1), (vx1, vy1) = vec1
    (x2, y2), (vx2, vy2) = vec2
    
    denom = vx1*vy2 - vx2*vy1
    # print('denom', denom)
    if denom == 0:
        return None
    
    t1 = vx2*(y1-y2) + vy2*(x2-x1)
    t1 /= denom
    t2 = vy1*(x2-x1) + vx1*(y1-y2)
    t2 /= denom
    # print('t1', t1)
    # print('t2', t2)
    
    if t1 < 0 or t2 < 0:
        return None
    
    return (x1 + t1*vx1, y1+t1*vy1)
    

MIN_COORD = 200000000000000
MAX_COORD = 400000000000000
total = 0
for i in range(len(vecs)-1):
    for j in range(i+1, len(vecs)):
        vec1 = vecs[i]
        vec2 = vecs[j]
        res = find_collision_point(vec1, vec2)
        if not res:
            continue
        rx, ry = res
        if MIN_COORD <= rx <= MAX_COORD and MIN_COORD <= ry <= MAX_COORD:
            total += 1
            
print(total)

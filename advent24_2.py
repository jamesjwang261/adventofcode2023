from sympy import symbols, solve

f = open('advent24_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

# 212542581053874, 357959731032403, 176793474286781 @ -88, -256, -240
vecs = []
for line in lines:
    pos, vel = line.split(' @ ')
    px, py, pz = pos.split(', ')
    vx, vy, vz = vel.split(', ')
    vecs.append(((int(px), int(py), int(pz)), (int(vx), int(vy), int(vz))))

n = 3

x0, y0, z0, vx0, vy0, vz0 = symbols('x0 y0 z0 vx0 vy0 vz0')
t = symbols(f't0:{n}')

equations = []
for i in range(n):
    (x1, y1, z1), (vx1, vy1, vz1) = vecs[i]
    equations.append((x0 + vx0 * t[i])-(x1 + vx1 * t[i]))
    equations.append((y0 + vy0 * t[i])-(y1 + vy1 * t[i]))
    equations.append((z0 + vz0 * t[i])-(z1 + vz1 * t[i]))

solution = solve(equations, (x0, y0, z0, vx0, vy0, vz0, *t))


# verifying that the solution works for all vectors
# (kind of suprised it just works lol)
x0, y0, z0, vx0, vy0, vz0, *t = solution[0]
x0, y0, z0 = int(x0), int(y0), int(z0)
vx0, vy0, vz0 = int(vx0), int(vy0), int(vz0)

times = []
for i in range(len(vecs)):
    (x1, y1, z1), (vx1, vy1, vz1) = vecs[i]
    
    tx, ty, tz = None, None, None
    
    if vx0 - vx1 != 0:
        tx = (x1 - x0) / (vx0 - vx1)
    
    if vy0 - vy1 != 0:
        ty = (y1 - y0) / (vy0 - vy1)
    
    if vz0 - vz1 != 0:
        tz = (z1 - z0) / (vz0 - vz1)
    
    if (tx and ty and tx != ty) or (tx and tz and tx != tz) or (ty and tz and ty != tz):
        print('unequal ts {i}')
        print(tx, ty, tz)
        break
    
    if tx: 
        times.append(tx)
    elif ty:
        times.append(ty)
    elif tz:
        times.append(tz)
    else:
        print(f'no times? {i}')


print(x0 + y0 + z0)

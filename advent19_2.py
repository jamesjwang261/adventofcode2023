# basically the same as 5_2


f = open('advent19_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

workflows = {}
for line in lines:
    if line == '':
        break
    name, rest = line.split('{')
    toks = rest.split(',')
    rules = []
    for tok in toks[:-1]:
        ineq, dest = tok.split(':')
        l = ineq[0]
        d = ineq[1]
        num = int(ineq[2:])
        rules.append((l, d, num, dest))
    rules.append(toks[-1][:-1])
    workflows[name] = rules

res = []
todo = [(('in', 0), [(1, 4000), (1, 4000), (1, 4000), (1, 4000)])]
while todo:
    (cur, idx), ranges = todo.pop(0)
    # print(cur, idx, ranges)
    (x_min, x_max), (m_min, m_max), (a_min, a_max), (s_min, s_max) = ranges
    
    if cur == 'A':
        res.append(ranges)
        continue
    elif cur == 'R':
        continue
    
    if idx == len(workflows[cur])-1:
        if workflows[cur][idx] == 'A':
            res.append(ranges)
        elif workflows[cur][idx] == 'R':
            pass
        else:
            todo.append(((workflows[cur][idx], 0), ranges))
        continue
    
    l, d, num, dest = workflows[cur][idx]
    if l == 'x':
        if d == '<':
            if x_min >= num:
                todo.append(((cur, idx+1), ranges))  # decline
            elif x_max < num:
                todo.append(((dest, 0), ranges))  # accept
            else:
                ranges[0] = (num, x_max)
                todo.append(((cur, idx+1), ranges.copy()))  # decline
                ranges[0] = (x_min, num-1)
                todo.append(((dest, 0), ranges))  # accept
        elif d == '>':
            if x_max <= num:
                todo.append(((cur, idx+1), ranges))  # declinne
            elif x_min > num:
                todo.append(((dest, 0), ranges))  # accept
            else:
                ranges[0] = (x_min, num)
                todo.append(((cur, idx+1), ranges.copy()))  # decline
                ranges[0] = (num+1, x_max)
                todo.append(((dest, 0), ranges))  # accept
    elif l == 'm':
        if d == '<':
            if m_min >= num:
                todo.append(((cur, idx+1), ranges))  # decline
            elif m_max < num:
                todo.append(((dest, 0), ranges))  # accept
            else:
                ranges[1] = (num, m_max)
                todo.append(((cur, idx+1), ranges.copy()))  # decline
                ranges[1] = (m_min, num-1)
                todo.append(((dest, 0), ranges))  # accept
        elif d == '>':
            if m_max <= num:
                todo.append(((cur, idx+1), ranges))  # declinne
            elif m_min > num:
                todo.append(((dest, 0), ranges))  # accept
            else:
                ranges[1] = (m_min, num)
                todo.append(((cur, idx+1), ranges.copy()))  # decline
                ranges[1] = (num+1, m_max)
                todo.append(((dest, 0), ranges))  # accept
    elif l == 'a':
        if d == '<':
            if a_min >= num:
                todo.append(((cur, idx+1), ranges))  # decline
            elif a_max < num:
                todo.append(((dest, 0), ranges))  # accept
            else:
                ranges[2] = (num, a_max)
                todo.append(((cur, idx+1), ranges.copy()))  # decline
                ranges[2] = (a_min, num-1)
                todo.append(((dest, 0), ranges))  # accept
        elif d == '>':
            if a_max <= num:
                todo.append(((cur, idx+1), ranges))  # declinne
            elif a_min > num:
                todo.append(((dest, 0), ranges))  # accept
            else:
                ranges[2] = (a_min, num)
                todo.append(((cur, idx+1), ranges.copy()))  # decline
                ranges[2] = (num+1, a_max)
                todo.append(((dest, 0), ranges))  # accept
    elif l == 's':
        if d == '<':
            if s_min >= num:
                todo.append(((cur, idx+1), ranges))  # decline
            elif s_max < num:
                todo.append(((dest, 0), ranges))  # accept
            else:
                ranges[3] = (num, s_max)
                todo.append(((cur, idx+1), ranges.copy()))  # decline
                ranges[3] = (s_min, num-1)
                todo.append(((dest, 0), ranges))  # accept
        elif d == '>':
            if s_max <= num:
                todo.append(((cur, idx+1), ranges))  # declinne
            elif s_min > num:
                todo.append(((dest, 0), ranges))  # accept
            else:
                ranges[3] = (s_min, num)
                todo.append(((cur, idx+1), ranges.copy()))  # decline
                ranges[3] = (num+1, s_max)
                todo.append(((dest, 0), ranges))  # accept

total = 0
for ranges in res:
    tmp = (ranges[0][1]-ranges[0][0]+1) * (ranges[1][1]-ranges[1][0]+1) * (ranges[2][1]-ranges[2][0]+1) * (ranges[3][1]-ranges[3][0]+1)
    # print(tmp)
    total += tmp
print(total)

f = open('advent19_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

workflows = {}
ratings = []
on_ratings = False
for line in lines:
    if line == '':
        on_ratings = True
    elif not on_ratings:
        name, rest = line.split('{')
        toks = rest.split(',')
        rules = []
        for tok in toks[:-1]:
            rules.append(tok.split(':'))
        rules.append(['True', toks[-1][:-1]])
        workflows[name] = rules
    else:
        x_str, m_str, a_str, s_str = line[1:-1].split(',')
        ratings.append([int(x_str[2:]), int(m_str[2:]), int(a_str[2:]), int(s_str[2:])])

total = 0
for x, m, a, s in ratings:
    cur = 'in'
    while not (cur == 'A' or cur == 'R'):
        for rule in workflows[cur]:
            if eval(rule[0]):
                cur = rule[1]
                break
    if cur == 'A':
        # print(x, m, a, s)
        total += x + m + a + s

print(total)

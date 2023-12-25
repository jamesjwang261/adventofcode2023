f = open('advent20_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

flipflops = {}
conjunctions = {}
for line in lines:
    if 'broadcaster' in line:
        toks = line.split()
        broadcaster = tuple(tok.strip(',') for tok in toks[2:])
    else:
        toks = line.split()
        switch_type = toks[0][0]
        name = toks[0][1:]
        dests = tuple(tok.strip(',') for tok in toks[2:])
        if switch_type == '%':
            flipflops[name] = [False, dests]
        else:
            conjunctions[name] = [{}, dests]

for name in flipflops:
    for dest in flipflops[name][1]:
        if dest in conjunctions:
            conjunctions[dest][0][name] = False

for name in conjunctions:
    for dest in conjunctions[name][1]:
        if dest in conjunctions:
            conjunctions[dest][0][name] = False

cts = [0, 0]
for i in range(1000):
    # button -low-> broadcaster
    cts[0] += 1
    
    # broadcaster -low-> receivers
    todo = []
    for name in broadcaster:
        todo.append((name, False, None))  # dest, sig, origin
        cts[0] += 1
    
    while todo:
        name, sig, origin = todo.pop(0)
        if name in flipflops:
            if sig:  # high signal
                pass
            else:  # low signal
                new_sig = not flipflops[name][0]
                flipflops[name][0] = new_sig
                for dest in flipflops[name][1]:
                    todo.append((dest, new_sig, name))
                    cts[new_sig] += 1
        elif name in conjunctions:
            conjunctions[name][0][origin] = sig
            new_sig = True
            if all(val for val in conjunctions[name][0].values()):  # if all high
                new_sig = False
            for dest in conjunctions[name][1]:
                todo.append((dest, new_sig, name))
                cts[new_sig] += 1
        else:
            # sending into the void i guess
            # print(name, sig, origin)
            pass

# print(cts)
print(cts[0] * cts[1])

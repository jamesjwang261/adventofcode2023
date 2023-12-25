f = open('advent15_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

line = lines[0]
toks = line.split(',')

total = 0
for tok in toks:
    val = 0
    for c in tok:
        val += ord(c)
        val *= 17
        val %= 256
    total += val
    
print(total)

f = open('advent15_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

line = lines[0]
toks = line.split(',')

def my_hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val

boxes = [{} for _ in range(256)]

for tok in toks:
    if tok[-1] == '-':
        label = tok[:-1]
        label_hash = my_hash(label)
        if label in boxes[label_hash]:
            del boxes[label_hash][label]
        continue
    # equal sign op
    label = tok[:-2]
    label_hash = my_hash(label)
    foc = int(tok[-1])
    boxes[label_hash][label] = foc

total = 0
for i, box in enumerate(boxes):
    for j, (k, v) in enumerate(box.items()):
        total += (i+1) * (j+1) * v

print(total)

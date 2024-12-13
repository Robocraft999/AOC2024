from helpers import *
path, testpath = get_input(9)

res = 0
text = parse_as_text(path)
blocks = {}
spaces = {}
space = False
id = 0
pos = 0
for i, c in enumerate(text):
    if space:
        spaces[pos] = int(c)
    else:
        blocks[(id, pos)] = int(c)
        id += 1
    pos += int(c)
    space = not space

for free_space in spaces.keys():
    amount = spaces[free_space]
    removes = set()
    adds = set()
    offset = free_space
    full = False
    for (id, pos) in sorted(blocks.keys(), key=lambda x: x[-1], reverse=True):
        if offset > pos:
            full = True
            break
        block_size = blocks[(id, pos)]
        if amount >= block_size:
            spaces[free_space] -= block_size
            adds.add(((id, offset), block_size))
            removes.add((id, pos))
            offset += block_size
            amount -= block_size
            continue
        else:
            if amount == 0:
                break
            spaces[free_space] -= amount
            adds.add(((id, offset), amount))
            blocks[(id, pos)] -= amount
            break
    for remove in removes:
        blocks.pop(remove)
    for (add, amount) in adds:
        blocks[add] = amount
    if full:
        break

for id, block in sorted(blocks.keys(), key=lambda x: x[-1]):
    for i in range(blocks[(id, block)]):
        res += (block + i) * id
print(res)
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

changes = set()
for (id, pos) in sorted(blocks.keys(), reverse=True):
    if id == 0:
        break
    block_size = blocks[(id, pos)]
    changed = set()
    for free_space in sorted(spaces.keys()):
        amount = spaces[free_space]
        if free_space > pos:
            break
        if amount >= block_size:
            changes.add(((id, pos), free_space))
            changed.add((free_space, amount-block_size, free_space+block_size))
            changed.add((None, block_size, pos))
            break
    for old_pos, new_amount, new_pos in changed:
        if old_pos:
            spaces.pop(old_pos)
        if new_amount > 0:
            spaces[new_pos] = new_amount

    new_spaces = {}
    last_space = None
    for free_space in sorted(spaces.keys()):
        if not last_space:
            last_space = free_space
            new_spaces[free_space] = spaces[free_space]
            continue
        last_amount = new_spaces[last_space]
        amount = spaces[free_space]
        if last_space + last_amount == free_space:
            new_spaces[last_space] += amount
        else:
            new_spaces[free_space] = amount
            last_space = free_space
    spaces = new_spaces

for (change, new_pos) in changes:
    l = blocks.pop(change)
    blocks[(change[0], new_pos)] = l

for id, block in sorted(blocks.keys(), key=lambda x: x[-1]):
    for i in range(blocks[(id, block)]):
        res += (block + i) * id
print(res)
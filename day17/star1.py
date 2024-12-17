from helpers import *
path, testpath = get_input(17)

res = 0
upper, lower = parse_as_two_parts(path, lambda x: splitmap(x, char=": ", mapper=lambda x: x), lambda x: splitmap(x, char=": ", mapper=lambda x: x))

registers = []
for l, r in upper:
    registers.append(int(r))
instructions = list(map(int, lower[0][1].split(",")))
operands = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: registers[0],
    5: registers[1],
    6: registers[2],
}
pc = 0
res = []
while pc < len(instructions):
    op = instructions[pc]
    literal = instructions[pc+1]
    if 3 >= literal >= 0:
        combo = literal
    elif literal == 4:
        combo = registers[0]
    elif literal == 5:
        combo = registers[1]
    elif literal == 6:
        combo = registers[2]
    if op == 0:
        print("adv", int(registers[0] / pow(2, combo)))
        registers[0] = int(registers[0] / pow(2, combo))
    elif op == 1:
        print("bxl", registers[1] ^ literal)
        registers[1] = registers[1] ^ literal
    elif op == 2:
        print("bst")
        registers[1] = combo % 8
    elif op == 3:
        print("jnz", literal)
        if registers[0] != 0:
            pc = literal
            continue
    elif op == 4:
        print("bxc")
        registers[1] = registers[1] ^ registers[2]
    elif op == 5:
        print("out", combo % 8)
        res.append(str(combo % 8))
    elif op == 6:
        print("bdv")
        registers[1] = int(registers[0] / pow(2, combo))
    elif op == 7:
        print("cdv")
        registers[2] = int(registers[0] / pow(2, combo))
    else:
        print(op, combo, pc)
    pc += 2
print(",".join(res))
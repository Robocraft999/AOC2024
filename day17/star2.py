from helpers import *
from tqdm import tqdm
path, testpath = get_input(17)

res = 0
upper, lower = parse_as_two_parts(path, lambda x: splitmap(x, char=": ", mapper=lambda x: x), lambda x: splitmap(x, char=": ", mapper=lambda x: x))

def run(registers, instructions, search, second=True):
    pc = 0
    res = []
    amt = len(search)
    while pc < len(instructions):
        op = instructions[pc]
        literal = instructions[pc+1]
        combo = 0
        if 3 >= literal >= 0:
            combo = literal
        elif literal == 4:
            combo = registers[0]
        elif literal == 5:
            combo = registers[1]
        elif literal == 6:
            combo = registers[2]
        if op == 0:
            #print("adv", int(registers[0] / pow(2, combo)))
            registers[0] = int(registers[0] / pow(2, combo))
        elif op == 1:
            #print("bxl", registers[1] ^ literal)
            registers[1] = registers[1] ^ literal
        elif op == 2:
            #print("bst")
            registers[1] = combo % 8
        elif op == 3:
            #print("jnz", literal)
            if registers[0] != 0:
                pc = literal
                continue
        elif op == 4:
            #print("bxc")
            registers[1] = registers[1] ^ registers[2]
        elif op == 5:
            #print("out", combo % 8)
            res.append(str(combo % 8))
            if second and (len(res) >= amt or res[0] != search[0] or (res[0] == search[0] and res[1] != search[1])):
                return ",".join(res)
        elif op == 6:
            #print("bdv")
            registers[1] = int(registers[0] / pow(2, combo))
        elif op == 7:
            #print("cdv")
            registers[2] = int(registers[0] / pow(2, combo))
        else:
            print(op, combo, pc)
        pc += 2
    return res

registers = []
for l, r in upper:
    registers.append(int(r))
first = lower[0][1]
instructions = list(map(int, first.split(",")))
search = instructions.copy()
print(search)

second = run(registers, instructions, [], second=False)
print(",".join(second))

part2 = 0
for i, s in enumerate(reversed(instructions)):
    for j in range(0,8):
        nr = part2 * 8 + j
        registers = [nr,0,0]
        result = run(registers, instructions, [], second=False)
        if int(result[0]) == s:
            part2 = nr
            break
print(part2)

#alternative from discord
program = instructions
valid_numbers = [0]
for i in reversed(program):
    new_valids = []
    for num in valid_numbers:
        for digit in range(8):
            a = num * 8 + digit
            val = ((a % 8) ^ 5 ^ (a // (2 ** ((a % 8) ^ 2)))) % 8
            if val == i:
                new_valids.append(a)
    valid_numbers = new_valids
print("valid", list(sorted(valid_numbers)))
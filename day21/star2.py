from helpers import *
import numpy as np
from tqdm import tqdm
from itertools import permutations
from functools import lru_cache
path, testpath = get_input(21)

def move_to(start, end):
    diff = end - start
    moves1 = ""
    moves2 = ""
    if diff[1] < 0:
        moves1 += "<" * -diff[1]
    if diff[1] > 0:
        moves1 += ">" *  diff[1]
    if diff[0] < 0:
        moves1 += "^" * -diff[0]
    if diff[0] > 0:
        moves1 += "v" *  diff[0]
    moves1 += "A"
    if diff[1] != 0 and diff[1] != 0:
        if diff[0] < 0:
            moves2 += "^" * -diff[0]
        if diff[0] > 0:
            moves2 += "v" *  diff[0]
        if diff[1] < 0:
            moves2 += "<" * -diff[1]
        if diff[1] > 0:
            moves2 += ">" *  diff[1]
        return [moves1, moves2 + "A"]
    return [moves1]

def check_path(start, seq, keypad):
    gap = keypad["g"]
    pos = V2(start[0], start[1])
    for c in seq:
        match c:
            case "<": pos += ( 0,-1)
            case ">": pos += ( 0, 1)
            case "^": pos += (-1, 0)
            case "v": pos += ( 1, 0)
        if pos == gap:
            return False
    return True
    
mappings = {
    ("A", "A"): [""],
    ("^", "A"): [">"],
    ("v", "A"): [">^", "^>"],
    ("<", "A"): [">>^", ">^>"],
    (">", "A"): ["^"],
    ("A", "^"): ["<"],
    ("^", "^"): [""],
    ("v", "^"): ["^"],
    ("<", "^"): [">^"],
    (">", "^"): ["<^", "^<"],
    ("A", "v"): ["<v", "v<"],
    ("^", "v"): ["v"],
    ("v", "v"): [""],
    ("<", "v"): [">"],
    (">", "v"): ["<"],
    ("A", "<"): ["v<<", "<v<"],
    ("^", "<"): ["v<"],
    ("v", "<"): ["<"],
    ("<", "<"): [""],
    (">", "<"): ["<<"],
    ("A", ">"): ["v"],
    ("^", ">"): ["v>", ">v"],
    ("v", ">"): [">"],
    ("<", ">"): [">>"],
    (">", ">"): [""]
}

@lru_cache(maxsize=None)
def calc_length(inp, origin, depth):
    if depth == 0:
        return 1
    
    mapping = mappings[(origin, inp)]
    c2 = "A"
    amounts = []
    for m in mapping:
        options = []
        for c in m + "A":
            options.append(calc_length(c, c2, depth-1))
            c2 = c
        amounts.append(sum(options))
    return min(amounts)

def press_button(tstart, button, keypad):
    tend = keypad[button]
    seq = move_to(tstart, tend)
    seq = [s for s in seq if check_path(tstart, s, keypad)]
    return seq, tend

def build_combinations(line):
    num_pos = V2(3,2)
    combs, num_pos = press_button(num_pos, line[0], keypadNums)
    combs = [(comb, num_pos) for comb in combs]
    for c in line[1:]:
        new_combs = []
        for comb, old_num_pos in combs:
            seq, end_pos = press_button(old_num_pos, c, keypadNums)
            
            for s in seq:
                new_combs.append((comb + s, end_pos))
        combs = new_combs
    return combs
        

keypadNums = {"7": V2(0,0), "8": V2(0,1), "9": V2(0,2), "4": V2(1,0), "5": V2(1,1), "6": V2(1,2), "1": V2(2,0), "2": V2(2,1), "3": V2(2,2), "g": V2(3,0), "0": V2(3,1), "A": V2(3,2)}
keyPadRobot = {"g": V2(0,0), "^": V2(0,1), "A": V2(0,2), "<": V2(1,0), "v": V2(1,1), ">": V2(1,2)}
res = 0

for line in list(open(path))[:]:
    line = line.strip()
    num_pos = V2(3,2)
    #print(line)
    combs = set(build_combinations(line))
    sums = []
    for comb, _ in combs:
        #print("comb", comb)
        last = "A"
        l = 0
        for s in comb:
            x = calc_length(s, last, 25)
            l += x
            last = s
        sums.append(l)
    res += int("".join([s for s in line if s.isdigit()])) * min(sums)

print(res)
print(calc_length.cache_info())
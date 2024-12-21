from helpers import *
import numpy as np
from tqdm import tqdm
from itertools import permutations
path, testpath = get_input(21)

def move_to(start, end, keypad):
    gap = keypad["g"]
    diff = end - start
    moves = ""
    if start[1] == 0 and end[0] == gap[0]:
        if diff[1] < 0:
            moves += "<" * -diff[1]
        if diff[1] > 0:
            moves += ">" *  diff[1]
        if diff[0] < 0:
            moves += "^" * -diff[0]
        if diff[0] > 0:
            moves += "v" *  diff[0]
    else:
        if diff[0] < 0:
            moves += "^" * -diff[0]
        if diff[0] > 0:
            moves += "v" *  diff[0]
        if diff[1] < 0:
            moves += "<" * -diff[1]
        if diff[1] > 0:
            moves += ">" *  diff[1]
    moves += "A"
    #print(diff)
    return moves

def check_path(start, end, seq, keypad, human):
    gap = keypad["g"]
    if not human and start[1] == 0 and end[0] == gap[0]:
        pos = start
        for c in seq:
            match c:
                case "<": pos += ( 0,-1)
                case ">": pos += ( 0, 1)
                case "^": pos += (-1, 0)
                case "v": pos += ( 1, 0)
            if pos == gap:
                return False
        return True
    else:
        return True

def press_button(tstart, button, keypad):
    tend = keypad[button]
    seq = move_to(tstart, tend, keypad)
    return seq, tend

def check_all(seq, start_pos, end_pos, keypad, human, depth):
    if depth == 3:
            return seq
    for i, perm in permutations(seq[:-1]):
        if not check_path(start_pos, end_pos, perm, keypad, human):
            continue
        for c in perm:
            nextSeq, nextStart = press_button(, c, keypad)
            check_all(nextSeq, nextStart, , keypad)

keypadNums = {"7": V2(0,0), "8": V2(0,1), "9": V2(0,2), "4": V2(1,0), "5": V2(1,1), "6": V2(1,2), "1": V2(2,0), "2": V2(2,1), "3": V2(2,2), "g": V2(3,0), "0": V2(3,1), "A": V2(3,2)}
keyPadRobot = {"g": V2(0,0), "^": V2(0,1), "A": V2(0,2), "<": V2(1,0), "v": V2(1,1), ">": V2(1,2)}
res = 0
for line in list(open(testpath))[2:3]:
    line = line.strip()
    num_pos = V2(3,2)
    r1_pos = we_pos = V2(0, 2)
    seq = []
    seq1 = []
    seq2 = []
    for c in line:
        num_pos_old = num_pos
        numSeq, num_pos = press_button(num_pos, c, keypadNums)
        print(c)
        for perm1 in permutations(numSeq[:-1]):
            if not check_path(num_pos_old, num_pos, perm1, keypadNums, False):
                continue
            print("p1", perm1 + ("A",))

            for c1 in perm1:
                r1_pos_old = V2(0, 2)#r1_pos
                r1Seq, r1_pos = press_button(r1_pos, c1, keyPadRobot)
                for perm2 in permutations(r1Seq[:-1]):
                    if not check_path(r1_pos_old, r1_pos, perm2, keyPadRobot, False):
                        continue
                    print("p2", perm2 + ("A",))
        break

        seq1 += numSeq
        for c1 in numSeq:
            r1_pos_old = r1_pos
            r1Seq, r1_pos = press_button(r1_pos, c1, keyPadRobot)
            
            seq2 += r1Seq
            for c2 in r1Seq:
                weSeq, we_pos = press_button(we_pos, c2, keyPadRobot)
                seq += weSeq
    print(seq)
    print(seq2)
    print(seq1)
    print(line)
    print(len(seq), int("".join([s for s in line if s.isdigit()])))
    res += int("".join([s for s in line if s.isdigit()])) * len(seq)
    #print(line)
    print()
#<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#<A>Av<<AA>^AA>AvAA^A<vAAA>^A
#v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A^>AA<A>Av<A<A>>^AAA<Av>A^A
#<A>A<AAv<AA>>^AvAA^Av<AAA^>A

print(res)
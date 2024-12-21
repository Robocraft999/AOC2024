from helpers import *
import numpy as np
from tqdm import tqdm
from itertools import permutations
path, testpath = get_input(21)

def move_to(start, end, other=False):
    diff = end - start
    moves = ""
    if other:
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
    return moves

def check_path(start, end, seq, keypad, human):
    gap = keypad["g"]
    if not human and start[1] == 0 and end[0] == gap[0]:
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
    else:
        return True

def press_button(tstart, button, keypad):
    tend = keypad[button]
    seq1 = move_to(tstart, tend)
    seq2 = move_to(tstart, tend, True)
    if seq2 == seq1:
        seq2 = ""
    print(button, tend)
    return seq1, seq2, tend

def check_all(pos, button, keypad, human, depth):
    old_pos = pos
    seq1, seq2, end_pos = press_button(pos, button, keypad)
    print(seq1, seq2, button, pos, end_pos)
    if depth == 1:
        return [seq1], [seq2], end_pos
    if "0" in keypad: keypad = keyPadRobot
    seq11 = seq12 = seq21 = seq22 = []
    if check_path(old_pos, pos, seq1, keypad, human):
        pos2 = V2(0, 2)
        
        for s in seq1:
            s1, s2, pos2 = check_all(pos2, s, keypad, human, depth + 1)
            seq11.append(s1)
            seq12.append(s2)
    if check_path(old_pos, pos, seq2, keypad, human):
        pos2 = V2(0, 2)
        for s in seq2:
            s1, s2, pos2 = check_all(pos2, s, keypad, human, depth + 1)
            seq21.append(s1)
            seq22.append(s2)
    return [seq11, seq12], [seq21, seq22], end_pos

keypadNums = {"7": V2(0,0), "8": V2(0,1), "9": V2(0,2), "4": V2(1,0), "5": V2(1,1), "6": V2(1,2), "1": V2(2,0), "2": V2(2,1), "3": V2(2,2), "g": V2(3,0), "0": V2(3,1), "A": V2(3,2)}
keyPadRobot = {"g": V2(0,0), "^": V2(0,1), "A": V2(0,2), "<": V2(1,0), "v": V2(1,1), ">": V2(1,2)}
res = 0
for line in list(open(testpath))[0:1]:
    line = line.strip()
    num_pos = V2(3,2)
    r1_pos1 = r1_pos2 = V2(0, 2)
    we_pos11 = we_pos12 = we_pos21 = we_pos22 = V2(0, 2)
    seq = [""] * 8
    seq1 = [""] * 2
    seq2 = [""] * 4
    for c in line:
        num_pos_old = num_pos
        numSeq1, numSeq2, num_pos = press_button(num_pos, c, keypadNums)
        if check_path(num_pos_old, num_pos, numSeq1, keypadNums, False):
            for c1 in numSeq1:
                r1_pos1_old = r1_pos1
                r1Seq1, r1Seq2, r1_pos1 = press_button(r1_pos1, c1, keyPadRobot)
                if check_path(r1_pos1_old, r1_pos1, numSeq1, keyPadRobot, False):
                    for c2 in r1Seq1:
                        we_pos11_old = we_pos11
                        weSeq1, weSeq2, we_pos11 = press_button(we_pos11, c2, keyPadRobot)
                        seq[0] += weSeq1
                        seq[1] += weSeq2
                if check_path(r1_pos1_old, r1_pos1, numSeq1, keyPadRobot, False):
                    for c2 in r1Seq2:
                        we_pos12_old = we_pos12
                        weSeq1, weSeq2, we_pos12 = press_button(we_pos12, c2, keyPadRobot)
                        seq[2] += weSeq1
                        seq[3] += weSeq2
                seq2[0] += r1Seq1
                seq2[1] += r1Seq2
            print("r1pos1", r1_pos1, numSeq1)
        if check_path(num_pos_old, num_pos, numSeq2, keypadNums, False):
            for c1 in numSeq1:
                r1_pos2_old = r1_pos2
                r2Seq1, r2Seq2, r1_pos2 = press_button(r1_pos2, c1, keyPadRobot)
                if check_path(r1_pos2_old, r1_pos2, numSeq1, keyPadRobot, False):
                    for c2 in r2Seq1:
                        we_pos21_old = we_pos21
                        weSeq1, weSeq2, we_pos21 = press_button(we_pos21, c2, keyPadRobot)
                        seq[4] += weSeq1
                        seq[5] += weSeq2
                if check_path(r1_pos2_old, r1_pos2, numSeq1, keyPadRobot, False):
                    for c2 in r2Seq2:
                        we_pos22_old = we_pos22
                        weSeq1, weSeq2, we_pos22 = press_button(we_pos22, c2, keyPadRobot)
                        seq[6] += weSeq1
                        seq[7] += weSeq2
                seq2[2] += r2Seq1
                seq2[3] += r2Seq2
        seq1[0] += numSeq1
        seq1[1] += numSeq2
    seq.sort(key=lambda x: len(x))
    for s in seq:
        print(s)
    print()
    for s in seq2:
        print(s)
    print()
    for s in seq1:
        print(s)
    print()
    print(line)
    
    print(len(seq[0]), int("".join([s for s in line if s.isdigit()])))
    res += int("".join([s for s in line if s.isdigit()])) * len(seq[0])
    #print(line)
    print()

for line in list(open(testpath))[0:1]:
    line = line.strip()
    num_pos = V2(3,2)
    for c in line:
        seq1, seq2, num_pos = check_all(num_pos, c, keypadNums, False, 0)
        print(c, seq1)
        print(c, seq2)
        print(c, num_pos)

#v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#v<<A^>>A<A>A<AAv>A^Av<AAA^>A

#<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#<A>Av<<AA>^AA>AvAA^A<vAAA>^A
#v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A^>AA<A>Av<A<A>>^AAA<Av>A^A
#<A>A<AAv<AA>>^AvAA^Av<AAA^>A

#g1  <
#g2  <

#r11 >
#r12 ^
#r21 >
#r22 ^

#w111 v
#w112 v
#w121 <
#w122 <
#w211 v
#w212 v
#w221 <
#w222 <

print(res)
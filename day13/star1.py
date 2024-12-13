from helpers import *
import re
import numpy as np
import functools
path, testpath = get_input(13)

def parse_as_text(path):
    text = ""
    for line in open(path):
        text += line
    return text

res = 0
text = parse_as_text(path)
for m in re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", text):
    target = V2(int(m[4]), int(m[5]))
    a = V2(int(m[0]), int(m[1]))
    b = V2(int(m[2]), int(m[3]))
    la = np.array([[a[0], b[0]], [a[1], b[1]]])
    lb = np.array([int(m[4]), int(m[5])])
    x = np.linalg.solve(la,lb)
    t = np.rint(x)

    margin = 1e-8
    #print(x, abs(t[0] - x[0]) < margin, abs(t[1] - x[1]) < margin)
    if 100 < x[0] or 100 < x[1]:
        continue
    
    if abs(t[0] - x[0]) < margin and abs(t[1] - x[1]) < margin:
        res += 3*t[0] + 1*t[1]
        #print((3, 1) * t)

print(sum([sum([np.sum((3, 1) * np.rint(x))for x,padd in [(np.linalg.solve(np.array([[int(m[0]), int(m[2])], [int(m[1]), int(m[3])]]), np.array([int(m[4]), int(m[5])])), 1e-8)]if abs(np.rint(x)[0] - x[0]) < padd and abs(np.rint(x)[1] - x[1]) < padd]) for m in re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", functools.reduce(lambda x, y: x+y,[line for line in open(get_input(13)[0])]))]))

print(res)
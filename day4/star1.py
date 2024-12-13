from helpers import *
import re
path, testpath = get_input(4)

res = 0
lines = []
for line in open(path):
    lines.append(line.strip())

for line in lines:
    res += len(re.findall(r"(?=(XMAS))", line))
    res += len(re.findall(r"(?=(XMAS))", line[::-1]))

cols = []
for x in range(len(lines[0])):
    col = ""
    for y in range(len(lines)):
        col += lines[y][x]
    cols.append(col)
for col in cols:
    res += len(re.findall(r"(?=(XMAS))", col))
    res += len(re.findall(r"(?=(XMAS))", col[::-1]))

for y in range(len(lines)-4):
    dial = ""
    diar = ""
    for x in range(len(line[0])-4):
        dial += line[y][x]

for j in range(len(lines)-4, -2, -1):
    diag = ""
    for i in range(len(lines)):
        j += 1
        if j > len(lines)-1:
             break
        diag += lines[i][j]
    #print(diag)
    res += len(re.findall(r"(?=(XMAS))", diag))
    res += len(re.findall(r"(?=(XMAS))", diag[::-1]))
for j in range(1, len(lines), 1):
    diag = ""
    for i in range(len(lines)-1, 0, -1):
        j -= 1
        if j < 0:
             break
        diag += lines[i][j]
    #print(diag)
    res += len(re.findall(r"(?=(XMAS))", diag))
    res += len(re.findall(r"(?=(XMAS))", diag[::-1]))

#print()

for j in range(len(lines)-4, -2, -1):
    diag = ""
    for i in range(len(lines)):
        j += 1
        if j > len(lines)-1:
             break
        diag += lines[::-1][i][j]
    #print(diag)
    res += len(re.findall(r"(?=(XMAS))", diag))
    res += len(re.findall(r"(?=(XMAS))", diag[::-1]))
for j in range(1, len(lines), 1):
    diag = ""
    for i in range(len(lines)-1, 0, -1):
        j -= 1
        if j < 0:
             break
        diag += lines[::-1][i][j]
    #print(diag)
    res += len(re.findall(r"(?=(XMAS))", diag))
    res += len(re.findall(r"(?=(XMAS))", diag[::-1]))

print(res)
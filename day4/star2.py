from helpers import *
import re
path, testpath = get_input(4)

res = 0
lines = []
for line in open(path):
    lines.append(line.strip())

for y in range(len(lines)-2):
    for x in range(len(lines[0])-2):
        dia1 = lines[y][x] + lines[y+1][x+1] + lines[y+2][x+2]
        dia2 = lines[y][x+2] + lines[y+1][x+1] + lines[y+2][x]
        if (re.match("MAS", dia1) or re.match("SAM", dia1)) and (re.match("MAS", dia2) or re.match("SAM", dia2)):
            res += 1

print(res)
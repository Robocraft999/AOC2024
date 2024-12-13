from helpers import *
from itertools import permutations
path, testpath = get_input(8)

res = 0
grid = parse_as_nparray(path)
antennas = find_all_in_grid(grid, ["."])
print(antennas)
poses = set()
for antenna in antennas.keys():
    g = grid.copy()
    for (a, b) in permutations(antennas[antenna], 2):
        diff = a - b
        pos = a + diff
        poses.add(a)
        poses.add(b)
        while pos_in_nparray(g, pos):
            if not pos in poses:
                #print(g[pos[0]][pos[1]])
                poses.add(pos)
            pos = pos + diff
            
        pos = b - diff
        while pos_in_nparray(g, pos):
            if not pos in poses:
                #print(g[pos[0]][pos[1]])
                poses.add(pos)
            pos = pos - diff
    #print(g)
res = len(poses)
print(res)
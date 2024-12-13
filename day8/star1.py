from helpers import *
from itertools import permutations
path, testpath = get_input(8)

res = 0
grid = parse_as_nparray(path)
antennas = find_all_in_grid(grid, ["."])
print(antennas)
poses = set()
for antenna in antennas.keys():
    for (a, b) in permutations(antennas[antenna], 2):
        diff = a - b
        pos = a + diff
        if pos_in_nparray(grid, pos) and not pos in poses:
            poses.add(pos)
            
        pos = b - diff
        if pos_in_nparray(grid, pos) and not pos in poses:
            poses.add(pos)
res = len(poses)
print(res)
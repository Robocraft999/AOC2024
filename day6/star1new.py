from helpers import *
import numpy as np
path, testpath = get_input(6)

grid = parse_as_nparray(path)
pos = V2.of(find_in_grid(grid, '^'))

dir = V2(-1, 0)
poses = {pos}
while pos_in_nparray(grid, pos, 1):
    npos = pos + dir
    if check_pos_in_grid(grid, npos, "#"):
        dir = dir.rotated90()
    else:
        pos = npos
        poses.add(pos)

print(grid, pos)
print(len(poses))
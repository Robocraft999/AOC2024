from helpers import *
import numpy as np
path, testpath = get_input(6)

def rotate_dir(dir):
    if dir == (-1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (-1, 0)

res = 1
grid = []
pos = (-1,-1)
for i, line in enumerate(open(path)):
    grid.append([c for c in line.strip()])
    if '^' in line:
        pos = (i, line.index('^'))

grid = np.array(grid)

dir = (-1, 0)
poses = {pos}
while pos[0] > 0 and pos[0] < grid.shape[0]-1 and pos[1] > 0 and pos[1] < grid.shape[1]-1:
    ny, nx = (pos[0] + dir[0], pos[1] + dir[1])
    if grid[ny][nx] == '#':
        dir = rotate_dir(dir)
    else:
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        poses.add(pos)

print(grid, pos)

print(len(poses))
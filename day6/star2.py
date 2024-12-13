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
    
def try_for_loop(grid, pos):
    dir = (-1, 0)
    poses = {pos}
    dirs = {pos: dir}

    while pos[0] > 0 and pos[0] < grid.shape[0]-1 and pos[1] > 0 and pos[1] < grid.shape[1]-1:
        ny, nx = (pos[0] + dir[0], pos[1] + dir[1])
        if grid[ny][nx] == '#':
            dir = rotate_dir(dir)
            if pos in poses and dirs[pos] == dir:
                return True
        else:
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            if pos in poses and dirs[pos] == dir:
                return True

            poses.add(pos)
            dirs[pos] = dir
    return False

res = 0
grid = []
pos = (-1,-1)
for i, line in enumerate(open(path)):
    grid.append([c for c in line.strip()])
    if '^' in line:
        pos = (i, line.index('^'))

grid = np.array(grid)

print("start", pos)

for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        g = grid.copy()
        if not (y == pos[0] and x == pos[1]):
            g[y][x] = '#'
            if try_for_loop(g, pos):
                res += 1


print(grid, pos)

print(res)
from helpers import *
import numpy as np
from tqdm import tqdm
from queue import Queue
path, testpath = get_input(18)

def print_grid(grid):
    for y, line in enumerate(grid):
        for x, elem in enumerate(line):
            print(int(elem), end="")
        print()

def pathfind(grid, start, end):
    visited = set()
    todo = Queue()
    todo.put((start, 0))
    while not todo.empty():
        (current, f) = todo.get()
        if current == end:
            return f
        
        if current in visited:
            continue
        dirs = [V2(0,1), V2(1,0), V2(0,-1), V2(-1,0)]
        for dir in dirs:
            new_pos = current + dir
            if pos_in_nparray(grid, new_pos) and grid[new_pos[0]][new_pos[1]] < 1:
                if not new_pos in visited:
                    todo.put((new_pos, f+1))
        visited.add(current)
    return None

res = 0
size = 71
grid = np.zeros([size,size])
start = V2(0,0)
end = V2(size-1,size-1)
lines = parse_lines_split(path, int, ",")
for x,y in lines:
    grid[y][x] = 1
print_grid(grid)

print(pathfind(grid, start, end))

watcher = tqdm(lines[::-1])
for x,y in watcher:
    grid[y][x] = 0
    distance = pathfind(grid, start, end)
    if distance:
        watcher.close()
        print("res:", x,y)
        break
print(res)
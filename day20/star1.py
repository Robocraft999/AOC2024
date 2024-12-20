from helpers import *
import numpy as np
from tqdm import tqdm
from queue import Queue
import re
path, testpath = get_input(20)

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
            if check_pos_in_grid(grid, new_pos, ".") or check_pos_in_grid(grid, new_pos, "E"):
                if not new_pos in visited:
                    todo.put((new_pos, f+1))
        visited.add(current)
    return None

res = 0
grid = parse_as_nparray(testpath)
positions = find_all_in_grid(grid, [".", "#"])
start = positions["S"][0]
end = positions["E"][0]
print(start, end)


normal_time = pathfind(grid, start, end)
print("nt", normal_time)

wall_poses = []
pattern = re.compile(r"\.#(?=\.)|\.#E|E#\.|S#\.|\.#S")
for y, line in enumerate(grid):
    for match in pattern.finditer("".join(line)):
        wall_poses.append((V2(y, match.start()), V2(y, match.start()+2)))
for x, col in enumerate(np.transpose(grid)):
    for match in pattern.finditer("".join(col)):
        wall_poses.append((V2(match.start(), x), V2(match.start()+2, x)))

times = []
for spos, epos in tqdm(wall_poses):
    time = pathfind(grid, spos, epos) - 2
    if normal_time - time >= 100:
        res += 1
    times.append(time)
    #print(normal_time - new_time)
times.sort()
print(times)

print(res)
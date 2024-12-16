from helpers import *
import sys
path, testpath = get_input(16)
sys.setrecursionlimit(1000000)

def print_grid(grid):
    for y, line in enumerate(grid):
        for x, elem in enumerate(line):
            print(elem, end="")
        print()

def visit(grid, pos, dir, score, visited):
    if pos in visited and score >= visited[pos]:
        return visited[pos]
    visited[pos] = score
    
    paths = []
    dirs = {dir: 0, dir.rotated90(): 1, dir.rotated90().rotated90().rotated90(): 1}
    for dirr, turns in dirs.items():
        if not check_pos_in_grid(grid, pos + dirr, "#"):
            r = visit(grid, pos + dirr, dirr, score + turns*1000 + 1, visited)
            if r > 0:
                paths.append(r)

    if len(paths) == 0:
        return -1
    return min(paths)

def visit2(pos, visited, visited2, dir):
    mins = {}
    if pos in visited2:
        return
    if pos == start:
        visited2.add(pos)
        return
    visited2.add(pos)
    dirs = {dir: 0, dir.rotated90(): 1, dir.rotated90().rotated90().rotated90(): 1}
    for dirr, i in dirs.items():
        if not check_pos_in_grid(grid, pos + dirr, "#"):
            score = visited[pos+dirr] + i * 1000
            
            if len(mins) == 0:
                mins[(pos+dirr, dirr)] = score
            else:
                old_score = list(mins.values())[0]
                if old_score > score:
                    mins.clear()
                    mins[(pos+dirr, dirr)] = score
                elif old_score == score:
                    mins[(pos+dirr, dirr)] = score
    for pos, dir in mins:
        visit2(pos, visited, visited2, dir)
res = 0
grid = parse_as_nparray(path)
positions = find_all_in_grid(grid, ["#", "."])
start = positions["S"][0]
end = positions["E"][0]
visited = {}
res = visit(grid, start, V2(0, 1), 0, visited)

print(start, end)
print(visited[end])
print("t")
visited2 = set()
visit2(end, visited, visited2, V2(1,0))
print(len(visited2))
for pos in visited2:
    grid[pos[0]][pos[1]] = "O"

#print_grid(grid)
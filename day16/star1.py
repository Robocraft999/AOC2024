from helpers import *
import sys
path, testpath = get_input(16)
sys.setrecursionlimit(1000000)

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

res = 0
grid = parse_as_nparray(testpath)
positions = find_all_in_grid(grid, ["#", "."])
start = positions["S"][0]
end = positions["E"][0]
visited = {}
res = visit(grid, start, V2(0, 1), 0, visited)

print(start, end)
print(visited[end])
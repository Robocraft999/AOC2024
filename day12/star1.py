from helpers import *
from itertools import combinations, permutations
path, testpath = get_input(12)


def visit(pos, visited: set):
    visited.add(pos)
    dir = V2(0, 1)
    area = 1
    peri = 0
    own_peri = 4
    for _ in range(4):
        new_pos = pos + dir
        if pos_in_nparray(grid, new_pos) and check_pos_in_grid(grid, new_pos, name):
            own_peri -= 1
            if not new_pos in visited:
                na, np = visit(new_pos, visited)
                area += na
                peri += np
        dir = dir.rotated90()
    return area, peri + own_peri

res = 0
grid = parse_as_nparray(path)
positions = find_all_in_grid(grid)

for name in positions:
    visited = set()
    for pos in positions[name]:
        if pos in visited:
            continue
        area, peri = visit(pos, visited)
        res += area * peri

print(res)
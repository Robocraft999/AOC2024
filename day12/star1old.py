from helpers import *
from itertools import combinations, permutations
path, testpath = get_input(12)

def get_area_and_peri(grid, name, pos, neighbor_map):
    neighbors = []
    dir = V2(0, 1)
    for i in range(4):
        new_pos = pos + dir
        if pos_in_nparray(grid, new_pos) and check_pos_in_grid(grid, new_pos, name):
            neighbors.append(new_pos)
        dir = dir.rotated90()
    peri = 4
    for n in neighbors:
        peri -= 1
    return peri, list(filter(lambda x: not x in neighbor_map, neighbors))

def reduce_pos(pos, neighbor_map):
    group = {pos}
    neighbors = []
    for neigbor in neighbor_map[pos]:
        neighbors = reduce_pos(neigbor, neighbor_map)
    group = group.union(neighbors)
    return group

res = 0
grid = parse_as_nparray(testpath)
positions = find_all_in_grid(grid)
for name in positions:
    groups = []
    neighbor_map = {}
    value_map = {}
    for pos in positions[name]:
        peri, neighbors = get_area_and_peri(grid, name, pos, neighbor_map)
        neighbor_map[pos] = neighbors
        value_map[pos] = peri
    visited = set()
    for pos in neighbor_map:
        group = reduce_pos(pos, neighbor_map)
        for pos in group:
            visited.add(pos)
        if all([group.isdisjoint(g) for g in groups]):
            groups.append(group)
        else:
            for i, g in enumerate(groups):
                if not group.isdisjoint(g):
                    groups[i] = g.union(group)
                    break
    for g in groups:
        res += len(g) * sum([value_map[p] for p in g])
        
    #print(groups)
    #print(neighbor_map)
    #print()
        

print(res)
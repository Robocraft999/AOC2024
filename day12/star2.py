from helpers import *
path, testpath = get_input(12)


def visit(pos, visited: set, name, grid):
    visited.add(pos)
    dir = V2(0, 1)
    area = 1
    corners = 0
    group = {pos}
    neighbors = []
    for _ in range(4):
        new_pos = pos + dir
        if pos_in_nparray(grid, new_pos) and check_pos_in_grid(grid, new_pos, name):
            neighbors.append(new_pos)
        dir = dir.rotated90()
    nc = len(neighbors)
    if len(neighbors) == 0:
        corners += 4
    elif len(neighbors) == 1:
        corners += 2
    else:
        l,r,n,d1,d2 = V2(0,-1), V2(0,1), V2(1,0), V2(1,1), V2(1,-1)
        for _ in range(4):
            lpos,rpos,npos,d1pos,d2pos = pos+l, pos+r, pos+n, pos+d1, pos+d2

            #XXX
            #XAA
            #XAX
            if check_pos_in_nparray(grid, npos, name) and check_pos_in_nparray(grid, rpos, name):
                if nc == 2:
                    corners += 1
                #XXX
                #XAA
                #XAB
                if not check_pos_in_nparray(grid, d1pos, name):
                    if nc == 4 or nc == 2:
                        corners += 1
                    #BBB
                    #AAA
                    #XAB
                    elif check_pos_in_nparray(grid, lpos, name):
                        corners += 1
                #XXX
                #XAA
                #BAX
                if not check_pos_in_nparray(grid, d2pos, name):
                    #BBB
                    #AAA
                    #BAX
                    if nc == 3 and check_pos_in_nparray(grid, lpos, name):
                        corners += 1

            l,r,n,d1,d2 = l.rotated90(), r.rotated90(), n.rotated90(), d1.rotated90(), d2.rotated90()
    for n in neighbors:
        if not n in visited:
            na, nc, ng = visit(n, visited, name, grid)
            area += na
            corners += nc
            group = group.union(ng)
    return area, corners, group

res = 0
grid = parse_as_nparray(path)
positions = find_all_in_grid(grid)

for name in positions:
    visited = set()
    for pos in positions[name]:
        if pos in visited:
            continue
        area, corners, group = visit(pos, visited, name, grid)
        #print(name, group, corners)
        res += area * corners

print(res)
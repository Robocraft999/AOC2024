from helpers import *
import numpy as np
path, testpath = get_input(18)

def print_grid(grid):
    for y, line in enumerate(grid):
        for x, elem in enumerate(line):
            print(int(elem), end="")
        print()

def backtrack(initial_node, desired_node, distances):
    path = [desired_node]

    while True:
        potential_distances = []
        potential_nodes = []

        dir = V2(0,1)

        for _ in range(4):
            node = path[-1] + dir
            if pos_in_nparray(grid, node):
                potential_nodes.append(node)
                potential_distances.append(distances[node[0],node[1]])
            
            dir = dir.rotated90()

        least_distance_index = np.argmin(potential_distances)
        path.append(potential_nodes[least_distance_index])

        if path[-1] == initial_node:
            break

    return list(reversed(path))

def astar(grid, start, end):
    obstacles = grid.copy() * 1000
    obstacles += np.ones(obstacles.shape)
    obstacles[start[0]][start[1]] = 0
    obstacles[end[0]][end[1]] = 0

    size = grid.shape[0]
    visited = np.zeros([size, size], bool)
    distances = np.ones([size,size]) * np.inf
    distances[start[0],start[1]] = 0

    current_node = start
    while True:
        dir = V2(0,1)
        for _ in range(4):
            new_pos = current_node + dir
            if pos_in_nparray(grid, new_pos):
                if not visited[new_pos[0]][new_pos[1]]:
                    distance = distances[current_node[0]][current_node[1]] + obstacles[new_pos[0]][new_pos[1]]
                    if distance < distances[new_pos[0]][new_pos[1]]:
                        distances[new_pos[0]][new_pos[1]] = distance
            dir = dir.rotated90()
        visited[current_node[0]][current_node[1]] = True
        t=distances.copy()
        t[np.where(visited)]=np.inf
        node_index = np.argmin(t)

        node_row = node_index//size
        node_col = node_index%size

        current_node = V2(int(node_row), int(node_col))
        if current_node == end:
            break
    #print(distances)
    return backtrack(start,end,distances)

res = 0
grid = np.zeros([71,71])
for x,y in parse_lines_split(path, int, ",")[:1024]:
    grid[y][x] = 1
print_grid(grid)

start = V2(0,0)
path = astar(grid, start, V2(70,70))
print(len(path) -1, path)

print(res)
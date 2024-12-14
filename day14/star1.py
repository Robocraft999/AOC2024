from helpers import *
path, testpath = get_input(14)

res = 1
robots = []
velocities = []
for left, right in parse_lines_split(path, mapper=lambda x: splitmap(x, char=",", mapper=lambda y: splitmap(y, char="=", mapper=lambda x: x))):
    pos = V2(int(left[1][0]), int(left[0][1]))
    velocity = V2(int(right[1][0]), int(right[0][1]))
    velocities.append(velocity)
    robots.append(pos)
grid = np.zeros([103, 101])
#grid = np.zeros([7, 11])
quadrants = [0, 0, 0, 0]
for i, robot in enumerate(robots):
    new_pos = robot
    new_pos += velocities[i]*100
    new_pos[0] %= grid.shape[0]
    new_pos[1] %= grid.shape[1]
    q = 0
    grid[new_pos[0]][new_pos[1]] += 1
    
    if new_pos[1] < grid.shape[1] // 2:
        q += 2
    if new_pos[0] > grid.shape[0] // 2:
        q += 1
    if new_pos[0] == grid.shape[0] // 2 or new_pos[1] == grid.shape[1] // 2:
        pass
    else:
        quadrants[q] += 1
for q in quadrants:
    res *= q
for y, line in enumerate(grid):
    for x, elem in enumerate(line):
        if y == grid.shape[0] // 2 or x == grid.shape[1] // 2:
            print(" ", end="")
        else:
            print(int(elem), "", end="")
    print()
print(quadrants, res)
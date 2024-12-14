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
#grid = np.zeros([7, 11])
for s in range(1, 11000):
    grid = Grid(np.zeros([103, 101]))
    flag = True
    for i, robot in enumerate(robots):
        new_pos = robot
        new_pos += velocities[i]
        new_pos[0] %= grid.inner.shape[0]
        new_pos[1] %= grid.inner.shape[1]
        q = 0
        grid[new_pos] += 1
        if grid[new_pos] > 1:
            flag = False
    if flag == True:
        for y, line in enumerate(grid):
            for x, elem in enumerate(line):
                if y == grid.inner.shape[0] // 2 or x == grid.inner.shape[1] // 2:
                    print(" ", end="")
                else:
                    print(int(elem), "", end="")
            print()
        print(s)
        break
print(res)
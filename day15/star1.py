from helpers import *
import numpy as np
path, testpath = get_input(15)

res = 0
upper, lower = parse_as_two_parts(path, lambda x : x, lambda x: x)
grid = []
for line in upper[1:len(upper)-1]:
    grid.append([x for x in line[1:len(line)-1]])
grid = np.array(grid)
positions = find_all_in_grid(grid, ["."])
print(grid)
instructions = ""
for line in lower:
    instructions += line
pos = positions["@"][0]
boxes: list = positions["O"]
for instruction in instructions[:]:
    if instruction == "<":
        dir = (0, -1)
    elif instruction == "^":
        dir = (-1, 0)
    elif instruction == ">":
        dir = (0, 1)
    elif instruction == "v":
        dir = (1, 0)
    next_pos = pos + dir

    if check_pos_in_nparray(grid, next_pos, "."):
        print(instruction, "moving to", next_pos)
        grid[next_pos[0]][next_pos[1]] = "@"
        grid[pos[0]][pos[1]] = "."
        pos = next_pos
    elif check_pos_in_nparray(grid, next_pos, "O"):
        print(instruction, "box")
        search_pos = next_pos + dir
        while check_pos_in_nparray(grid, search_pos, "O"):
            search_pos += dir
        if pos_in_nparray(grid, search_pos):
            if check_pos_in_grid(grid, search_pos, "."):
                boxes.remove(next_pos)
                boxes.append(search_pos)
                grid[search_pos[0]][search_pos[1]] = "O"
                grid[next_pos[0]][next_pos[1]] = "@"
                grid[pos[0]][pos[1]] = "."
                pos = next_pos
            if check_pos_in_grid(grid, search_pos, "#"):
                pass
    elif not pos_in_nparray(grid, next_pos) or check_pos_in_nparray(grid, next_pos, "#"):
        print(instruction, "wall")
        pass
    print(pos)
    print(grid)
for box in boxes:
    res += (box[0] + 1) * 100 + (box[1] + 1)

print(res)
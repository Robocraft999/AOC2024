from helpers import *
import numpy as np
import sys
path, testpath = get_input(15)
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())

def print_grid(grid):
    for y, line in enumerate(grid):
        for x, elem in enumerate(line):
            print(elem, end="")
        print()

def check_ud_move(grid, next_pos, rnext_pos, dir, rec=True):
    if not pos_in_nparray(grid, next_pos):
        return False
    #print("t", grid[next_pos[0]][next_pos[1]], grid[rnext_pos[0]][rnext_pos[1]], check_pos_in_nparray(grid, rnext_pos, "#"))
    if not rec and check_pos_in_grid(grid, next_pos, "]"):
        return check_ud_move(grid, next_pos-(0,1), next_pos, dir)
    if check_pos_in_nparray(grid, next_pos, "#") or check_pos_in_nparray(grid, rnext_pos, "#"):
        #current pos is blocked
        return False
    elif check_pos_in_nparray(grid, next_pos, "."):
        if check_pos_in_nparray(grid, rnext_pos, "."):
            #current pos is empty
            return True
        elif check_pos_in_nparray(grid, rnext_pos, "["):
            return check_ud_move(grid, rnext_pos+dir, rnext_pos+dir+(0,1), dir)
    elif check_pos_in_nparray(grid, rnext_pos, "."):
        if check_pos_in_nparray(grid, next_pos, "]"):
            return check_ud_move(grid, next_pos+dir-(0,1), next_pos+dir, dir)
    elif check_pos_in_nparray(grid, next_pos, "["):
        #box directly above
        return check_ud_move(grid, next_pos+dir, rnext_pos+dir, dir)
    else:
        #two boxes above
        left_check = check_ud_move(grid, next_pos+dir-(0,1), next_pos+dir, dir)
        right_check = check_ud_move(grid, rnext_pos+dir, rnext_pos+dir+(0,1), dir)
        return left_check and right_check
    
def ud_move(grid, next_pos, dir):
    target_pos = next_pos + dir
    if check_pos_in_grid(grid, next_pos, "]"):
        #print(".@\n[]")
        ud_move(grid, next_pos-(0,1), dir)
    if check_pos_in_grid(grid, target_pos, ".") and check_pos_in_grid(grid, target_pos+(0,1), "."):
        #print("@.\n[]\n..")
        pass
    elif check_pos_in_grid(grid, target_pos, "["):
        #print("@.\n[]\n[]")
        ud_move(grid, target_pos, dir)
    else:
        if check_pos_in_grid(grid, target_pos, "]"):
            #print("@.\n[]\n] ")
            ud_move(grid, target_pos-(0,1), dir)
        if check_pos_in_grid(grid, target_pos+(0,1), "["):
            #print("@.\n[]\n [")
            ud_move(grid, target_pos+(0,1), dir)
    grid[target_pos[0]][target_pos[1]] = grid[next_pos[0]][next_pos[1]]
    grid[target_pos[0]][target_pos[1]+1] = grid[next_pos[0]][next_pos[1]+1]
    grid[next_pos[0]][next_pos[1]] = "."
    grid[next_pos[0]][next_pos[1]+1] = "."
    
def check_left_move(grid, next_pos):
    dir = (0,-1)
    search_pos = V2(next_pos[0], next_pos[1])
    while check_pos_in_nparray(grid, search_pos, "[") or check_pos_in_nparray(grid, search_pos, "]"):
        search_pos += dir
    if check_pos_in_nparray(grid, search_pos, "."):
        rsearch_pos = search_pos + (0,1)
        while search_pos != next_pos:
            grid[search_pos[0]][search_pos[1]] = grid[rsearch_pos[0]][rsearch_pos[1]]
            search_pos += (0,1)
            rsearch_pos+= (0,1)
        return True
    return False

def check_right_move(grid, next_pos):
    dir = (0,1)
    rsearch_pos = V2(next_pos[0], next_pos[1])
    while check_pos_in_nparray(grid, rsearch_pos, "[") or check_pos_in_nparray(grid, rsearch_pos, "]"):
        rsearch_pos += dir
    if check_pos_in_nparray(grid, rsearch_pos, "."):
        lsearch_pos = rsearch_pos - (0,1)
        while rsearch_pos != next_pos:
            grid[rsearch_pos[0]][rsearch_pos[1]] = grid[lsearch_pos[0]][lsearch_pos[1]]
            rsearch_pos -= (0,1)
            lsearch_pos -= (0,1)
        return True
    return False

res = 0
upper, lower = parse_as_two_parts(path, lambda x : x, lambda x: x)
grid = []
for line in upper[1:len(upper)-1]:
    grid_line = []
    for x in line[1:len(line)-1]:
        if x == "#":
            grid_line.append("#")
            grid_line.append("#")
        elif x == "@":
            grid_line.append("@")
            grid_line.append(".")
        elif x == ".":
            grid_line.append(".")
            grid_line.append(".")
        elif x == "O":
            grid_line.append("[")
            grid_line.append("]")
    grid.append(grid_line)
grid = np.array(grid)
positions = find_all_in_grid(grid, ["."])

instructions = ""
for line in lower:
    instructions += line
pos = positions["@"][0]
boxes = []
for left in positions["["]:
    boxes.append((left, left + (0,1)))

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
        #print(instruction, "moving to", next_pos)
        grid[next_pos[0]][next_pos[1]] = "@"
        grid[pos[0]][pos[1]] = "."
        pos = next_pos
    elif not pos_in_nparray(grid, next_pos) or check_pos_in_nparray(grid, next_pos, "#"):
        #print(instruction, "wall")
        pass
    elif instruction == "<":
        #print("box left")
        if check_left_move(grid, next_pos):
            grid[next_pos[0]][next_pos[1]] = "@"
            grid[pos[0]][pos[1]] = "."
            pos = next_pos
            #print("after left")
            #print_grid(grid)
    elif instruction == ">":
        #print("box right")
        if check_right_move(grid, next_pos):
            grid[next_pos[0]][next_pos[1]] = "@"
            grid[pos[0]][pos[1]] = "."
            pos = next_pos
            #print("after right")
            #print_grid(grid)
    elif instruction == "^" or instruction == "v":
        #print(instruction, "box up or down")
        #print_grid(grid)
        if check_ud_move(grid, next_pos, next_pos+(0,1), dir, False):
            if check_pos_in_grid(grid, next_pos, "["):
                ud_move(grid, next_pos, dir)
            else:
                ud_move(grid, next_pos-(0,1), dir)
            grid[next_pos[0]][next_pos[1]] = "@"
            grid[pos[0]][pos[1]] = "."
            pos = next_pos
            #print("after", instruction)
            #print_grid(grid)
        else:
            pass
            #print("blocked")
    
    #print(instruction)
    #print_grid(grid)
print_grid(grid)
for box in find_all_in_grid(grid, ["["], True)["["]:
    res += (box[0] + 1) * 100 + (box[1] + 2)

print(res)
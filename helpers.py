import requests
import numpy as np
from pathlib import Path
from math import cos, sin, pi

def get_input(day):
    path = f"day{day}/input.txt"
    testpath = f"day{day}/testinput.txt"
    if not Path(path).is_file():
        print("downloading input")
        session_cookie = open("secrets.txt").readline()
        cookies = dict(session=session_cookie)
        r = requests.get(f"https://adventofcode.com/2024/day/{day}/input", cookies=cookies)
        if r.status_code == 200:
            file = open(path, "w")
            file.write(r.text)
            file.close()
        else:
            print(f"Couldn't download input for day {day}: {r.status_code}: {r.text}")
    else:
        print("input cached")
    return (path, testpath)

class V2:
    def __init__(self, y=0, x=0):
        self.x = x
        self.y = y

    def of(tup):
        return V2(tup[0], tup[1])

    def __add__(self, other):
        if isinstance(other, V2):
            x = self.x + other.x
            y = self.y + other.y
            return V2(y, x)
        elif isinstance(other, int):
            return V2(self.y + other, self.x + other)
        elif isinstance(other, tuple) and len(other) == 2:
            x = self.x + other[1]
            y = self.y + other[0]
            return V2(y, x)
        else:
            raise TypeError(f"Unsupported type {type(other)} for operation '+'")
        
    def __sub__(self, other):
        if isinstance(other, V2):
            x = self.x - other.x
            y = self.y - other.y
            return V2(y, x)
        elif isinstance(other, int):
            return V2(self.y - other, self.x - other)
        elif isinstance(other, tuple) and len(other) == 2:
            x = self.x - other[1]
            y = self.y - other[0]
            return V2(y, x)
        else:
            raise TypeError(f"Unsupported type {type(other)} for operation '-'")
        
    def __mul__(self, other):
        if isinstance(other, V2):
            x = self.x * other.x
            y = self.y * other.y
            return V2(y, x)
        elif isinstance(other, int):
            return V2(self.y * other, self.x * other)
        elif isinstance(other, tuple) and len(other) == 2:
            x = self.x * other[1]
            y = self.y * other[0]
            return V2(y, x)
        else:
            raise TypeError(f"Unsupported type {type(other)} for operation '*'")
    
    def __floordiv__(self, other):
        if isinstance(other, V2):
            x = self.x // other.x
            y = self.y // other.y
            return V2(y, x)
        elif isinstance(other, int):
            return V2(self.y // other, self.x // other)
        elif isinstance(other, tuple) and len(other) == 2:
            x = self.x // other[1]
            y = self.y // other[0]
            return V2(y, x)
        else:
            raise TypeError(f"Unsupported type {type(other)} for operation '/'")
    
    def __iadd__(self, other):
        if isinstance(other, V2):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int):
            self.y += other
            self.x += other
        elif isinstance(other, tuple) and len(other) == 2:
            self.x += other[1]
            self.y += other[0]
        else:
            raise TypeError(f"Unsupported type {type(other)} for operation '+='")
        return self
    
    def __eq__(self, value):
        if isinstance(value, V2):
            return self.x == value.x and self.y == value.y
        elif isinstance(value, tuple) and len(value) == 2:
            return self.x == value[1] and self.y == value[0]
        return False
    
    def __abs__(self):
        return abs(self.x) + abs(self.y)
    
    def __getitem__(self, index):
        if index == 0:
            return self.y
        elif index == 1:
            return self.x
        raise IndexError(index)
    
    def __setitem__(self, index, value):
        if index == 0:
            self.y = value
            return self
        elif index == 1:
            self.x = value
            return self
        raise IndexError(index)

    def rotated90(self):
        x = round(self.x * cos(pi/2) + self.y * -sin(pi/2))
        y = round(self.x * sin(pi/2) + self.y *  cos(pi/2))
        return V2(y, x)
    
    def __repr__(self):
        return repr((self.y, self.x))
    
    def __hash__(self):
        return (self.y, self.x).__hash__()
    
### Mappers

def imap(string):
    return int(string)

def splitmap(string, mapper, char=None):
    return list(map(mapper, string.split(char)))

def nop(x):
    return x
    
### Parsing

def parse_lines_split(path, mapper=None, char=None):
    lines = []
    for line in open(path):
        splitted = []
        for elem in line.strip().split(char):
            if mapper is not None:
                splitted.append(mapper(elem))
        lines.append(splitted)
    return lines

def parse_as_text(path):
    text = ""
    for line in open(path):
        text += line.strip()
    return text

def parse_as_two_parts(path, upper_mapper=None, lower_mapper=None):
    upper = True
    upper_part = []
    lower_part = []
    for line in open(path):
        if line == "\n":
            upper = False
            continue
        line = line.strip()
        if upper:
            if upper_mapper != None:
                line = upper_mapper(line)
            upper_part.append(line)
        else:
            if lower_mapper != None:
                line = lower_mapper(line)
            lower_part.append(line)
    return (upper_part, lower_part)



def parse_as_grid(path, mapper=None):
    grid = []
    for line in open(path):
        line = line.strip()
        if mapper is not None:
            line = mapper(line)
        grid.append(line)
    return grid

def parse_as_nparray(path, mapper=None):
    if mapper != None:
        line_mapper = lambda line: mapper([x for x in line])
    else:
        line_mapper = lambda line: [x for x in line]
    grid = parse_as_grid(path, mapper=line_mapper)
    return np.array(grid)

### Grid

class Grid:
    def __init__(self, inner):
        self.inner = inner

    def __getitem__(self, index):
        if isinstance(index, V2) or (isinstance(index, tuple) and len(index) == 0):
            return self.inner[index[0]][index[1]]
        elif isinstance(index, int):
            return self.inner[index]
        else:
            raise KeyError()
        
    def __setitem__(self, index, item):
        if isinstance(index, V2) or (isinstance(index, tuple) and len(index) == 0):
            self.inner[index[0]][index[1]] = item
            return self
        else:
            raise KeyError()
        
    def __repr__(self):
        return str(self.inner)


def find_in_grid(grid, element):
    for y, line in enumerate(grid):
        for x, e in enumerate(line):
            if e == element:
                return (y, x)
    return (-1, -1)

def find_all_in_grid(grid, ignore=[], inverted=False):
    positions = {}
    for y, line in enumerate(grid):
        for x, e in enumerate(line):
            if inverted ^ (e in ignore):
            #if (inverted is True and e not in ignore) or (inverted is not True and e in ignore):
                continue
            if e not in positions:
                positions[str(e)] = [V2(y,x)]
            else:
                positions[str(e)].append(V2(y,x))
    return positions

def check_pos_in_grid(grid, pos, element):
    return grid[pos[0]][pos[1]] == element

def check_pos_in_nparray(grid, pos, element):
    if not pos_in_nparray(grid, pos):
        return False
    return check_pos_in_grid(grid, pos, element)

def pos_in_nparray(grid, pos, padding=0):
    return pos[0] >= (0 + padding) and pos[0] < grid.shape[0]-padding and pos[1] >= (0 + padding) and pos[1] < grid.shape[1]-padding


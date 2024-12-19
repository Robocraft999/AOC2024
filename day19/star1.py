from helpers import *
import numpy as np
from tqdm import tqdm
path, testpath = get_input(19)

def matches(string: str, parts):
    if len(string) == 0:
        return True
    for part in parts:
        if string.startswith(part):
            if matches(string[len(part):], parts):
                return True
    #print(string, matched)
    return False

res = 0
upper, lower = parse_as_two_parts(path, lambda x: splitmap(x, lambda x: x, ", "), lambda x: x)
upper = upper[0]
for line in tqdm(lower):
    if matches(line, upper):
        res += 1

print(res)
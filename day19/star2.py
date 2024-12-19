from helpers import *
import numpy as np
from tqdm import tqdm
from functools import lru_cache
path, testpath = get_input(19)

@lru_cache(maxsize=None)
def matches(string: str):
    if len(string) == 0:
        return 1
    matched = 0
    for part in upper:
        if string.startswith(part):
            matched += matches(string[len(part):])
    return matched

res = 0
upper, lower = parse_as_two_parts(path, lambda x: splitmap(x, lambda x: x, ", "), lambda x: x)
upper = upper[0]
for line in tqdm(lower):
    res += matches(line)

print(res)
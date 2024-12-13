from helpers import *
from tqdm import tqdm
import functools
path, testpath = get_input(11)

res = 0
stones = list(map(int, parse_as_text(path).split()))
expansions = {}

@functools.lru_cache(maxsize=None)
def new_nums(i, stone):
    s = str(stone)
    d = len(s)
    if i == 0:
        return 1
    else:
        if stone == 0:
            return new_nums(i-1, 1)
        elif d % 2 == 0:
            return new_nums(i-1, int(s[:d//2])) + new_nums(i-1, int(s[d//2:]))
        else:
            return new_nums(i-1, stone * 2024)

print(stones)
for stone in tqdm(stones):
    res += new_nums(25, stone)

print(new_nums.cache_info())
print(res)
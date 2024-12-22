from helpers import *
import numpy as np
from tqdm import tqdm
from math import floor
from itertools import permutations, combinations
from functools import cache, lru_cache
path, testpath = get_input(22)

@cache
def next_num(num):
    r = (num ^ (num << 6)) % 16777216
    r = (floor(r >> 5) ^ r) % 16777216
    r = (r ^ (r << 11)) % 16777216
    return r

def build_combs():
    combs = []
    for i in range(-9, 10):
        for j in range(-9, 10):
            for k in range(-9, 10):
                for l in range(-9, 10):
                    combs.append((i, j, k, l))
    return combs

@lru_cache(maxsize=100000)
def get_indices(j, first, second):
    x = all_diffs[j][:-3]
    return [i for i in np.where(x == first)[0] if all_diffs[j][i+1] == second]

res = 0
sequence = list(range(-9, 10))
lines = list(open(path))
all_diffs = []
all_values = []
for line in lines:
    num = int(line.strip())
    value = num % 10
    diffs = []
    values = []
    for i in range(2000):
        num = next_num(num)
        new_value = num%10
        diffs.append(new_value - value)
        values.append(new_value)
        value = new_value
    all_diffs.append(np.array(diffs))
    all_values.append(values)
len_diffs = len(all_diffs)

for seq in tqdm(build_combs()):
    summ = 0
    for j, diffs in enumerate(all_diffs):
        if ((len_diffs - j) * 9 + summ) < res:
            break
        for i in get_indices(j, seq[0], seq[1]):
            if diffs[i+2] == seq[2] and diffs[i+3] == seq[3]:
                summ += all_values[j][i+3]
                break

    res = max(res, summ)
print(res)
from helpers import *
import numpy as np
from tqdm import tqdm
from math import floor
path, testpath = get_input(22)

def next_num(num, t):
    r = (num ^ (num << 6)) % 16777216
    r = (floor(r >> 5) ^ r) % 16777216
    r = (r ^ (r << 11)) % 16777216
    return r


res = 0
for line in tqdm(list(open(path))):
    num = int(line.strip())
    for i in range(2000):
        num = next_num(num, i)
        #print(num)

    #print(num)
    res += num

print(res)
from helpers import *
import numpy as np
from tqdm import tqdm
from numba import prange, njit, cuda
from numba.cuda import jit
import time
path, testpath = get_input(22)

def vectorized_next_nums(nums, iterations=2000):
    results = np.zeros((len(nums), iterations), dtype=np.int32)
    current_nums = nums.copy()

    for i in range(iterations):
        current_nums = (current_nums ^ (current_nums << 6)) % 16777216
        current_nums = ((current_nums >> 5) ^ current_nums) % 16777216
        current_nums = (current_nums ^ (current_nums << 11))% 16777216
        results[:, i] = current_nums % 10
    return results

def build_combs():
    nums = np.arange(-9, 10)
    grid = np.meshgrid(nums, nums, nums, nums)
    return np.array(grid).T.reshape(-1, 4)

@jit
def calc_for_all_sequences(summ, sequences, len_diffs, all_diffs, all_values):
    tx = cuda.threadIdx.x
    bx = cuda.blockIdx.x
    bw = cuda.blockDim.x
    tid = bx * bw + tx
    if tid >= len(sequences):
        return

    for j in range(len_diffs):
        for i, x in enumerate(all_diffs[j][:-3]):
            if x == sequences[tid][0] and all_diffs[j][i+1] == sequences[tid][1] and all_diffs[j][i+2] == sequences[tid][2] and all_diffs[j][i+3] == sequences[tid][3]:
                summ[tid][j] = all_values[j][i+4]
                break

@njit(parallel=True)
def calc_for_all_sequences_cpu(summ, sequences, len_diffs, all_diffs, all_values):
    c_all_diffs = all_diffs
    c_all_values = all_values
    c_sequences = sequences
    for k, _ in enumerate(c_sequences):
        for j in prange(len_diffs):
            for i, x in enumerate(c_all_diffs[j][:-3]):
                if x == c_sequences[k][0] and c_all_diffs[j][i+1] == c_sequences[k][1] and c_all_diffs[j][i+2] == c_sequences[k][2] and c_all_diffs[j][i+3] == c_sequences[k][3]:
                    summ[k][j] = c_all_values[j][i+4]
                    break

res = 0
nums = np.array([int(line.strip()) for line in open(path)])
all_values = vectorized_next_nums(nums)
all_diffs = np.diff(all_values, axis=1)
combs = build_combs()

start = time.process_time()

d_all_diffs = cuda.to_device(all_diffs)
d_all_values = cuda.to_device(all_values)
d_combs = cuda.to_device(combs)

summ = np.zeros([len(combs), len(all_diffs)])
d_summ = cuda.to_device(summ)
threadsperblock = 64
blockspergrid = summ.shape[0] + threadsperblock - 1

calc_for_all_sequences[blockspergrid, threadsperblock](d_summ, d_combs, len(all_diffs), d_all_diffs, d_all_values)
summ = d_summ.copy_to_host()
#calc_for_all_sequences_cpu(summ, combs, len(all_diffs), all_diffs, all_values)
print(time.process_time() - start)

for psum in summ:
    res = max(res, np.sum(psum))
print(res)
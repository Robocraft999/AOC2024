from helpers import *
import numpy as np
from tqdm import tqdm
import itertools
path, testpath = get_input(23)

graph = {}
for left, right in parse_lines_split(path, nop, "-"):
    graph.setdefault(left, []).append(right)
    graph.setdefault(right, []).append(left)

groups = []

def t(k):
    nodes = graph[k] + [k]
    inter = set(nodes)
    subnodes = set()
    for x in graph[k]:
        subnodes = subnodes.union(graph[x])
    return inter.intersection(subnodes)

for k in graph:
    inter = t(k)
    flag = True
    for x in inter:
        if t(x) != inter:
            flag = False
            break
    if flag and inter not in groups:
        groups.append(inter)
groups = sorted(groups, key=lambda x: len(x))

print(",".join(sorted(groups[-1])))
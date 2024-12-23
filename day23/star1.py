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
for k in graph:
    for l, r in itertools.combinations(graph[k], 2):
        if l in graph[r]:
            group = set((k, l, r))
            if group not in groups and (k.startswith("t") or l.startswith("t") or r.startswith("t")):
                groups.append(group)

print(len(groups))
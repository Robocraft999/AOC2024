from helpers import *
path, testpath = get_input(7)

res = 0
for line in open(path):
    left, right = line.split(": ")
    left, right = int(left), list(map(int, right.split()))
    print(left, right)
    results = [right[0]]
    for i, num in enumerate(right[1:]):
        new_results = []
        for last in results:
            new_results.append(last * num)
            new_results.append(last + num)
            new_results.append(int(str(last) + str(num)))
        results = new_results
    if left in results:
        res += left

print(res)
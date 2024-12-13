from helpers import *
path, testpath = get_input(5)

res = 0
rules, updates = parse_as_two_parts(testpath, lambda x: splitmap(x, int, "|"), lambda x: splitmap(x, int, ","))

a=0
for i, update in enumerate(updates):
    flag2 = False
    for j, num in enumerate(update):
        for pair in rules:
            if num in pair:
                first, second = 0,0
                if num == pair[0]:
                    first, second = num, pair[1]
                    if second not in update[j:] and second in update:
                        flag2 = True
                        break
                else:
                    first, second = pair[0], num
                    if first not in update[:j] and first in update:
                        flag2 = True
                        break
        if flag2:
            break
    if not flag2:
        a += 1
        res += update[len(update)//2]

print(res, a, len(updates))
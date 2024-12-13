from helpers import *
path, testpath = get_input(5)

res = 0
rules = []
updates = []
flag = False
for line in open(path):
    if not flag:
        if line == "\n":
            flag = True
            continue
        left, right = line.strip().split("|")
        rules.append([int(left), int(right)])
    else:
        updates.append([int(x) for x in line.strip().split(",")])
a=0
for i, update in enumerate(updates):
    flag2 = False
    for j, num in enumerate(update):
        #print("num", num)
        for pair in rules:
            #print("pair", pair)
            if num in pair:
                first, second = 0,0
                #print(update, num)
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
                #print(update, num, pair, first, second)
        if flag2:
            break
    if not flag2:
        a += 1
        #print(update)
        res += update[len(update)//2]

print(res, a, len(updates))
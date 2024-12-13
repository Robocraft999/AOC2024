from helpers import *
path, testpath = get_input(1)

sum = 0
list1 = []
list2 = []
for line in open(path):
    x,y = line.split()
    list1.append(int(x))
    list2.append(int(y))
print(list1, list2)
for x in list1:
    sum += list2.count(x) * x

print(sum)
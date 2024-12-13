from helpers import *
path, testpath = get_input(1)

sum = 0
list1 = []
list2 = []
for line in open(path):
    x,y = line.split()
    list1.append(int(x))
    list2.append(int(y))
while len(list1) > 0:
    mix = min(list1)
    list1.remove(mix)
    miny = min(list2)
    list2.remove(miny)
    sum += abs(mix - miny)

print(sum)


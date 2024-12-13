from helpers import *
path, testpath = get_input(2)

def t(elements):
    unsaf = False
    inc = None
    for i,e in enumerate(elements[1:]):
        e = int(e)
        f = int(elements[i])
        if inc == None:
            inc = e > f
        
        flag = None
        if inc == True:
            flag = e > f
        else:
            flag = e < f
        if not (flag and 1 <= (abs(e - f) < 4)):
            unsaf = True
            break
    return unsaf

sum = 0
for line in open(path):
    elements = line.split()

    if t(elements) == False:
        sum += 1

print(sum)
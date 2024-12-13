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

    unsaf = t(elements)
    for i in range(len(elements)):
        elems = elements.copy()
        elems.pop(i)
        if t(elems) == False:
            sum += 1
            break

print(sum)